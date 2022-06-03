# Python in a Dataflow, Functionalist, Literate Style

## Functional Programming

## Basic

## Variable

### Python Operations on Basic Types

#### gotchas

```
2 // 3
```

0

```
2 % 3
```

2

```
try:
    2 + "2"
except Exception as e:
    print("Exception (%s): %s" % (type(e), str(e)))
```

Exception (<class 'TypeError'>): unsupported operand type(s) for +: 'int' and 'str'

#### casting

```
ord("2")
```

50

the UTF-8 code for "2" is 50

```
chr(50)
```

2

#### C-style String Formatting.

```
"pi to 4 decimals is %0.4f" % 3.14159265359
```

'pi to 4 decimals is 3.1416'

```
"Hello %s, I hope you love %s" % ("Student", "Python")
```

'Hello Student, I hope you love Python'

#### Python String Formatting

```
"pi to 4 decimals is {:0.4f}".format(3.14159265359)
```

'pi to 4 decimals is 3.1416'

```
"Hello {0}, I hope you love {1}".format("Student", "Python")
```

'Hello Student, I hope you love Python'

```
pi = 3.14159265359
f"pi to 4 decimals is {pi:0.4f}"
```

'pi to 4 decimals is 3.1416'

## Python Collections

### List

