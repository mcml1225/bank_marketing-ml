import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from ucimlrepo import fetch_ucirepo 
import os

# 1. Descargar datos
print("Descargando datos...")
bank_marketing = fetch_ucirepo(id=222) 
df = bank_marketing.data.original 

# 2. Preprocesamiento
print("Preprocesando datos...")
X = df.drop(columns=['y', 'duration'])
y = df['y'].apply(lambda x: 1 if x == 'yes' else 0)

# Convertir variables categóricas a numéricas
X = pd.get_dummies(X, drop_first=True)

# 3. Entrenar modelo
print("Entrenando modelo...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print(f"Precisión del modelo: {model.score(X_test, y_test)}")

# 4. Crear la carpeta app si no existe
os.makedirs('app', exist_ok=True)

# 5. Guardar el modelo y las columnas
joblib.dump(model, 'app/model.pkl')
joblib.dump(X_train.columns.tolist(), 'app/columns.pkl')

print("✅ Modelo guardado en app/model.pkl")
print("✅ Columnas guardadas en app/columns.pkl")