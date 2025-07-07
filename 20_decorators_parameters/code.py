# Making this dynamic
import functools

user = {
    "username": "john",
    "access_level": "guest"
}

# This is a factory, that makes a decorator
def make_secure(access_level):
    # This is called a decorator
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return "You do not have access."
        return secure_function
    return decorator

# This has been decorated
@make_secure("admin")
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "5678"


print(get_password("billing"))