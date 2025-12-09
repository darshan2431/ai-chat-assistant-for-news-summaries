"""
AI Chat Assistant for News Summaries

Usage:
    python main.py
"""

import re
from collections import Counter


# ---------- Text Processing Helpers ----------

def clean_text(text: str) -> str:
    """Normalize whitespace and remove extra line breaks."""
    text = text.replace("\r", " ").replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_sentences(text: str):
    """Split text into sentences using simple punctuation rules."""
    sentences = re.split(r'(?<=[.!?]) +', text)
    return [s.strip() for s in sentences if s.strip()]


def build_word_freq(text: str) -> Counter:
    """Build a word frequency dictionary ignoring common stopwords."""
    text = text.lower()
    words = re.findall(r"\w+", text)

    stopwords = {
        "the", "is", "and", "a", "an", "to", "of", "in", "on", "for", "this",
        "that", "it", "as", "at", "by", "from", "with", "be", "are", "was",
        "were", "or", "has", "have", "had", "will", "would", "can", "could"
    }

    filtered = [w for w in words if w not in stopwords]
    return Counter(filtered)


# ---------- Summarization ----------

def summarize(text: str, max_sentences: int = 3) -> str:
    """
    Simple extractive summarization:
    1. Build word frequency map
    2. Score each sentence by sum of word frequencies
    3. Pick top N sentences in original order
    """
    cleaned = clean_text(text)
    sentences = split_sentences(cleaned)

    if not sentences:
        return ""

    if len(sentences) <= max_sentences:
        return cleaned

    word_freq = build_word_freq(cleaned)

    sentence_scores = {}
    for sent in sentences:
        words = re.findall(r"\w+", sent.lower())
        score = sum(word_freq.get(w, 0) for w in words)
        sentence_scores[sent] = score

    # Top N sentences by score
    top_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )[:max_sentences]

    # Keep original order
    summary = [s for s in sentences if s in top_sentences]
    return " ".join(summary)


# ---------- Simple Q&A over the article ----------

def answer_question(question: str, sentences):
    """
    Very basic Q&A:
    - Extract keywords from question
    - Return the sentence that contains most of those keywords
    This is NOT real QA, just a helpful heuristic.
    """
    q_words = re.findall(r"\w+", question.lower())
    # Remove common filler words
    stopwords = {"what", "when", "where", "who", "why", "how", "is", "was",
                 "the", "a", "an", "in", "of", "for", "to", "do", "does"}
    keywords = [w for w in q_words if w not in stopwords]

    if not keywords:
        return "I'm not sure how to answer that. Try asking more specifically."

    best_sent = None
    best_score = 0

    for sent in sentences:
        s_words = set(re.findall(r"\w+", sent.lower()))
        score = sum(1 for k in keywords if k in s_words)
        if score > best_score:
            best_score = score
            best_sent = sent

    if best_score == 0 or best_sent is None:
        return "I couldn't find anything related to that question in the article."

    return best_sent


# ---------- CLI Interface ----------

def read_article_from_input() -> str:
    print("Paste your news article below.")
    print("When you are done, press ENTER on an empty line.\n")

    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break

        if line.strip() == "":
            # empty line = end of article
            break
        lines.append(line)

    return "\n".join(lines)


def main():
    # 1) Read article
    article = read_article_from_input()
    if not article.strip():
        print("No article text provided. Exiting.")
        return

    # 2) Summarize
    summary = summarize(article, max_sentences=3)
    print("\n--- SUMMARY ---\n")
    print(summary)
    print("\n----------------\n")

    # 3) Simple chat loop for Q&A
    sentences = split_sentences(clean_text(article))
    print("You can now ask questions about this article.")
    print("Type 'exit' to quit.\n")

    while True:
        q = input("Your question: ").strip()
        if q.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        if not q:
            continue

        answer = answer_question(q, sentences)
        print("Answer:", answer, "\n")


if __name__ == "__main__":
    main()
