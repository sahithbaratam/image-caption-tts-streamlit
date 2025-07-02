# 🖼️ Image Captioning + Grammar Polishing + Translation + TTS (Streamlit App)

This is a **Streamlit web app** that performs:

- 📷 **Image Captioning** using the BLIP-1 model  
- ✍️ **Grammar Polishing** using a T5-based paraphrasing model  
- 🌐 **Translation** into multiple languages (Telugu, Hindi, French, Spanish)  
- 🔊 **Text-to-Speech (TTS)** audio generation using gTTS  

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository

bash
git clone https://github.com/sahithbaratam/image-caption-tts-streamlit.git
cd image-caption-tts-streamlit

2️⃣ Create a virtual environment (optional but recommended)

For Windows:

python -m venv .venv

.venv\Scripts\activate


For Mac/Linux:

python3 -m venv .venv

source .venv/bin/activate

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Run the Streamlit app

streamlit run app.py

📁 Folder Structure

streamlitcaption/
├── app.py              # Main Streamlit app
├── requirements.txt    # Required Python libraries
├── tts_audio/          # (Optional) Folder for storing audio files
└── README.md           # This file

💡 Notes

A working internet connection is required for:

Downloading models the first time

Using gTTS (Google TTS API)

If Streamlit is not found:

pip install streamlit

If T5 tokenizer errors occur, ensure sentencepiece is installed:

pip install sentencepiece

🌍 Optional: Deployed Demo

You can also check out the deployed version on Hugging Face Spaces:

🔗 https://huggingface.co/spaces/sahithbaratam/image-caption-tts

🙌 Acknowledgements

BLIP-1 Image Captioning

Vamsi/T5_Paraphrase_Paws

Google Text-to-Speech (gTTS)

Deep Translator

Streamlit
