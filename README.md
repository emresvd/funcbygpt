# funcbygpt

tell the function what to do and gpt will write the code

## install funcbygpt
```bash
pip install funcbygpt
```

## api key
you need to get an api key from [openai](https://openai.com/)<br>
and put it in a file called `.env` in the root of the project.<br>
the file should look like this:
```bash
OPENAI_API_KEY=your_api_key
```

<br><br>

## usage

### hello world
```python
import funcbygpt

@funcbygpt.funcbygpt
def hello():
    return "function that prints hello world"

hello()
```
output:
```
Hello World!
```

<br><br>

### counter
```python
import funcbygpt

@funcbygpt.funcbygpt
def count():
    return "function that counts to 100"

count()
```
output:
```
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100
```

<br><br>

### bubble sort
```python
import funcbygpt

@funcbygpt.funcbygpt
def bubble_sort(array):
    return f"function that sorts array {array} with bubble sort"

bubble_sort([7, 4, 1, 8, 5, 2, 0, 9, 6, 3])
```
output:
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

<br><br>

### remove char
```python
import funcbygpt

@funcbygpt.funcbygpt
def remove_char(string, c):
    return f"function that removes the {c} character from the {string} string and returns the result --return"

print(remove_char("hello world", "l"))
```
output:
```
heo word
```
