def my_deco(function):
    def wrapper():
        print("antes de executar a função")
        function()
        print("depois de executar a função")
    return wrapper

def upper_deco(function):
    def wrapper():
        func = function()
        makeUppercase = func.upper()
        return makeUppercase
    return wrapper

def split_str(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper
