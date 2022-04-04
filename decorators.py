# function which takes as input another function
def respond_to_mailman(func):
    def wrapper(*arg, **kwargs):  # define a new fnc
        print("A mailman is coming")
        response = func(*arg, **kwargs)  # excecute the input fnct
        return response

    return wrapper


# input fnct within the wrapper
def response_to_approacher(name, approaching):
    def inner_response(func):  # pass the function
        def wrapper(*args, **kwargs):
            if approaching is True:
                print(f"A {name} is coming")
            else:
                print(f"A {name} is leaving")
            response = func(*args, **kwargs)
            return response

        return wrapper

    return inner_response  # Notice the function name without the ()




@respond_to_mailman
def bark():
    print("woof")


def cat_response():
    print("miao")

def print_hallo(func):
    def wrapper(*args, **kwargs):
        print('hello')
        return func(*args, **kwargs)
    return wrapper

@respond_to_mailman #calling the respond fnct with make_sound as input
def make_sound(sound):
    print(sound * 2)


@response_to_approacher("husband", False)
@print_hallo
def return_sound(sound):
    return sound * 2  # now we have return instead of print


# response= respond_to_mailman(bark)
# not passing the function bark(), but call it
# response()

bark()

make_sound("woof")

return_value=return_sound("hey")
print("return value of the fnct: ", return_value)