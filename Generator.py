def new_generator(new_str):
    for char in range(len(new_str)):
        yield new_str[char]


for char in new_generator("Hello world"):
    print(char)
