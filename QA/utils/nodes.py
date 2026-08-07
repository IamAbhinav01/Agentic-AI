from state import QAState

def input_node(state):
    print(state)
    question = state.get("question","").strip()

    if not question:
        return {"valid":False,"error":"question cannot be empty"}

    return {"valid":True}


def context_provider_node(state):
    question = state.get("question","").lower()

    if "langgraph" in question or "guided project" in question:
        context = (
            "This guided project is about using LangGraph, a Python library to design state-based workflows. "
            "LangGraph simplifies building complex applications by connecting modular nodes with conditional edges."
        )
        return {"context":context}
    
    return {"context":None}



# qa_state_example  = QAState(
#     question="",
#     context="This project focuses on building a chatbot using Python.",
#     answer=None
# )

# print(input_node(qa_state_example))