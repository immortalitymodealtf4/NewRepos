def new_decor(decorated_func):
    some_text = "Here we go again(decorator text)"

    def inner_function():
        print(some_text)
        decorated_func()

    return inner_function


def hello_world():
    print("Hello world")


hello_world()
print("*"*10)
decorated = new_decor(hello_world)
decorated()


def add_five(decorated_func):
    """ decorator that add 5 to decorated function res"""
    def inner_func():
        return decorated_func() + 5

    return inner_func


@add_five
def grimme_the_loot():
    return 223


print("<3"*20)

print(grimme_the_loot())  # grimme now give 228
grimme_the_loot = add_five(grimme_the_loot)
print(grimme_the_loot())  # so this will return 228 + 5


def new_decor(decor_func):
    def inner():
        return decor_func() + "again"
    return inner


@new_decor
def here():
    return "Here we go "


print("%"*20)
print(here())
