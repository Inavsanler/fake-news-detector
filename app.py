import streamlit as st
import joblib
import re
import spacy

# Cargar modelo de lenguaje de spaCy (asegúrate de tener 'en_core_web_sm' en requirements.txt)
nlp = spacy.load("en_core_web_sm")

# Cargar modelo y vectorizador
modelo = joblib.load("modelo_svm_fake_news.pkl")
vectorizador = joblib.load("vectorizador_tfidf.pkl")

# Stopwords básicas
basic_stopwords = set("""
i me my myself we our ours ourselves you your yours yourself yourselves he him his himself
she her hers herself it its itself they them their theirs themselves what which who whom
this that these those am is are was were be been being have has had having do does did doing
a an the and but if or because as until while of at by for with about against between into
through during before after above below to from up down in out on off over under again
further then once here there when where why how all any both each few more most other some
such no nor not only own same so than too very can will just don should now
""".split())

# Funciones de limpieza
def clean_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def lemmatize_text(text):
    doc = nlp(text)
    return " ".join([
        token.lemma_ for token in doc
        if token.is_alpha and token.lemma_ not in basic_stopwords and not token.is_stop
    ])

def preprocess(text):
    cleaned = clean_text(text)
    lemmatized = lemmatize_text(cleaned)
    return lemmatized

# 🖼️ Interfaz Streamlit
st.set_page_config(page_title="Detector de Fake News", page_icon="📰")
st.title("📰 Fake News Detector")
st.markdown("Introduce el texto de una noticia para verificar si es **falsa** o **real**.")

user_input = st.text_area("📝 Escribe tu noticia aquí")

if st.button("🔍 Analizar"):
    if user_input.strip() == "":
        st.warning("Por favor, escribe un texto primero.")
    else:
        texto_preprocesado = preprocess(user_input)
        vector = vectorizador.transform([texto_preprocesado])
        prediccion = modelo.predict(vector)[0]
        resultado = "🟥 Fake News" if prediccion == 0 else "🟩 Real News"
        st.success(f"Resultado: {resultado}")
