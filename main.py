from fastapi import FastAPI
from gensim.models import Word2Vec

# Initialize the FastAPI app
app = FastAPI(
    title="Project Echo Recommendation API",
    description="An advanced API serving recommendations from a Word2Vec model."
)

# Load the saved Word2Vec model
print("Loading Word2Vec model...")
w2v_model = Word2Vec.load("product_w2v.model")
print("Model loaded successfully.")

# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Word2Vec Recommendation API!"}

# Define the recommendation endpoint
@app.get("/recommend/{item_id}")
def get_recommendations(item_id: str, top_n: int = 10):
    """
    Get top N recommendations for a given item_id.
    """
    try:
        # Get the top N most similar items from the model's vocabulary
        similar_items = w2v_model.wv.most_similar(item_id, topn=top_n)
        
        # Extract just the item IDs
        recommendations = [item for item, score in similar_items]
        
        return {"item_id": item_id, "recommendations": recommendations}
    except KeyError:
        # Handle cases where the item_id is not in the model's vocabulary
        return {"error": f"Item ID '{item_id}' not found in the model."}