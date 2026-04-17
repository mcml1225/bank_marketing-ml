from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib  # ← IMPORTANTE: es "joblib", no "jobib"
import pandas as pd
import os

# Inicializar app
app = FastAPI(title="Bank Marketing Prediction API")

# Cargar el modelo y las columnas
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
columns_path = os.path.join(os.path.dirname(__file__), 'columns.pkl')

# model
model = joblib.load(model_path)
train_columns = joblib.load(columns_path)

# Definir la forma de los datos de entrada
class ClientData(BaseModel):
    age: int
    job: str
    marital: str
    education: str
    default: str
    balance: float
    housing: str
    loan: str
    contact: str
    day: int
    month: str
    campaign: int
    pdays: int
    previous: int
    poutcome: str

@app.get("/")
def read_root():
    return {"message": "Bank Marketing Prediction API", "status": "online"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
def predict(client: ClientData):
    try:
        # Convertir a DataFrame
        input_df = pd.DataFrame([client.dict()])
        input_encoded = pd.get_dummies(input_df)
        
        # Asegurar las mismas columnas
        input_final = input_encoded.reindex(columns=train_columns, fill_value=0)
        
        # Predicción
        prediction = model.predict(input_final)[0]
        probability = model.predict_proba(input_final)[0][1]
        
        return {
            "subscription": "Yes" if prediction == 1 else "No",
            "probability": round(probability, 3)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))