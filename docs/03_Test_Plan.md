# Test Plan
## Bank Marketing Prediction API

### 1. Testing Strategy

#### 1.1 Test Types

| Type | Tool | Coverage |
|------|------|----------|
| Unit Tests | pytest | Individual endpoints |
| Integration Tests | pytest + requests | API + Model |
| Model Validation | sklearn.metrics | Model accuracy |
| Performance | locust | Response time |
| CI/CD | GitHub Actions | Automation |

### 2. Test Cases

#### 2.1 API Tests

```python
# tests/test_api.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    """Test GET / endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_health_check():
    """Test GET /health endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_prediction_valid():
    """Test POST /predict with valid data"""
    valid_client = {
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
    }
    response = client.post("/predict", json=valid_client)
    assert response.status_code == 200
    assert "subscription" in response.json()
    assert "probability" in response.json()

def test_prediction_invalid():
    """Test POST /predict with invalid data"""
    invalid_data = {"age": 30}  # Missing required fields
    response = client.post("/predict", json=invalid_data)
    assert response.status_code == 400