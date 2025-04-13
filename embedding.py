from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

result = client.models.embed_content(
        model="gemini-embedding-exp-03-07",
        contents="Effel Tower is in Paris and is a famous landmark, it is 324 meters tall",)

print(result.embeddings)

# response = client.embeddings.create(
#     input=text,  
#     model= "text-embedding-3-small"
# )
# print(f"Response : {response.data[0].embedding}")
print(f"Response : {response.text}")