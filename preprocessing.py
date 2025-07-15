# preprocessing.py

import re
import spacy

# ✅ Cargar modelo de lenguaje de spaCy (asegúrate de tener 'en_core_web_sm' instalado)
nlp = spacy.load("en_core_web_sm")

# ✅ Stopwords mínimas personalizadas
basic_stopwords = set("""
i me my myself we our ours ourselves you your yours yourself yourselves he him his himself
she her hers herself it its itself they them their theirs themselves what which who whom
this that these those am is are was were be been being have has had having do does did doing
a an the and but if or because as until while of at by for with about against between into
through during before after above below to from up down in out on off over under again
further then once here there when where why how all any both each few more most other some
such no nor not only own same so than too very can will just don should now
""".split())

# ✅ Limpieza básica de texto
def clean_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# ✅ Lematización y eliminación de stopwords
def lemmatize_text(text):
    doc = nlp(text)
    return " ".join([
        token.lemma_ for token in doc
        if token.is_alpha and token.lemma_ not in basic_stopwords and not token.is_stop
    ])

# ✅ Pipeline completo
def preprocess(text):
    cleaned = clean_text(text)
    lemmatized = lemmatize_text(cleaned)
    return lemmatized
