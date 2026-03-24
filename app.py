from openai import OpenAI
from dotenv import load_dotenv
import os
from retriever import buscar_contexto
from memory import salvar_memoria, buscar_memoria
from pdf_loader import carregar_pdf

pdf_texto = carregar_pdf("data/manuais/Manual-de-Servicos-Positivo-Master-N6450_N8450.pdf")

# carregar variáveis
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ API KEY não encontrada no .env")
    exit()

client = OpenAI(api_key=api_key)

print("🚀 FieldTech AI iniciado...")

while True:
    try:
        pergunta = input("\nTécnico: ")

        if pergunta.lower() in ["sair", "exit"]:
            print("Encerrando sistema...")
            break

        # 🔍 buscar dados
        contexto = buscar_contexto(pergunta)
        memorias = buscar_memoria(pergunta)

        # 🤖 chamada da IA
        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"""
Você é um especialista técnico.

Use:

Base:
{contexto}

Memória:
{memorias}

Manual:
{pdf_texto[:2000]}

Responda com:
1. Causa
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

        print("\n🧠 IA:\n", resposta_texto)

        # 💾 salvar aprendizado
        salvar_memoria(pergunta, resposta_texto)

    except Exception as e:
        print("\n⚠️ Erro na API:", e)
        print("\n💡 Resposta baseada no contexto:")

        if contexto:
            for item in contexto:
                print("-", item)
        else:
            print("Sem dados disponíveis.")