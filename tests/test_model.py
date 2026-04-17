# tests/test_model.py
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, roc_auc_score

def test_model_accuracy():
    """Test model accuracy meets minimum threshold"""
    model = joblib.load('app/model.pkl')
    # Load test data
    from ucimlrepo import fetch_ucirepo
    bank = fetch_ucirepo(id=222)
    df = bank.data.original
    X = df.drop(columns=['y', 'duration'])
    y = df['y'].apply(lambda x: 1 if x == 'yes' else 0)
    
    # Simple test split
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    accuracy = accuracy_score(y_test, model.predict(X_test))
    assert accuracy > 0.85, f"Accuracy {accuracy} below threshold"

def test_model_roc_auc():
    """Test ROC-AUC score meets minimum threshold"""
    model = joblib.load('app/model.pkl')
    # ... similar setup
    auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    assert auc > 0.90