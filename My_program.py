"""
example program from Code In Place Lesson on how to use VS Code program as Python IDE and then publish to GitHub
"""
MAX_NUMBER=50
def even_number():
    for i in range(MAX_NUMBER):
        if i % 2 == 0:
            print(i)
even_number()

def odd_number():
    for i in range(MAX_NUMBER):
        if i % 2 == 1:
            print(i)
odd_number()
