import psycopg2
import os
# --- IMPORTANT: Replace with your database credentials ---
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

try:
    print("Connecting to the database...")
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
        host=DB_HOST, port=DB_PORT
    )
    cur = conn.cursor()
    print("Connection successful.")

    print("Enabling 'vector' extension...")
    cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")

    print("Creating 'product_embeddings' table...")
    cur.execute("CREATE TABLE IF NOT EXISTS product_embeddings (product_id VARCHAR(255) PRIMARY KEY, embedding vector(100));")
    
    conn.commit()
    cur.close()
    conn.close()
    print("Database setup complete.")

except Exception as e:
    print(f"An error occurred: {e}")