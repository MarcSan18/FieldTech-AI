import pandas as pd
import chromadb

client = chromadb.Client()
collection = client.create_collection("chamados")

df = pd.read_csv("data/chamados.csv")

for i, row in df.iterrows():
    texto = f"Problema: {row['problema']} | Causa: {row['causa']} | Solução: {row['solucao']}"
    
    collection.add(
        documents=[texto],
        ids=[str(i)]
    )

print("Base carregada com sucesso!")