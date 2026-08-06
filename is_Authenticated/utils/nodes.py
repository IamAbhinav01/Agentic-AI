from .state import AuthState

def input_node(state):
    print(state)

    if state.get('user_name','') == '':
        username = input('what is your username')

    password = input('Enter your Password')

    if state.get('user_name','') == '':
        return {"user_name": username, "password": password}
    else:
        return {"password": password}


def validate_credentials_node(state):

    username = state.get('user_name','')
    password = state.get('password','')

    print("Username : ",username," Password : ",password)

    if username == "iamAbhinav01" and password == "HeHEHE":
        is_Authenticated = True
    else:
        is_Authenticated = False

    return {"is_Authenticated": is_Authenticated}


def success_node(state):
    username = state.get("user_name","")
    return {"output":f"Authentication Successful , Hi {username}"}

def failure_node(state):
    username = state.get("user_name","")
    return {"output":f"Authentication failed , try Again {username} 😑"}

auth__state1 :AuthState = {
    "user_name" : "iamAbhinav01",
    "password"  : "HeHEHE",
    "is_Authenticated" : True,
    "output" : "Login Successful"
}

auth__state2 :AuthState = {
    "user_name" : "iamNotAbhinav01",
    "password"  : "HaHaHaHa",
    "is_Authenticated" : False,
    "output" : "Login Failed"
}

# print(validate_credentials_node(auth__state1))
# print(validate_credentials_node(auth__state2))