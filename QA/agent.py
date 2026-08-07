from langgraph.graph import StateGraph
from utils.state import QAState
from utils.nodes import input_node,context_provider_node,llm_node

workflow = StateGraph(QAState)

workflow.add_node("InputNode",input_node)
workflow.add_node("ContextNode",context_provider_node)
workflow.add_node("QANode",llm_node)

