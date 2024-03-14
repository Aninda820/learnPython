# def function_name_print(a, b, c, d):
#     print(a, b, c, d)

# function_name_print("Aninda", 'Naruto', 'Itachi', 'Madara')



def funargs(normal, *args, **kwargs):
    print(normal)
    # print(type(args))
    # print(args)
    for item in args:
        print(item)

    for key, value in kwargs.items():
        print(key, value)

har = ['Harry', 'Naruto', 'Krishna', 'Siva', 'Ram']
normal = "This is a normal"
kw = {
    'Ram': 'Programmer',
    'Rohim': 'Fitness Trainer',
    'Krishna': 'Monitor'
}
funargs(normal, *har, **kw)



# Another one
def tup(*args):
    for item in args:
        print(f"hi {item}")
def names():
    tup('Harry', 'Naruto', 'Krishna', 'Siva', 'Ram')

names()



# Another Example
def greet(*users):
    for user in users:
        print(f"Walcome {user}")

def main():
    greet('Feet', 'Harry', 'Tom')

if __name__ == '__main__':
    main()