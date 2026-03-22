def decorator(func):
    def wrapper():
        print("I am executing a funcation")
        func()
        print("I am executed this funcation")
    return wrapper
        
@decorator
def say_hi():
    print("Hi bro, how are you")

say_hi()

'''

def bjain(fuc):
    def jain():
        print("I am about the execute a function")  
        print("I have exected this function")
        fuc()
    return jain
def say_hello():
    print("Hi br o, how are you")
    print("Hi bro, how are you")


def say_bye():
    print("Hi br o, how are you")
    print("Bye bro")
    
f = bjain(say_hello)
g = bjain(say_bye)
f()
g()

h = say_bye()
'''