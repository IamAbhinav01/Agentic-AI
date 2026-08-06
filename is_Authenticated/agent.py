from langchain_groq import ChatGroq
from config.serverConfig import Settings, server_config
from langgraph.graph import StateGraph,END
from utils.state import AuthState
from utils.nodes import validate_credentials_node,input_node,failure_node,success_node
from utils.router import router

settings = server_config()
llm = ChatGroq(api_key=settings.GROQ_API_KEY, model=settings.GROQ_MODEL, temperature=settings.TEMPERATURE)


workflow = StateGraph(AuthState)
workflow.add_node("InputNode",input_node)
workflow.add_node("ValidateCredential",validate_credentials_node)
workflow.add_node("Success",success_node)
workflow.add_node("Failure",failure_node)

