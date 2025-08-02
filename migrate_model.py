import psycopg2
from psycopg2.extras import execute_batch
from gensim.models import Word2Vec
import os

# --- IMPORTANT: Replace with your database credentials ---
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

print("Loading local Word2Vec model...")
w2v_model = Word2Vec.load("product_w2v.model")
print("Model loaded.")

all_embeddings = []
for product_id in w2v_model.wv.index_to_key:
    embedding = w2v_model.wv[product_id].tolist()
    all_embeddings.append((product_id, embedding))

try:
    print("Connecting to the database...")
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
        host=DB_HOST, port=DB_PORT
    )
    cur = conn.cursor()
    print("Connection successful.")
    
    print(f"Migrating {len(all_embeddings)} embeddings to the database in batches...")
    query = "INSERT INTO product_embeddings (product_id, embedding) VALUES (%s, %s) ON CONFLICT (product_id) DO NOTHING;"
    execute_batch(cur, query, all_embeddings, page_size=1000)

    conn.commit()
    cur.close()
    conn.close()
    print("Migration complete.")

except Exception as e:
    print(f"An error occurred: {e}")