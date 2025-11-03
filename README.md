# AI Chat Assistant for News Summaries 📰
A conversational chatbot that summarizes and answers queries about news articles using Natural Language Processing (NLP).

## Overview
This project demonstrates text summarization and context retrieval using simple NLP pipelines.  
The chatbot extracts news content from online sources, generates concise summaries, and allows users to ask questions about the articles.

## Features
- Fetches latest news articles from URLs or RSS feeds  
- Performs text summarization using transformer-based models  
- Answers simple queries about summarized content  
- Clean command-line interface for quick testing  

## Tech Stack
- **Language:** Python  
- **Libraries:** Transformers, BeautifulSoup, NLTK, FAISS  
- **Tools:** Jupyter Notebook, VS Code  

## How It Works
1. User provides a news article link or keyword.  
2. System scrapes the content and summarizes it.  
3. Chatbot responds to follow-up questions contextually.

## Future Enhancements
- Integrate with a simple web UI.  
- Improve summarization accuracy using fine-tuned models.  
- Add voice input/output features for accessibility.
