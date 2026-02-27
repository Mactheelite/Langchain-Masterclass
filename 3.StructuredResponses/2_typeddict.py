from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

# Schema for structured response
class Review(TypedDict):
    summary: str
    sentiment: str

# Prompt to generate structured response
prompt =  """
The hardware is great but the software feels bloated. There are too many pre-installed apps that I never use, and it slows down the device. However, the battery life is impressive and the display is stunning. Hoping for a software update to improve performance. Overall, it's a mixed experience.
"""

structured_model = model.with_structured_output(Review)

response = structured_model.invoke(prompt)

print(response) # This is the end of the code snippet for this file.


# Final output will be a structured response adhering to the Review TypedDict schema, making it easier to parse and utilize the information in downstream applications.

# Something like this will be the output:
{'sentiment': 'neutral', 'summary': 'The device has great hardware, but the software is bloated with too many pre-installed apps, slowing it down. However, the battery life and display are impressive.'}