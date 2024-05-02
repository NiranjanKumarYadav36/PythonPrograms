## SyntaxError
# Occurs when the Python parser encounters a syntax error, such as a missing colon or parentheses python

if True
    print("Hello, World!")
           
# SyntaxError: expected ':'


## IndentationError:
# Occurs when there is incorrect indentation in your code, typically in the context of loops, functions, or conditional statements.
for i in range(5):
print(i)

# IndentationError: expected an indented block after 'for' statement on line 11


# type error:
# Occurs when an operation or function is applied to an object of inappropriate type.

text = "HEllo" + 5
# TypeError: can only concatenate str (not "int") to str

## index error
# Occurs when you try to access an index that is out of range for a sequence (e.g., list, tuple, string).

my_list = [1, 2, 3]
print(my_list[5])
# IndexError: list index out of range