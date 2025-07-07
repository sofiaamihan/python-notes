# Making this dynamic
import functools

user = {
    "username": "john",
    "access_level": "guest"
}

def denied_password():
    return "You do not have access"

# This is called a decorator
def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return "You do not have access."
    return secure_function

# This has been decorated
@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "5678"


print(get_password("billing"))