Este proyecto utiliza un modelo SVM entrenado con TF-IDF para detectar si una noticia es real o falsa. Está desplegado como aplicación web usando Streamlit.

## ✨ Probar la app

[![Ver en Hugging Face](https://img.shields.io/badge/HuggingFace-App-orange?logo=streamlit)](https://huggingface.co/spaces/tuusuario/Detector_Fake_News)

## 📂 Estructura del proyecto

- `Streamlit_app.py`: interfaz web con Streamlit
- `Modelo_svm_fake_news.pkl`: modelo entrenado
- `Vectorizador_tfidf.pkl`: vectorizador
- `requirements.txt`: dependencias


# 🧠 Fake News Detector - Clasificador de Noticias Falsas
---
title: detector-noticias-falsas
emoji: 🕵️‍♂️
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: "1.29.0"
app_file: streamlit_app.py
pinned: false
---

Este proyecto de Machine Learning detecta si una noticia es **falsa o verdadera** a partir de su texto (título y contenido). Utiliza procesamiento de lenguaje natural (NLP) y un modelo SVM entrenado sobre un dataset real.

---

## 🧰 Tecnologías usadas

- Python 3.10+
- Pandas
- Scikit-learn
- spaCy
- TQDM
- Flask (para API)
- Google Colab (para entrenamiento)
- Visual Studio Code (para desarrollo)
- Git & GitHub

---

## 📦 Estructura del proyecto
fake-news-detection/
├── Streamlit_app.py             # Script principal de la API Flask
├── preprocessing.py             # Funciones de limpieza y lematización del texto
├── modelo_svm_fake_news.pkl     # Modelo SVM entrenado y guardado
├── vectorizador_tfidf.pkl       # Vectorizador TF-IDF entrenado
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Documentación principal del repositorio
├── .gitignore                   # Archivos/carpetas ignoradas por Git
└── data/
    ├── news_dataset_unificado.csv  # Dataset ya preprocesado (opcional)
# 🚀 Demo rápida en Google Colab

Haz clic en el botón para abrir el notebook en Google Colab y ejecutar el proyecto paso a paso:

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/Inavsanler/fake-news-detector.git)

---

## 📦 Requisitos del entorno

Asegúrate de tener instalado Python 3.8+ y los siguientes paquetes:

```bash
pip install -r requirements.txt

# Detector de Noticias Falsas


