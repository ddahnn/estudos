def test_soma():
    assert sum([1,4,5]) == 10

def positive(num):
    return num > 0



def test_is_positive():
    assert positive(5) is True
    assert positive(-1) is False