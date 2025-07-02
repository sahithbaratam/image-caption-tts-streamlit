# app.py
import streamlit as st
st.set_page_config(page_title="Image Captioning + TTS", layout="centered")
import uuid
import os

from transformers import BlipProcessor, BlipForConditionalGeneration
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM  # ✅ This is required
from deep_translator import GoogleTranslator
from gtts import gTTS
from PIL import Image
import torch


# Load models
device = "cuda" if torch.cuda.is_available() else "cpu"

@st.cache_resource
def load_blip():
    processor = BlipProcessor.from_pretrained('Salesforce/blip-image-captioning-base')
    model = BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-base')
    return processor, model

@st.cache_resource
def load_polish_model():
    tokenizer = AutoTokenizer.from_pretrained("Vamsi/T5_Paraphrase_Paws")
    model = AutoModelForSeq2SeqLM.from_pretrained("Vamsi/T5_Paraphrase_Paws").to(device)
    return tokenizer, model

processor, model = load_blip()
grammar_tokenizer, grammar_model = load_polish_model()


# Caption generator
def generate_caption(image):
    inputs = processor(images=image, return_tensors="pt").to(device)
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)

    seen = set()
    cleaned = []
    for word in caption.split():
        lw = word.lower()
        if lw not in seen:
            cleaned.append(word)
            seen.add(lw)
    return " ".join(cleaned)


# Grammar polish
def polish_grammar(text):
    input_text = f"paraphrase: {text} </s>"
    input_ids = grammar_tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True).to(device)
    outputs = grammar_model.generate(
        input_ids,
        max_length=64,
        num_beams=5,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        early_stopping=True
    )
    return grammar_tokenizer.decode(outputs[0], skip_special_tokens=True)

# Translator
def translate_caption_google(text, target_lang="te"):
    return GoogleTranslator(source='auto', target=target_lang).translate(text)

# Text-to-Speech
def generate_tts(text, lang="en"):
    filename = f"{uuid.uuid4().hex}.mp3"
    path = os.path.join("tts_audio", filename)
    os.makedirs("tts_audio", exist_ok=True)
    tts = gTTS(text=text, lang=lang)
    tts.save(path)
    return path

# Streamlit UI
st.set_page_config(page_title="Image Captioning + TTS", layout="centered")
st.title("🖼️ AI Image Captioning with 🎤 Voice Narration")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
language = st.selectbox("Choose a language for translation", ["Telugu", "Hindi", "French", "Spanish"])

lang_map = {
    "Telugu": "te",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es"
}

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Generating caption..."):
        caption = generate_caption(image)
        polished = polish_grammar(caption)
        translated = translate_caption_google(polished, target_lang=lang_map[language])
        audio_path = generate_tts(polished)

    st.subheader("Raw Caption")
    st.write(caption)

    st.subheader("Polished Caption")
    st.write(polished)

    st.subheader(f"Translated Caption ({language})")
    st.write(translated)

    st.subheader("🎧 Voice Narration (English)")
    st.audio(audio_path)
