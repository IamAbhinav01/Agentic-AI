from typing import TypedDict,Optional

class QAState(TypedDict):
    question : Optional[str]

    context : Optional[str]

    answer : Optional[str]


# for key,value in qa_state_example.items():
#     print(f"{key} : {value}")