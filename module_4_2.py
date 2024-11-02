test_= "Nothing see"

def test_function(test):
    print(test)
    #global test_
    def inner_function(test_):
        #test_= 3
        print(test_)
    inner_function("Я в области видимости функции test_function")

    return test
    inner_function("Nothing see")
b = test_function("Это  объемлющую область видимости")
test_= "Nothing see"










