import re
from collections import Counter

def clean_text(text):
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def split_sentences(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    return [s.strip() for s in sentences if s.strip()]

def build_word_freq(text):
    # very simple word frequency dictionary
    text = text.lower()
    words = re.findall(r'\w+', text)
    stopwords = {"the", "is", "and", "a", "an", "to", "of", "in", "on", "for", "this", "that", "it", "as"}
    words = [w for w in words if w not in stopwords]
    return Counter(words)

def summarize(text, max_sentences=2):
    text = clean_text(text)
    sentences = split_sentences(text)

    if len(sentences) <= max_sentences:
        return text

    word_freq = build_word_freq(text)

    # score each sentence by sum of word frequencies
    sentence_scores = {}
    for sent in sentences:
        words = re.findall(r'\w+', sent.lower())
        score = sum(word_freq.get(w, 0) for w in words)
        sentence_scores[sent] = score

    # pick top N sentences
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:max_sentences]

    # keep them in original order
    summary = [s for s in sentences if s in top_sentences]
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
