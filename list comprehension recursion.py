'''
#recursion
def factorial(n):
    if n <= 1:
        return 1
    else:
        print('{}*{}={}'.format(n, n-1, n*(n-1)))
        return n * factorial(n-1)

print(factorial(3))

#nested list comprehension
nest = [[1,2],[3,4],[4,5]]
flat = [child for parent in nest for child in parent]
print(flat)
'''
#n level recursion
ends = [10, 11]
start = 60
blocks = [[10,20],[20,30],[30,40],[40,50],[40,60],[11,21],[21,60]]
#10 blocks 20, 20 blocks 30, 30 blocks 40...

children = {}
for p, c in blocks:
    children.setdefault(p, []).append(c)
print(blocks)
print(children)

def all_children(end):
    if end not in children:
        return set()
    return set(children[end] + [b for a in children[end] for b in all_children(a)])

print(all_children(10))
print({p: all_children(p) for p in ends})

'''
OUTPUT
[[10, 20], [20, 30], [30, 40], [40, 50], [40, 60], [11, 21], [21, 60]]
{10: [20], 20: [30], 30: [40], 40: [50, 60], 11: [21], 21: [60]}
{40, 50, 20, 60, 30}
{10: {40, 50, 20, 60, 30}, 11: {60, 21}}
'''
