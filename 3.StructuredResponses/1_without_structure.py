from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

# Prompt to generate structured response
prompt =  """
The hardware is great but the software feels bloated. There are too many pre-installed apps that I never use, and it slows down the device. However, the battery life is impressive and the display is stunning. Hoping for a software update to improve performance. Overall, it's a mixed experience.
"""

response = model.invoke(prompt)

print(response.content) # This is the end of the code snippet for this file.


# Final output will be a unstructured response, which may be difficult to parse and utilize in downstream applications. The output will likely be a free-form text summary of the review, without any specific structure or format.