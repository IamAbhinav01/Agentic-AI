from langchain_groq import ChatGroq
from config.serverConfig import Settings
from langgraph.graph import StateGraph,END
from utils.state import AuthState
from utils.nodes import validate_credentials_node,input_node,failure_node,success_node
from utils.router import router

llm = ChatGroq(api_key=Settings.GROQ_API_KEY,model=Settings.GROQ_MODEL,temperature=Settings.TEMPERATURE)


