example = 'Практическое задание'
print(example[0])
print(example[-1])
print(example[::-1])
print(example[::2])
a=len(example)
b = a / 2
if b % 2 != 0 :
    print(example[int(b):])
else :
    print(example[int(b - 1):])