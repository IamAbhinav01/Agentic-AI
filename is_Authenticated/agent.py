from langchain_groq import ChatGroq
from config.serverConfig import Settings

llm = ChatGroq(api_key=Settings.GROQ_API_KEY,model=Settings.GROQ_MODEL,temperature=Settings.TEMPERATURE)
