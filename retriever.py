import chromadb

client = chromadb.Client()

# garante que a coleção existe
try:
    collection = client.get_collection("chamados")
except:
    collection = client.create_collection("chamados")

def buscar_contexto(pergunta):
    resultado = collection.query(
        query_texts=[pergunta],
        n_results=2
    )

    # evita erro se não tiver dados
    if not resultado["documents"]:
        return ["Sem dados encontrados"]

    return resultado["documents"][0]