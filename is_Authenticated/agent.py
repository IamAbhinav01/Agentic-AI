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

workflow.add_edge("InputNode","ValidateCredential")
workflow.add_edge("Success",END)
workflow.add_edge("Failure","InputNode")

workflow.add_conditional_edges("ValidateCredential",router,{"success_node":"Success","failure_node":"Failure"})

workflow.set_entry_point("InputNode")

app = workflow.compile()

inputs = {"user_name":"iamAbhinav01"}
result = app.invoke(inputs)
print(result)