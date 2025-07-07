# @ - ensures that the code does not accidentally run before the one specified at @

import functools
# Need to specify it's a wrap otherwise the name and documentation of get_password will be overwritten

user = {
    "username": "john",
    "access_level": "guest"
}

def denied_password():
    return "You do not have access"

def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func
        else:
            return denied_password
    return secure_function

@make_secure
def get_password():
    return "1234"


print(get_password())