def add(*args):
    result = 0
    for num in args:
      result += num
    return result

dev = add(5,4,6,7,4,3,2,3)
print(dev)