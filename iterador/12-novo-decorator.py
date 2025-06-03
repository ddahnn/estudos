from decorator import my_deco, upper_deco, split_str



@my_deco
def my_function():
    print("função")


my_function()

@upper_deco
def text():
    return "Hello world"

print(text())


@split_str
@upper_deco
def texto():
    return "Hello world"

print(texto())