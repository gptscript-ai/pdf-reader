import os
import fitz

pdf = os.environ["FILENAME"]
doc = fitz.open(pdf)
text = ""
for page in doc:
    text+=page.get_text()
print(text)
