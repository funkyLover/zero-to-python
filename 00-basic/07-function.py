
def example():
    print('basic function')
    z = 3 + 9
    print(z)

example()

def sample_addition(num1, num2):
    print(num1 + num2)
    return num1 + num2

result = sample_addition(1, 2)
print(result)

# TypeError
# sample_addition(1, 2, 3)
# sample_addition(1)

def example_multi_return(num1, num2):
    return num1, num2

multi = example_multi_return(1, 2)
print(multi)

x, y = example_multi_return(1, 2)
print(x, y)

def example_default(num1, num2=5):
    return num1 + num2

result_with_default = example_default(1)
print(result_with_default)

result_without_default = example_default(1, 2)
print(result_without_default)

result_specify_default = example_default(1, num2=10)
print(result_specify_default)
