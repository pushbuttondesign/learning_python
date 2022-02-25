#python shallow vs deep copy

stack = [1,2,3]
not_stack = []
print(not_stack)
not_stack.append(stack[:])
print(not_stack)
stack.pop()
print(not_stack)
