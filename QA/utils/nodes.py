from state import QAState

def input_node(state):
    print(state)
    question = state.get("question","").strip()

    if not question:
        return {"valid":False,"error":"question cannot be empty"}

    return {"valid":True}

# qa_state_example  = QAState(
#     question="",
#     context="This project focuses on building a chatbot using Python.",
#     answer=None
# )

# print(input_node(qa_state_example))