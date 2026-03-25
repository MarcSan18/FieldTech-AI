from openai import OpenAI
from dotenv import load_dotenv
import os

from app.services.retriever_service import buscar_contexto
from app.services.memory_service import buscar_memoria, salvar_memoria
from app.services.pdf_service import carregar_pdf

# ==============================
# 🔐 CONFIGURAÇÃO
# ==============================
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise Exception("API KEY não encontrada no .env")

client = OpenAI(api_key=api_key)

# ==============================
# 📄 CARREGAR MANUAL UMA VEZ
# ==============================
try:
    caminho_pdf = "data/manuais/Manual-de-Servicos-Positivo-Master-N6450_N8450.pdf"
    pdf_texto = carregar_pdf(caminho_pdf)
    pdf_resumo = pdf_texto[:2000] if pdf_texto else "Manual vazio"
except Exception as e:
    print("Erro ao carregar PDF:", e)
    pdf_resumo = "Manual não disponível"


# ==============================
# 🧠 FUNÇÃO PRINCIPAL
# ==============================
def responder(pergunta: str) -> str:

    # 🔍 buscar contexto
    contexto = buscar_contexto(pergunta) or []
    memorias = buscar_memoria(pergunta) or []

    # 🧠 formatar memória
    memoria_formatada = "\n".join(
        [f"Problema: {m[0]} | Solução: {m[1]}" for m in memorias]
    ) if memorias else "Sem histórico relevante"

    try:
        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"""
Você é um especialista técnico em suporte de TI.

Use as fontes abaixo:

🔹 Base de conhecimento:
{contexto}

🔹 Histórico de atendimentos:
{memoria_formatada}

🔹 Manual técnico:
{pdf_resumo}

Responda de forma objetiva e técnica com:

1. Causa provável
2. Diagnóstico
3. Solução
"""
                },
                {
                    "role": "user",
                    "content": pergunta
                }
            ]
        )

        resposta_texto = resposta.choices[0].message.content

        # 💾 salvar aprendizado
        salvar_memoria(pergunta, resposta_texto)

        return resposta_texto

    except Exception as e:
        print("Erro na API:", e)

        # 🔁 fallback inteligente
        if contexto:
            return "\n".join(contexto)

        return "Sem dados suficientes para responder."