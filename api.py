from flask import Flask, request, jsonify
import joblib
from preprocessing import preprocess  # Asegúrate que preprocessing.py esté en el mismo directorio

# Crear la app
app = Flask(__name__)

# Cargar modelo y vectorizador (deben estar en el mismo directorio que este script)
try:
    modelo = joblib.load("modelo_svm_fake_news.pkl")
    vectorizador = joblib.load("vectorizador_tfidf.pkl")
except FileNotFoundError:
    raise Exception("❌ Archivos del modelo no encontrados. Asegúrate de que estén en la misma carpeta.")

# Ruta principal
@app.route("/")
def home():
    return "API para detección de noticias falsas. Usa /predict con método POST."

# Ruta para predicción
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "Se necesita una clave 'text' en el JSON"}), 400

    texto = data['text']
    try:
        procesado = preprocess(texto)
        vector = vectorizador.transform([procesado])
        prediccion = modelo.predict(vector)[0]
        resultado = "Fake News" if prediccion == 0 else "Real News"
        return jsonify({"resultado": resultado})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ejecutar la app
if __name__ == "__main__":
    app.run(debug=True)
