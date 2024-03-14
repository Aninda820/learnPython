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