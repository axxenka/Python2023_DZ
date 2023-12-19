import inspect

def type_chec (func):
    def wrapper(*args, **kwargs):
        func_signature = inspect.get_annotations(func)
        received_signature = inspect.get_annotations(func)
        if received_signature != func_signature:
            raise TypeError
        print(func(*args, **kwargs))
    return wrapper
@type_chec
def val_func(name: str, passw: str) -> bool:
    return f" {name} with {passw} do"

val_func(name = "jik", passw = "17")
