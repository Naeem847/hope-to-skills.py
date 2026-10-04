from pypdf import PdfReader
from typing import List
def extract_text_from_pdf(pdf_path: str)-> str:
    """
    Extracts all text content from a PDF file.
    
    Args:
        pdf_path (str): The path to the PDF file.
    
    Returns:
        str: The extracted text from the PDF file.
    """
    try:
        reader = PdfReader(pdf_path)
        full_text = []
        for page in reader.pages:
            text=page.extract_text()
            if text:
                full_text.append(text)
        return "\n".join(full_text)
    except FileNotFoundError:
        print(f"File not found at {pdf_path}")
        return ""
    except Exception as e:
        print(f"Error occurred while extracting text from PDF: {str(e)}")
        return ""