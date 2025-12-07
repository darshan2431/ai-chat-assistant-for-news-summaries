import re

def clean_text(text):
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def split_sentences(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    return [s.strip() for s in sentences if s.strip()]

def summarize(text, max_sentences=3):
    text = clean_text(text)
    sentences = split_sentences(text)

    if len(sentences) <= max_sentences:
        return text

    # simple sentence scoring (longer sentence = more information)
    scored = sorted(sentences, key=len, reverse=True)
    summary = scored[:max_sentences]
    summary = [s for s in sentences if s in summary]

    return " ".join(summary)

if __name__ == "__main__":
    print("Paste your article below. Press ENTER twice to summarize.\n")

    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    article = "\n".join(lines)
    result = summarize(article)
    print("\n--- SUMMARY ---\n")
    print(result)
