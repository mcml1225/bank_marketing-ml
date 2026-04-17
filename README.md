# 🏦 Bank Marketing Prediction API

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/mcml1225/bank_marketing-ml)
[![GitHub last commit](https://img.shields.io/github/last-commit/mcml1225/bank_marketing-ml.svg)](https://github.com/mcml1225/bank_marketing-ml)
[![Simple Test](https://github.com/mcml1225/bank_marketing-ml/actions/workflows/simple-test.yml/badge.svg)](https://github.com/mcml1225/bank_marketing-ml/actions/workflows/simple-test.yml)

<!-- Badge de CI/CD aparecerá automáticamente cuando el workflow pase -->
<!-- [![CI/CD Pipeline](https://github.com/mcml1225/bank_marketing-ml/actions/workflows/deploy.yml/badge.svg)](https://github.com/mcml1225/bank_marketing-ml/actions) -->

## 📊 Overview
...



Machine Learning API that predicts whether a bank customer will subscribe to a term deposit. Built with \*\*FastAPI\*\*, \*\*scikit-learn\*\*, and \*\*Docker\*\*. Implements professional \*\*SDLC\*\* practices including CI/CD, comprehensive testing, and full documentation.



\*\*Accuracy: 89.3% | Response Time: ~18ms | Model: Random Forest\*\*



---



\## 🎯 Key Features



\- ✅ \*\*Real-time predictions\*\* (~18ms response time)

\- ✅ \*\*89.3% model accuracy\*\* (Random Forest Classifier)

\- ✅ \*\*Auto-generated API documentation\*\* (Swagger UI + ReDoc)

\- ✅ \*\*CI/CD pipeline\*\* with GitHub Actions

\- ✅ \*\*Docker containerization\*\* for consistent deployment

\- ✅ \*\*Complete SDLC documentation\*\* (SRS, Architecture, Tests, Manual)



---



\## 📁 Project Structure

bank\_marketing-ml/

├── app/ # API application

│ ├── main.py # FastAPI endpoints

│ ├── model.pkl # Trained model

│ └── columns.pkl # Model columns

├── models/ # Training module

│ └── train.py # Model training script

├── docs/ # SDLC Documentation

│ ├── 01\_SRS\_Requirements.md

│ ├── 02\_Architecture\_Design.md

│ ├── 03\_Test\_Plan.md

│ ├── 04\_User\_Manual.md

│ └── 05\_Deployment\_Guide.md

├── tests/ # Test suite

│ ├── test\_api.py

│ └── test\_performance\_simple.py

├── .github/workflows/ # CI/CD

│ └── deploy.yml

├── Dockerfile

├── requirements.txt

└── README.md



text



---



\## 🚀 Quick Start



```bash

\# Clone repository

git clone https://github.com/mcml1225/bank\_marketing-ml.git

cd bank\_marketing-ml



\# Install dependencies

pip install -r requirements.txt



\# Train model

python models/train.py



\# Run API

cd app \&\& uvicorn main:app --reload

