from langgraph.graph import StateGraph,END
from utils.state import QAState
from utils.nodes import input_node,context_provider_node,llm_node

workflow = StateGraph(QAState)

workflow.add_node("InputNode",input_node)
workflow.add_node("ContextNode",context_provider_node)
workflow.add_node("QANode",llm_node)

workflow.set_entry_point("InputNode")
workflow.add_edge("InputNode","ContextNode")
workflow.add_edge("ContextNode","QANode")
workflow.add_edge("QANode",END)

app = workflow.compile()
ans = app.invoke({"question":"What is LangGraph?"})
print(ans)