from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app

# Create a test client for your app
client = TestClient(app)

def test_read_root():
    """
    Test that the root endpoint ("/") returns a 200 OK status code
    and the correct welcome message.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Word2Vec Recommendation API!"}

def test_get_recommendations():
    """
    Test the /recommend/{item_id} endpoint.
    It should return a 200 OK status code and a JSON object
    with the correct keys and a list of 10 recommendations.
    """
    # Use a known valid item ID from your model
    test_item_id = 1005115
    
    response = client.get(f"/recommend/{test_item_id}")
    
    # Check that the request was successful
    assert response.status_code == 200
    
    # Check the structure of the JSON response
    response_data = response.json()
    assert "item_id" in response_data
    assert "recommendations" in response_data
    
    # Check that we got a list of 10 recommendations back
    assert isinstance(response_data["recommendations"], list)
    assert len(response_data["recommendations"]) == 10