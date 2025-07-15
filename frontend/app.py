import streamlit as st
import datetime
import sys
import os
from dotenv import load_dotenv
from fpdf import FPDF  # 📄 For PDF export
import tempfile

# 🖌️ Custom CSS Styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(-45deg, #1e3c72, #2a5298, #f3ec78, #af4261);
        background-size: 400% 400%;
        animation: gradientBG 20s ease infinite;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .stMarkdown, .stTextInput, .stSelectbox, .stTextArea, .stButton, .stRadio {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 5px;
    }

    textarea, .stTextArea textarea {
        color: white !important;
        background-color: #2f2f2f !important;
        font-size: 16px;
    }

    .black-label {
        color: black !important;
        font-weight: 600;
    }

    section[data-testid="stSidebar"] label, 
    section[data-testid="stSidebar"] span {
        color: black !important;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# 🌐 Load environment variables
load_dotenv()

# 🧠 Import model functions
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "models")))
from compose_email import compose_email_with_transformer
from reply_email import reply_email_with_transformer
from gemini_email import compose_email_with_gemini, reply_email_with_gemini

# 📄 Page config
st.set_page_config(page_title="PolyMail AI", page_icon="📬")

# 🚀 Title
st.markdown('<span style="color: black; font-size: 2.25rem; font-weight: 700;">📬 PolyMail AI Assistant</span>', unsafe_allow_html=True)

# 🛠️ Sidebar
st.sidebar.header("📌 Settings")
model_choice = st.sidebar.selectbox("Select Model", ["EmailAssistant", "FLAN-T5 (Google)"])
task = st.sidebar.radio("Task", ["✍️ Compose Email", "📨 Reply to Email"])

# 🔤 Optional language (API only)
target_language = "English"
if model_choice == "EmailAssistant":
    target_language = st.sidebar.selectbox("Select Language", ["English", "Hindi", "Telugu", "Tamil", "Spanish", "French"])

# 📝 Main Input
st.markdown('<h4 class="black-label">💬 Input</h4>', unsafe_allow_html=True)
st.markdown('<span class="black-label">Enter your situation or paste the email here</span>', unsafe_allow_html=True)
user_input = st.text_area(" ")

# 🎯 Generate
if st.button("Generate"):
    if not user_input.strip():
        st.warning("Please enter some input.")
    else:
        with st.spinner("🧠 Generating your email..."):
            if model_choice == "FLAN-T5 (Google)":
                full_output = compose_email_with_transformer(user_input.strip()) if task == "✍️ Compose Email" else reply_email_with_transformer(user_input.strip())
            else:
                full_output = compose_email_with_gemini(user_input.strip(), target_language) if task == "✍️ Compose Email" else reply_email_with_gemini(user_input.strip(), target_language)

        st.markdown('<h4 class="black-label">📧 AI-Generated Email:</h4>', unsafe_allow_html=True)
        st.text_area("Generated Email", value=full_output, height=300, max_chars=None)

        # 🖨️ Download as PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in full_output.splitlines():
            pdf.multi_cell(0, 10, line)

        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        pdf.output(tmp_file.name)

        with open(tmp_file.name, "rb") as f:
            st.download_button(
                label="📥 Download as PDF",
                data=f,
                file_name="Generated_Email.pdf",
                mime="application/pdf"
            )
