import os
import re

path = os.path.join("english", "class8", "sci-ch6-pressure-winds-storms-and-cyclones.html")
if not os.path.exists(path):
    print("File does not exist!")
    exit(1)

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

size_bytes = os.path.getsize(path)
size_kb = size_bytes / 1024

print("=" * 60)
print(f"VERIFICATION REPORT: {path}")
print(f"File Size: {size_bytes:,} bytes ({size_kb:.2f} KB)")
print("=" * 60)

print("Size >= 150KB:", size_kb >= 150.0)
print("Doctype:", text.startswith("<!DOCTYPE html>"))
print("Closing html:", text.strip().endswith("</html>"))

for i in range(1, 7):
    print(f"sec{i}:", f'id="sec{i}"' in text, f"section-{i}:", f'id="section-{i}"' in text)

print("SVGs:", text.count("<svg"))
print("ans-box:", text.count('class="ans-box"'))
print("quiz-card:", text.count('class="quiz-card"'))

odia = re.findall(r'[\u0B00-\u0B7F]', text)
print("Odia characters:", len(odia))

latex = re.findall(r'(?<!\\)\$[^\$]+\$', text)
print("Raw LaTeX dollars:", len(latex))

latex_bs = re.findall(r'\\[a-zA-Z]{2,}', text)
print("Raw LaTeX backslashes:", len(latex_bs))

print("speechSynthesis:", "speechSynthesis" in text)
print("reading-progress-bar:", "reading-progress-bar" in text)
