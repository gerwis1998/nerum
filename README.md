# Nerum
Nerum is a library for automatically generating command line interfaces (CLIs) from python classes.

## Example

```python
from nerum import Nerum

class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

if __name__ == '__main__':
    Nerum(Calculator)
```

```
> python calculator.py add 5, 8
13
```
```
> python calculator.py add a=5, b=15
20
```
