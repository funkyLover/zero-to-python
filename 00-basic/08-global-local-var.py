
x = 6

def example():
    z = 5
    print(z)
    # x += 1 # UnboundLocalError:
    global x
    print(x)
    x += 1
    print(x)

example()
