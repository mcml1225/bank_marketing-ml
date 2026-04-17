# Architecture Design Document
## Bank Marketing Prediction API

### 1. High-Level Architecture
┌─────────────────────────────────────────────────────────────┐
│ Client / System │
└─────────────────────────┬───────────────────────────────────┘
│ HTTP
▼
┌─────────────────────────────────────────────────────────────┐
│ API Gateway (FastAPI) │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────────────┐ │
│ │ GET / │ │ GET /health │ │ POST /predict │ │
│ └─────────────┘ └─────────────┘ └──────────┬──────────┘ │
└─────────────────────────────────────────────────┼───────────┘
│
▼
┌─────────────────────────┐
│ Random Forest Model │
│ (joblib serialized) │
└─────────────────────────┘

text

### 2. System Components

#### 2.1 API Layer (app/main.py)
- **Framework**: FastAPI
- **Port**: 8000
- **Endpoints**:
  - `GET /`: Service status
  - `GET /health`: Health check
  - `POST /predict`: Main prediction endpoint
  - `GET /docs`: Interactive documentation

#### 2.2 ML Model (models/train.py)
- **Algorithm**: Random Forest Classifier
- **Hyperparameters**:
  - n_estimators: 50
  - max_depth: 10
  - random_state: 42
- **Accuracy**: 89.3%

#### 2.3 Data Pipeline
UCI Data → Preprocessing → One-Hot Encoding → Training → Model

text

### 3. Deployment Architecture
┌─────────────────────────────────────────────────────────────┐
│ GitHub Actions │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ Build → Test → Docker → Deploy │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│ Docker Container │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ Python 3.9-slim + Dependencies + API │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘

text

### 4. Data Flow Diagram
Input (JSON) → Pydantic Validation → DataFrame →
One-Hot Encoding → Reindexing → Model → Prediction (JSON)

text

### 5. Technology Stack

| Component | Technology | Version |
|-----------|------------|---------|
| API Framework | FastAPI | 0.104+ |
| ML Library | scikit-learn | 1.3+ |
| Serialization | joblib | 1.3+ |
| Container | Docker | 20.10+ |
| CI/CD | GitHub Actions | - |
| Data Source | UCI ML Repository | - |
| Version Control | Git | 2.40+ |

### 6. Design Decisions

| Decision | Justification |
|----------|---------------|
| FastAPI vs Flask | Auto-documentation, async support |
| Random Forest vs Neural Network | Better interpretability, less data needed |
| joblib vs pickle | Optimized for numpy/scikit-learn arrays |
| Docker vs venv | Portability, production consistency |

### 7. Sequence Diagram
User → API → Validator → Model → Response
│ │ │ │ │
│ │ │ │ └─ Return JSON
│ │ │ └─ Predict
│ │ └─ Validate input
│ └─ Process request
└─ Send request