import sqlite3

# conexão com banco
conn = sqlite3.connect("db/memoria.db")
cursor = conn.cursor()

# criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS memoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    problema TEXT,
    resposta TEXT
)
""")

conn.commit()

# salvar dados
def salvar_memoria(problema, resposta):
    cursor.execute(
        "INSERT INTO memoria (problema, resposta) VALUES (?, ?)",
        (problema, resposta)
    )
    conn.commit()

# buscar memória
def buscar_memoria(pergunta):
    cursor.execute(
        "SELECT problema, resposta FROM memoria WHERE problema LIKE ? LIMIT 2",
        (f"%{pergunta}%",)
    )
    return cursor.fetchall()