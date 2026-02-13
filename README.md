# Language Translation API

A FastAPI-based language translation service that uses state-of-the-art transformer models (NLLB and mBART) for multilingual translation.

## 🚨 IMPORTANT: First-Time Setup

**Before running this project for the first time, you MUST run the `SavingModelLocally.py` script to download and save the translation models locally.**

```bash
python SavingModelLocally.py
```

This script will:
- Download the NLLB-200 distilled 600M model from Hugging Face
- Download the mBART-large-50-many-to-many-mmt model from Hugging Face
- Save both models to the `models/` directory

⚠️ **Note:** This process may take some time depending on your internet connection as the models are several gigabytes in size.

## Features

- 🌍 Support for multiple languages using NLLB and mBART models
- 🚀 Fast and efficient FastAPI backend
- 🔄 RESTful API endpoints for translation
- 🐳 Docker support for easy deployment
- 📦 Local model storage for offline usage

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git
- Docker (optional, for containerized deployment)

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd languages_translations
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv myenv
myenv\Scripts\activate

# Linux/Mac
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Models (REQUIRED)

```bash
python SavingModelLocally.py
```

This will create the following directory structure:
```
models/
├── nllb_model/
│   ├── config.json
│   ├── generation_config.json
│   ├── model.safetensors
│   ├── tokenizer_config.json
│   └── tokenizer.json
└── facebook_mbart/
    ├── config.json
    ├── generation_config.json
    ├── model.safetensors
    ├── tokenizer_config.json
    └── tokenizer.json
```

### 5. Configure Environment Variables

Create a `.env` file in the `env/` directory with the following configuration:

```env
# Application
app_name=Language Translation API

# Model Selection
Translate_model=nllb

# Ollama Configuration (if using)
OLLAMA_API_URL=http://localhost:11434

# Model Paths
model_path_nllb=models/nllb_model
model_path_facebook=models/facebook_mbart_large_50_many_to_many_mmt
```

## Running the Application

### Option 1: Run with Python

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Option 2: Run with Docker

```bash
# Build the Docker image
docker build -t translation-api .

# Run the container
docker run -p 8000:8000 translation-api
```

### Option 3: Run with Docker Compose

```bash
docker-compose up --build
```

## API Endpoints

### 1. Root Endpoint

**GET** `/`

Returns a welcome message.

**Response:**
```json
{
  "message": "Welcome to the Language Translation API!"
}
```

### 2. Translate with mBART-50 Model

**POST** `/translate_50_mmt`

Translates text from English to Nepali using the mBART-50 model.

**Request Body:**
```json
{
  "text": "Hello, how are you?"
}
```

**Response:**
```json
{
  "source_text": "Hello, how are you?",
  "source_language": "en_XX",
  "target_language": "ne_NP",
  "translation": "नमस्ते, तपाईं कस्तो हुनुहुन्छ?"
}
```

### 3. Translate with NLLB Model

**POST** `/translate_nllb_model?text=<text>&src_lang=<src>&tgt_lang=<tgt>`

Translates text using the NLLB model with custom source and target languages.

**Query Parameters:**
- `text`: Text to translate
- `src_lang`: Source language code (e.g., "eng_Latn")
- `tgt_lang`: Target language code (e.g., "npi_Deva")

**Example:**
```
POST /translate_nllb_model?text=Hello&src_lang=eng_Latn&tgt_lang=npi_Deva
```

**Response:**
```json
{
  "translation": "नमस्ते"
}
```

## Language Codes

### mBART-50 Language Codes
Use language codes like: `en_XX`, `ne_NP`, `hi_IN`, `fr_XX`, `de_DE`, etc.

### NLLB Language Codes
Use language codes like: `eng_Latn`, `npi_Deva`, `hin_Deva`, `fra_Latn`, etc.

Refer to the official documentation for complete language code lists:
- [mBART-50 Languages](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt)
- [NLLB Languages](https://huggingface.co/facebook/nllb-200-distilled-600M)

## Project Structure

```
languages_translations/
├── main.py                 # FastAPI application entry point
├── config.py              # Configuration settings
├── SavingModelLocally.py  # Script to download models (RUN THIS FIRST!)
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── models/               # Local model storage (created after running SavingModelLocally.py)
├── src/                  # Source code
│   └── project_routes.py # API route definitions
├── schema/               # Pydantic models
│   └── model.py
└── utlis/                # Utility modules
    ├── nllb_model.py     # NLLB model handler
    ├── large_50_mmt.py   # mBART-50 model handler
    └── translate_gemma.py
```

## Troubleshooting

### Models Not Found Error
If you get an error about models not being found:
1. Ensure you have run `python SavingModelLocally.py`
2. Check that the `models/` directory exists and contains the model files
3. Verify the paths in your `.env` file match the actual model directories

### Out of Memory Error
If you encounter memory errors:
- The models are large and require sufficient RAM (at least 8GB recommended)
- Consider using the distilled NLLB model (600M) instead of larger variants
- Close other applications to free up memory

### Slow First Request
The first translation request may be slow as the models are loaded into memory. Subsequent requests will be faster.

## Dependencies

Main dependencies include:
- FastAPI - Web framework
- Uvicorn - ASGI server
- Transformers - Hugging Face transformers library
- PyTorch - Deep learning framework
- SentencePiece - Tokenization library
- Pydantic-settings - Configuration management

See [requirements.txt](requirements.txt) for the complete list.

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]

## Support

For issues and questions, please [open an issue](your-repo-issues-url) on GitHub.
