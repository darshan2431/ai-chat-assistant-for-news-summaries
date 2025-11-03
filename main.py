# AI Chat Assistant for News Summaries - Prototype
# Created by Darshan N

def summarize(text):
    # Simple placeholder summary logic
    words = text.split()
    return " ".join(words[:20]) + "..."

print("📰 AI Chat Assistant for News Summaries")
sample_text = "OpenAI has announced new AI models that improve efficiency and understanding."
print("Summary:", summarize(sample_text))
print("Chatbot Response: This article discusses advancements in AI models by OpenAI.")
