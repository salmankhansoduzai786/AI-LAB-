import re

samples = [
    "AI, search!",
    "I can't log in.",
    "help@example.com",
    "CS4944 late!",
    "",
    "یہ ایک مثال ہے",
]

for text in samples:
    ws = text.split()
    words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    print("Original :", repr(text))
    print("Whitespace:", ws, len(ws))
    print("Word-like :", words, len(words))
    print("-" * 60)

assert re.findall(r"\b\w+\b", "") == []

try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2",
                                device="cpu")
    for text in samples[:2]:
        print(text, model.tokenizer.tokenize(text))
except ImportError:
    print("Model tokenizer skipped: sentence-transformers is not installed.")