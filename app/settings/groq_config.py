import os
from groq import Groq
from dotenv import load_dotenv


load_dotenv(verbose=True)
groq_client = Groq(
    api_key=os.environ['GROQ_API_KEY'],
)
