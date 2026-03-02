# summarise_news.py

import json
from datetime import datetime
import google.generativeai as genai
from config import NEWS_STORAGE_FILE, GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Choose model
model = genai.GenerativeModel("gemini-2.5-flash")  

def load_articles():
    with open(NEWS_STORAGE_FILE, "r") as f:
        return json.load(f)

def create_prompt(articles):
    content = "\n\n".join(
        [
            f"Title: {a['title']}\nSummary: {a['summary']}\nSource: {a['source']}"
            for a in articles
        ]
    )

    prompt = f"""
    You are a global news analyst.

    Given the news below, summarize the news into:

    1. Top Global News
    2. Top India News
    3. Business & Economy
    4. Technology
    5. Geopolitics
    6. Sports News
    7. Other Trending topics

    Rules:
    - Provide bullet points per section
    - Mention links in summary as well.
    - Keep concise but informative.
    - Avoid repeating similar news.
    - If there are multiple news on related topic, summarize them together.

    News:
    {content}
    """

    return prompt

def generate_report():
    articles = load_articles()
    prompt = create_prompt(articles)

    response = model.generate_content(prompt)

    return response.text

if __name__ == "__main__":
    report = generate_report()

    with open("final_report.txt", "w") as f:
        f.write(f"📰 Daily News Summary – {datetime.now().strftime('%d %B %Y')}\n\n")
        f.write(report)