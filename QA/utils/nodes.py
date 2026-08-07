from state import QAState
from llm import llm_client

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

def llm_node(state):
    question = state.get("question","")
    context = state.get("context",None)

    if not context:
        return {"answer" : "I don't have enough context to answer your question."}

    prompt = f"Context : {context}\n Question : {question}\n Answer the question based on the provided context."

    try:
        llm = llm_client()
        response = llm.invoke(prompt)
        return {"answer":response.content.strip()}
    except Exception as e:
        return {"answer":f"An error occured {str(e)}"}

# qa_state_example  = QAState(
#     question="what kind of work iam doing",
#     context="This project focuses on building a chatbot using Python.",
#     answer=None
# )

# print(llm_node(qa_state_example))