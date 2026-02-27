from config.config import OPENAI_API_KEY, GOOGLE_API_KEY, GROQ_API_KEY, TAVILY_API_KEY
import json

ai_response = ''' {
    "title": "Hanry potter",
    "author": "J.K. Rowling",
    "published_year": 1997
}
'''

book_data = json.loads(ai_response)
print(book_data['title'])
