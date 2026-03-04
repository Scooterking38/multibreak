# multibreak

`multibreak` lets you break out of multiple nested loops in Python easily.

### Example

```python
from multibreak import break_

for i in range(3):
    for j in range(3):
        if j == 1:
            break_(2)  # exits both loops
        print(i, j)
```

Works with any number of nested loops!
