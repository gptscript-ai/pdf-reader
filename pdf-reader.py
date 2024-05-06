import os
import fitz

pdf = os.environ["FILENAME"]
doc = fitz.open(pdf)
text = ""

for page in doc:
    text+=page.get_text(flags=fitz.TEXTFLAGS_TEXT & ~fitz.TEXT_PRESERVE_LIGATURES & ~fitz.TEXT_PRESERVE_IMAGES)
print(text)
