
---

### **Document 4: `docs/04_User_Manual.md`**

```markdown
# User Manual
## Bank Marketing Prediction API

### 1. Introduction

This API predicts whether a bank customer will accept a term deposit offer based on their profile and campaign interaction data.

### 2. Quick Start

#### Prerequisites
- Python 3.9+
- Git
- 2GB RAM minimum

#### Installation
```bash
# Clone repository
git clone https://github.com/mcml1225/bank_marketing-ml.git
cd bank_marketing-ml

# Install dependencies
pip install -r requirements.txt

# Train model
python models/train.py

# Run API
cd app
uvicorn main:app --reload