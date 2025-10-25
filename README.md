**Project Echo: End-to-End Session-Based Recommendation Engine**


[![CI/CD Pipeline for Recommendation API](https://github.com/IshanLenin/project-echo/actions/workflows/deploy.yml/badge.svg)](https://github.com/IshanLenin/project-echo/actions/workflows/deploy.yml)

**A complete MLOps pipeline designed and deployed to serve real-time, session-based product recommendations via a secure REST API. This project demonstrates proficiency in data engineering, model training, containerization, cloud deployment, and CI/CD automation.**

**Live Demo**: https://reco.ishan-visionary.tech

**Motivation & Problem Solved**

Traditional recommendation systems often rely on user history, which isn't available for new or anonymous users. This project tackles the challenge of providing relevant product recommendations based only on a user's current browsing session. The goal was to build not just a model, but the entire production infrastructure required to train, deploy, and serve these recommendations reliably and efficiently, automating the process with a CI/CD pipeline.

**Tech Stack**

**Cloud Provider**: DigitalOcean (Droplet)

**Web Server / Proxy**: Nginx

**Application Framework**: FastAPI (Python)

**Database**: PostgreSQL

**ML Model**: Word2Vec (Gensim)

**Data Processing**: Pandas

**Containerization**: Docker

**CI/CD**: GitHub Actions

**Key Features & Learnings**

Full MLOps Pipeline: Architected the entire lifecycle from data ingestion and cleaning to model training, API serving, and automated deployment.

Large-Scale Data Engineering: Developed a robust data pipeline using Pandas to efficiently process and transform a massive 42-million-row e-commerce dataset.

Custom Model Training: Implemented and trained a Word2Vec model using Gensim to generate meaningful vector embeddings for over 127,000 products, enabling recommendations even for unseen item combinations.

Scalable API Deployment: Built a secure and performant REST API using FastAPI, containerized it with Docker, and deployed it behind an Nginx reverse proxy on a cloud server.

CI/CD Automation: Created a complete Continuous Integration and Continuous Deployment pipeline using GitHub Actions to automatically test, build, and deploy the application upon code changes.

**Getting Started (Local Setup)**

**Clone the repository:**

git clone [https://github.com/IshanLenin/project-echo.git](https://github.com/IshanLenin/project-echo.git)
cd project-echo


Set up environment variables: Create a .env file based on .env.example (if applicable). Consider adding an example file if you don't have one.

Build and run using Docker Compose (Recommended):

# Ensure you have Docker Compose installed
docker-compose up --build -d


Access the API at http://localhost:8000. (Adjust port if different)
