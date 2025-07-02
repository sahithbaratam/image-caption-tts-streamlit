# 🖼️ Image Captioning + Grammar Polishing + Translation + TTS (Streamlit App)

This is a Streamlit web app that performs the following:

- 📷 **Image Captioning** using BLIP-1 model
- ✍️ **Grammar Polishing** using a T5-based paraphrasing model
- 🌐 **Translation** into multiple languages (Telugu, Hindi, French, Spanish)
- 🔊 **Text-to-Speech (TTS)** audio generation using gTTS

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository

2️⃣ Create virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv .venv
.\.venv\Scripts\activate      # On Windows
source .venv/bin/activate    # On Mac/Linux

3️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

4️⃣ Run the Streamlit app
bash
Copy
Edit
streamlit run app.py

📁 Folder Structure
bash
Copy
Edit
streamlitcaption/
│
├── app.py              # Main Streamlit app
├── requirements.txt    # Required Python libraries
├── tts_audio/          # (Optional) Folder for storing audio files
└── README.md           # This file

💡 Notes
Make sure you have a working internet connection (for model downloads and TTS).

If streamlit is not found, install it using pip install streamlit.

Ensure sentencepiece is installed to support T5-based models.
