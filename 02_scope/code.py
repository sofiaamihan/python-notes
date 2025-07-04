a = 1
b = 10

def func():
    global a
    print(a)
    a = 2
    print(a)

func()
print(a)

for i in range(5):
    b += 1
    print(b)

print(b)