## Gyukutai

Because bad things come with weeb names

### Installation

```bash
$ pip install gyukutai
```

Or install the development version:

```bash
$ pip install git+https://github.com/SunDwarf/gyukutai.git
```

### Usage

Use `gyukutai.apply()` to hurt the interpreter.

```py
# apply
print("Squares of the first 10 integers:", range(1, 11).apply | (lambda x: x ** 2))

# find
print("First square number:", range(2, 100).find | (lambda x: sqrt(x) % 1 == 0))

# filter
print("Factors of 234:", range(0, 234).filter | (lambda x: x != 0 and 234 % x == 0))
```
