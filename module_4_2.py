
#inner_function("Я в области видимости функции test_function")
def test_function(test):
    print(test)

    def inner_function(test_):

        print(test_)
    inner_function("Я в области видимости функции test_function")

    return test


b = test_function("Это  объемлющую область видимости")
#test_= "Nothing see"
#inner_function("Я в области видимости функции test_function")









