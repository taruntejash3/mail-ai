# 📬 PolyMail AI - Smart Email Assistant

PolyMail AI is a dynamic and elegant web application that generates professional emails and smart replies using state-of-the-art language models. Built with Streamlit, it supports both **Google FLAN-T5** (transformer-based) and **Gemini API (EmailAssistant)** models to offer flexibility and high-quality results.

---

##  Features

 -->Compose and Reply to Emails  
 -->Choose between Transformer (FLAN-T5) or Gemini (EmailAssistant)  
 -->Multi-language support for EmailAssistant  
 -->Clean, animated UI with dark-mode input field  
 -->Download the generated email as a PDF  
 -->Simple deployment with Streamlit  

---

##  Models Used

### 1. **FLAN-T5 (Google)**
- Uses `google/flan-t5-large` from HuggingFace Transformers
- Runs locally via `pipeline("text2text-generation")`
- Best for quick, consistent email composition and replies

### 2. **EmailAssistant (Gemini API)**
- Uses Google's **Gemini 2.0 Flash** via REST API
- Language options: English, Hindi, Telugu, Tamil, Spanish, French
- Ideal for real-time, multi-lingual smart responses

---

## Project Structure

```bash
polymail-ai/
│
├── frontend/
│   └── app.py                  # Streamlit frontend with model selector
│
├── models/
│   ├── compose_email.py        # Transformer-based email composer
│   ├── reply_email.py          # Transformer-based reply handler
│   └── gemini_email.py         # Gemini API email composer and replier
│
├── .env                        # API keys and environment vars (excluded from Git)
├── requirements.txt            # All dependencies
└── README.md                   # You are here!
 ``` 
## ⚙️ **Setup Instructions**

### Step 1: Clone the Repository
git clone https://github.com/your-username/polymail-ai.git
cd polymail-ai


### Step 2: Create a Virtual Environment
bash

python -m venv venv
venv\Scripts\activate  # For Windows
##### source venv/bin/activate  ##### For Mac/Linux


### Step 3: Install Dependencies
bash

pip install -r requirements.txt




### STEP-4:
### 🔐 Environment Variable (.env)

This project uses an `.env` file to load the Gemini API key.

 ## **Important:**  
The `.env` file included in this repository **does not contain the actual API key**.  
For security reasons, the key is shared separately in the submitted document.

If you're running this locally, create a `.env` file in the project root like this:

GEMINI_API_KEY=your_api_key_here



### STEP-5:
### Running the App ###
bash

cd frontend
streamlit run app.py

 ### Then open your browser and go to: http://localhost:8501



## 🛡️ Disclaimer
This project is intended for educational/demo purposes. Please avoid sharing sensitive data with public APIs.
