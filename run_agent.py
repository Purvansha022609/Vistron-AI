# main.py

import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from lokseva_prepper.agent import root_agent # <-- Corrected import statement

# Load API key from .env
load_dotenv()  # expects GOOGLE_ADK_API_KEY=<your_key>

# -------------------------------
# Function to read PDF text
# -------------------------------
def read_pdf_text(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    try:
        reader = PdfReader(pdf_path)
    except Exception as e:
        raise RuntimeError(f"Failed to open PDF file: {e}")
    
    text = ""
    for i, page in enumerate(reader.pages):
        try:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        except Exception as e:
            print(f"Warning: Failed to extract text from page {i}: {e}")
    
    if not text.strip():
        raise ValueError("No text could be extracted from the PDF.")
    
    return text

# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    pdf_file = "sample.pdf"  # replace with your PDF path

    try:
        pdf_text = read_pdf_text(pdf_file)
    except Exception as e:
        print(f"Error reading PDF: {e}")
        exit(1)
    
    user_prompt = f"""
Please summarize the following content for UPSC prelims and create a short study plan.
Also, generate questions, suggest resources, and revision notes.

Content:
{pdf_text}
"""

    try:
        response = root_agent.run(user_prompt) # <-- Use the correct root_agent
    except Exception as e:
        print(f"Error running agent: {e}")
        exit(1)

    print("\n--- UPSC Preparation Output ---\n")
    print(response)