# 🏦 Bank Marketing Prediction API

[![Simple Test](https://github.com/mcml1225/bank_marketing-ml/actions/workflows/simple-test.yml/badge.svg)](https://github.com/mcml1225/bank_marketing-ml/actions/workflows/simple-test.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/mcml1225/bank_marketing-ml)
[![GitHub last commit](https://img.shields.io/github/last-commit/mcml1225/bank_marketing-ml.svg)](https://github.com/mcml1225/bank_marketing-ml)

## 📊 Overview

Machine Learning API that predicts whether a bank customer will subscribe to a term deposit. Built with **FastAPI**, **scikit-learn**, and **Docker**.

**Accuracy: 89.3% | Response Time: ~18ms | Model: Random Forest**

---

## 🎯 Key Features

- ✅ **Real-time predictions** (~18ms response time)
- ✅ **89.3% model accuracy** (Random Forest Classifier)
- ✅ **Auto-generated API documentation** (Swagger UI + ReDoc)
- ✅ **CI/CD pipeline** with GitHub Actions
- ✅ **Docker containerization** for consistent deployment

---

## 🚀 Quick Start

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