def validate_args(func):
    def wrapper(*args, **kwargs):
        if len(args) != 1:
            return "Not enough arguments" if len(args) < 1 \
                else "Too many arguments"

        arg = args[0]
        if not isinstance(arg, int):
            return "Wrong types"
        if arg < 0:
            return "Negative argument"

        return func(*args, **kwargs)

    return wrapper


@validate_args
def my_function(n):
    return n * 2

print(my_function(6,7,8))
print(my_function())
print(my_function("таск7.1"))
print(my_function(5))
print(my_function(-28))