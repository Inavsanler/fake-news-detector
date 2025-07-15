---
title: Fake News Detector
emoji: 📰
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.46.1
app_file: app.py
pinned: false
license: mit
---

# 📰 Fake News Detector

Este proyecto usa un modelo SVM entrenado para detectar si una noticia es **falsa** o **real**, utilizando procesamiento de lenguaje natural (spaCy) y una interfaz construida con Streamlit.

## 🚀 Cómo funciona

1. Introduce el texto de una noticia en el cuadro de texto.
2. Haz clic en **Analizar**.
3. El modelo devolverá si se trata de una noticia falsa (🟥) o real (🟩).

## 🧠 Tecnologías utilizadas

- `scikit-learn` para el modelo SVM
- `spaCy` para limpieza y lematización de texto
- `Streamlit` como interfaz gráfica
- `joblib` para cargar el modelo
