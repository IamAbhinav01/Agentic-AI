from typing import TypedDict,Optional


class AuthState(TypedDict):
    user_name:Optional[str]
    password : Optional[str]
    is_Authenticated : Optional[bool]
    output:Optional[str]


# auth__state1 :AuthState = {
#     "user_name" : "iamAbhinav01",
#     "password"  : "HeheHehe",
#     "is_Authenticated" : True,
#     "output" : "Login Successful"
# }

# auth__state2 :AuthState = {
#     "user_name" : "iamNotAbhinav01",
#     "password"  : "HaHaHaHa",
#     "is_Authenticated" : False,
#     "output" : "Login Failed"
# }

# print(f'auth_state_1 : {auth__state1}')
# print(f'auth_state_2 : {auth__state2}')