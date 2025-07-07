# @ - ensures that the code does not accidentally run before the one specified at @
user = {
    "username": "john",
    "access_level": "guest"
}

def denied_password():
    return "You do not have access"

def make_secure(func):
    if user["access_level"] == "admin":
        return func
    else:
        return denied_password

@make_secure
def get_password():
    return "1234"


print(get_password())