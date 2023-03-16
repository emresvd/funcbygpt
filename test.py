import funcbygpt


@funcbygpt.funcbygpt
def hello():
    return "function that prints hello world --print"


@funcbygpt.funcbygpt
def count():
    return "function that counts to 100 --print"


@funcbygpt.funcbygpt
def bubble_sort(array):
    return f"function that sorts array {array} with bubble sort --print"


@funcbygpt.funcbygpt
def remove_char(string, c):
    return f"function that removes the {c} character from the {string} string and returns the result --return --print"


print("test hello")
hello()
print("end hello")

input()

print("test count")
count()
print("end count")

input()

print("test bubble_sort")
bubble_sort([7, 4, 1, 8, 5, 2, 0, 9, 6, 3])
print("end bubble_sort")

input()

print("test remove_char")
result = remove_char("hello world", "l")
print("result:", result)
print("end remove_char")
