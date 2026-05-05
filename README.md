# Bank Marketing Prediction API

[![Simple Test](https://github.com/mcml1225/bank_marketing-ml/actions/workflows/simple-test.yml/badge.svg)](https://github.com/mcml1225/bank_marketing-ml/actions/workflows/simple-test.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/mcml1225/bank_marketing-ml)
[![GitHub last commit](https://img.shields.io/github/last-commit/mcml1225/bank_marketing-ml.svg)](https://github.com/mcml1225/bank_marketing-ml)

---

## Overview

Machine Learning API that predicts whether a bank customer will subscribe to a term deposit. Built with **FastAPI**, **scikit-learn**, and **Docker**.

**Accuracy: 89.3% | Response Time: ~18ms | Model: Random Forest**

---

## Key Features

- Real-time predictions (~18ms response time)
- 89.3% model accuracy (Random Forest Classifier)
- Auto-generated API documentation (Swagger UI + ReDoc)
- CI/CD pipeline with GitHub Actions
- Docker containerization for consistent deployment
- Complete SDLC documentation (SRS, Architecture, Tests, Manual)

---

## Project Structure
```
bank_marketing-ml/
├── app/ # API application
│ ├── main.py # FastAPI endpoints
│ ├── model.pkl # Trained model
│ └── columns.pkl # Model columns
├── models/ # Training module
│ └── train.py # Model training script
├── docs/ # SDLC Documentation
│ ├── 01_SRS_Requirements.md
│ ├── 02_Architecture_Design.md
│ ├── 03_Test_Plan.md
│ ├── 04_User_Manual.md
│ └── 05_Deployment_Guide.md
├── tests/ # Test suite
│ ├── test_api.py
│ └── test_performance_simple.py
├── .github/workflows/ # CI/CD
│ ├── deploy.yml
│ └── simple-test.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Quick Start

```bash
# Clone repository
git clone https://github.com/mcml1225/bank_marketing-ml.git
cd bank_marketing-ml

# Install dependencies
pip install -r requirements.txt

# Train model
python models/train.py

# Run API
cd app && uvicorn main:app --reload
Then visit: http://localhost:8000/docs

API Endpoints
Method	Endpoint	Description
GET	/	Service status
GET	/health	Health check
POST	/predict	Make prediction
GET	/docs	Swagger UI documentation
GET	/redoc	ReDoc documentation
Example Request
bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 35,
    "job": "management",
    "marital": "married",
    "education": "university.degree",
    "default": "no",
    "balance": 2500,
    "housing": "yes",
    "loan": "no",
    "contact": "cellular",
    "day": 15,
    "month": "may",
    "campaign": 1,
    "pdays": -1,
    "previous": 0,
    "poutcome": "unknown"
  }'
Example Response
json
{
  "subscription": "No",
  "probability": 0.170
}
Model Performance
Metric	Value
Accuracy	89.3%
Response Time	~18ms
Model Size	80MB
Algorithm	Random Forest
Training Data	UCI Bank Marketing Dataset
Running Tests
bash
# Install test dependencies
pip install pytest pytest-cov

# Run performance tests
python tests/test_performance_simple.py

# Run all tests
pytest tests/ -v

# Run with coverage report
pytest tests/ --cov=app --cov-report=html
Docker Deployment
bash
# Build image
docker build -t bank-marketing-api .

# Run container
docker run -d -p 8000:8000 --name bank-api bank-marketing-api

# Check logs
docker logs -f bank-api

# Stop container
docker stop bank-api
SDLC Documentation
Document	Description
SRS Requirements	Functional & non-functional requirements
Architecture Design	System architecture & components
Test Plan	Testing strategy & test cases
User Manual	API usage guide
Deployment Guide	Deployment strategies
Technology Stack
Component	Technology
API Framework	FastAPI
ML Library	scikit-learn
Serialization	joblib
Container	Docker
CI/CD	GitHub Actions
Data Source	UCI ML Repository
Testing	pytest
Version Control	Git
Project Status (SDLC Phases)
Phase	Status
Requirements	Complete
Design	Complete
Implementation	Complete
Testing	Complete
Deployment	Ready
Maintenance	Active
Contributing
Contributions, issues, and feature requests are welcome.

Fork the project

Create your feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add some amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

Author
mcml1225

GitHub: @mcml1225

License
Distributed under the MIT License. See LICENSE file for more information.

Acknowledgments
UCI Machine Learning Repository for the dataset

FastAPI for the amazing framework

GitHub Actions for CI/CD

scikit-learn for the ML library
<<<<<<< Updated upstream
=======

scikit-learn for the ML library

>>>>>>> Stashed changes
