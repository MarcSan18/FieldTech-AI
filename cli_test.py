# cli_test.py

from app.services.ai_service import responder

print("🧪 Modo teste (CLI) iniciado...")

while True:
    pergunta = input("\nTécnico: ")

    if pergunta.lower() in ["sair", "exit"]:
        break

    resposta = responder(pergunta)
    print("\n🧠 IA:\n", resposta)