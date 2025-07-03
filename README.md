# 🖼️ AI Image Captioning with 🎤 Voice Narration

A powerful Streamlit application that combines computer vision and natural language processing to generate intelligent captions for images, with support for multiple languages and text-to-speech functionality.

## 🌟 Features

- **Intelligent Image Captioning**: Uses BLIP (Bootstrapped Language-Image Pre-training) model to generate accurate descriptions of uploaded images
- **Grammar Enhancement**: Employs T5 paraphrase model to improve caption quality and readability
- **Multi-language Translation**: Supports translation to Telugu, Hindi, French, and Spanish using Google Translate
- **Text-to-Speech**: Converts captions to audio using Google Text-to-Speech (gTTS)
- **User-friendly Interface**: Clean, intuitive Streamlit web interface
- **GPU Acceleration**: Automatically detects and uses CUDA if available for faster processing

## 🚀 Demo

1. Upload an image (JPG, JPEG, or PNG)
2. Select your preferred language for translation
3. Get three versions of the caption:
   - Raw caption from the AI model
   - Polished caption with improved grammar
   - Translated caption in your chosen language
4. Listen to the English narration of the polished caption

## 📋 Requirements

### Python Dependencies

```
streamlit>=1.28.0
transformers>=4.21.0
torch>=1.12.0
torchvision>=0.13.0
Pillow>=9.0.0
deep-translator>=1.11.0
gtts>=2.3.0
```

### System Requirements

- Python 3.8 or higher
- At least 4GB RAM (8GB recommended for better performance)
- CUDA-compatible GPU (optional, for faster inference)
- Internet connection (required for translation and TTS services)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd image-captioning-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create requirements.txt** (if not present)
   ```bash
   pip freeze > requirements.txt
   ```

## 🎯 Usage

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Using the Interface

1. **Upload Image**: Click "Upload an image" and select a JPG, JPEG, or PNG file
2. **Choose Language**: Select your preferred language from the dropdown menu
3. **View Results**: The app will automatically process your image and display:
   - The uploaded image
   - Raw caption from the AI model
   - Polished caption with improved grammar
   - Translated caption in your selected language
   - Audio player for the English narration

## 🧠 Model Architecture

### BLIP Image Captioning Model
- **Model**: `Salesforce/blip-image-captioning-base`
- **Purpose**: Generates initial image descriptions
- **Architecture**: Vision Transformer + Language Model
- **Performance**: State-of-the-art results on image captioning benchmarks

### T5 Paraphrase Model
- **Model**: `Vamsi/T5_Paraphrase_Paws`
- **Purpose**: Improves grammar and readability of captions
- **Architecture**: Text-to-Text Transfer Transformer
- **Function**: Paraphrases text to make it more natural and grammatically correct

## 🌐 Supported Languages

| Language | Code | Translation Quality |
|----------|------|-------------------|
| Telugu   | te   | High              |
| Hindi    | hi   | High              |
| French   | fr   | High              |
| Spanish  | es   | High              |

*Note: Additional languages can be easily added by extending the `lang_map` dictionary in the code.*

## 📁 Project Structure

```
image-captioning-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── tts_audio/            # Directory for generated audio files (auto-created)
└── .gitignore           # Git ignore file
```

## ⚡ Performance Optimization

### GPU Acceleration
The application automatically detects and uses CUDA if available:
```python
device = "cuda" if torch.cuda.is_available() else "cpu"
```

### Model Caching
Uses Streamlit's `@st.cache_resource` decorator to cache models in memory, preventing repeated loading:
- Reduces startup time for subsequent runs
- Improves overall application performance

### Duplicate Word Removal
Implements intelligent duplicate word removal to clean up generated captions:
```python
seen = set()
cleaned = []
for word in caption.split():
    lw = word.lower()
    if lw not in seen:
        cleaned.append(word)
        seen.add(lw)
```

## 🔧 Configuration

### Adjusting Model Parameters

You can modify the generation parameters in the `polish_grammar` function:

```python
outputs = grammar_model.generate(
    input_ids,
    max_length=64,        # Maximum length of polished caption
    num_beams=5,          # Number of beams for beam search
    num_return_sequences=1, # Number of sequences to return
    no_repeat_ngram_size=2, # Prevent repetition
    early_stopping=True   # Stop when end token is reached
)
```

### Adding New Languages

To add support for new languages:

1. Add the language to the selectbox options
2. Update the `lang_map` dictionary with the appropriate language code
3. Ensure the language is supported by Google Translate and gTTS

## 🚨 Troubleshooting

### Common Issues

**1. CUDA Out of Memory**
```bash
RuntimeError: CUDA out of memory
```
*Solution*: Reduce batch size or use CPU by setting `device = "cpu"`

**2. Model Download Issues**
```bash
HTTPError: 404 Client Error
```
*Solution*: Check internet connection and ensure model names are correct

**3. Audio File Generation Issues**
```bash
Permission denied when creating audio files
```
*Solution*: Ensure write permissions for the `tts_audio` directory

**4. Translation API Limits**
```bash
Too many requests
```
*Solution*: Implement rate limiting or use alternative translation services

### Debug Mode

To enable debug mode, add this to the beginning of your `app.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```


## 📊 Performance Metrics

| Component | Processing Time | Memory Usage |
|-----------|----------------|--------------|
| Image Captioning | ~2-3 seconds | ~1.5GB |
| Grammar Polishing | ~1-2 seconds | ~0.8GB |
| Translation | ~0.5 seconds | ~50MB |
| TTS Generation | ~1-2 seconds | ~20MB |

*Note: Times are approximate and depend on hardware specifications*



## 🙏 Acknowledgments

- **Salesforce** for the BLIP image captioning model
- **Hugging Face** for the transformers library and model hosting
- **Google** for translation and text-to-speech services
- **Streamlit** for the amazing web application framework
- **OpenAI** for inspiration in AI application development



**Made with ❤️ using Python, Streamlit, and cutting-edge AI models**
