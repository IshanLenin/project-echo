# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container first (good for caching)
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# --- THE FIX: Copy the trained model file ---
# Copy the large model file specifically before the rest of the code
COPY product_w2v.model /app/product_w2v.model

# Copy the rest of the application's code into the container
COPY . .

# Expose the port (already done implicitly by uvicorn command, but good practice)
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

