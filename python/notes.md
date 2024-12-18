### Read a File
``` python
f = open("demofile.txt", "r")
print(f.read())
```

### Range
range(5) -> 0, 1, 2, 3, 4
range(3,6) -> 3, 4, 5
range(0, 10, 2) -> 0, 2, 4, 6, 8

### convert string to list
list = list(str)

### Altering objects by reference
String, ints, chars, etc are immutable and can't be passed by reference, but objects like lists or maps are mutable and can be. However, if you re-assign an object entirely within the function, it effectively creates a new instance of that object and "breaks" the link with the original variable outside the function.

To re-assign a list, you must update it in place:
```
curr_pos[0], curr_pos[1] = new_pos
```

### Remove newline in a string
```
str = str.strip()
```

### Print concatenated list of strings from a list
```
''.join(arr)
```