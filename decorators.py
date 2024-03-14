# def function1():
#     print('Subscribe my channel')

# func2 = function1
# del function1
# func2()


def decorator1(func1):
    def nowExe():
        print('Executing now')
        func1()
        print('Executed!')
    return nowExe

@decorator1
def hello():
    print(f"Hi I am Aninda")

hello()
# hello = decorator1(hello)
# hello()