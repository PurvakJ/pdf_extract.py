import pdfplumber
import pyttsx3

def speak(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 180)  # Speed of speech

    # Use the engine to speak the provided text
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page_number in range(20, 194 + 1):
            page = pdf.pages[page_number - 1]  # Adjusting for 0-based indexing
            text += page.extract_text()
    return text

def read_text(text):
    print(text)

# Replace 'your_file.pdf' with the path to your PDF file
pdf_path = 'D:/downloads/The-Guide-PDF.pdf'

# Extract text from the PDF file
extracted_text = extract_text_from_pdf(pdf_path)

# Read and print the extracted text
read_text(extracted_text)
speak(extracted_text)
