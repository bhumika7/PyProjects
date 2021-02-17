import pyttsx3
import PyPDF2
book = open('book.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
page = pdfReader.getPage(0)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
