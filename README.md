# 🚀 FieldTech AI

Assistente inteligente para suporte técnico em campo, utilizando IA, base de conhecimento (RAG), memória de atendimentos e leitura de manuais técnicos.

---

## 📌 Visão Geral

O **FieldTech AI** foi desenvolvido para auxiliar técnicos de TI no diagnóstico e resolução de problemas em campo, combinando:

* 🔍 Busca de contexto em base de dados (RAG)
* 🧠 Memória de atendimentos anteriores (SQLite)
* 📄 Leitura de manuais técnicos (PDF)
* 🤖 Integração com modelo de IA

O objetivo é reduzir tempo de diagnóstico, padronizar soluções e reaproveitar conhecimento técnico.

---

## 🧱 Arquitetura do Projeto

```
FieldTech-AI/
│
├── app/
│   ├── main.py                # API (FastAPI)
│   ├── services/
│   │   ├── ai_service.py      # Lógica principal da IA
│   │   ├── memory_service.py  # Persistência de memória (SQLite)
│   │   ├── retriever_service.py # Busca de contexto (RAG)
│   │   └── pdf_service.py     # Leitura de manuais PDF
│   │
│   ├── core/
│   │   └── config.py
│
├── data/
│   └── manuais/               # PDFs técnicos
│
├── db/                        # Banco de dados SQLite
│
├── .env                       # Variáveis de ambiente
├── requirements.txt
└── README.md
```

---

## ⚙️ Tecnologias Utilizadas

* Python
* FastAPI
* OpenAI API
* ChromaDB
* SQLite
* PyPDF
* python-dotenv

---

## 🔧 Configuração do Ambiente

### 1. Clone o projeto

```bash
git clone <url-do-repositorio>
cd FieldTech-AI
```

---

### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configure o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave_aqui
```

---

## 🚀 Execução do Projeto

### ▶️ Rodar API

```bash
python -m uvicorn app.main:app --reload
```

---

### 🌐 Acessar documentação

Abra no navegador:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Exemplo de Uso

### Endpoint: `POST /chat`

```json
{
  "pergunta": "Notebook não liga"
}
```

### Resposta esperada:

```
1. Causa provável: ...
2. Diagnóstico: ...
3. Solução: ...
```

---

## 🧠 Funcionalidades

* ✔ Busca inteligente por contexto (RAG)
* ✔ Aprendizado contínuo com memória de atendimentos
* ✔ Leitura de manuais técnicos em PDF
* ✔ API REST para integração com outros sistemas

---

## 🔄 Fluxo de Funcionamento

1. Usuário envia pergunta
2. Sistema busca contexto semelhante (ChromaDB)
3. Recupera histórico de atendimentos (SQLite)
4. Consulta manual técnico (PDF)
5. IA gera resposta baseada nas fontes
6. Resposta é armazenada para aprendizado futuro

---

## 📈 Evoluções Futuras

* Interface web (frontend)
* Upload dinâmico de PDFs
* Classificação automática de chamados
* Dashboard de atendimentos
* Deploy em nuvem

---

## 👨‍💻 Autor

Projeto desenvolvido como parte de estudo prático em Inteligência Artificial aplicada ao suporte técnico, com foco em entrada no mercado de tecnologia.

---

## 📌 Observação

Este projeto simula um ambiente real de suporte técnico, aplicando boas práticas de arquitetura, integração de IA e organização de código.
