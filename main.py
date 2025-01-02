import PyPDF2
from gtts import gTTS
import os

# Open a PDF file
with open('sample.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)

    # Get the total number of pages
    total_pages = len(reader.pages)
    print(f"Total pages: {total_pages}")

    # Read the content of the first page
    first_page = reader.pages[0]
    text = first_page.extract_text()
    print(text)

language="en"
myobj = gTTS(text,slow=True,lang=language)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")