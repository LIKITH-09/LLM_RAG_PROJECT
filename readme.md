# LLM-Based RAG System

## Overview

This project demonstrates a Retrieval-Augmented Generation (RAG) system that fetches internet data and uses a Large Language Model (LLM) to generate contextual responses.

## Setup

1. Create a virtual environment:
```bash
python -m venv env
```

2. Activate it (Windows PowerShell):
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\env\Scripts\Activate.ps1
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

4. Add your API keys to `.env`

5. Run the backend:
```bash
cd flask_app
python app.py
```

6. In a new terminal, run the frontend:
```bash
cd streamlit_app
streamlit run app.py
```
#   L L M _ R A G _ P R O J E C T  
 