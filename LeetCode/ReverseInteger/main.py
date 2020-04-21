

data = 123
beta = str(data)
array = [];
for c in beta:
    array.append(c);

i = 0
j = len(array) - 1
while i < len(array):
    if i >= j:
        break
    if array[i] == '-':
        i += 1;
    array[i] , array[j] = array[j], array[i]
    i += 1;
    j -= 1;


result = '';
i = 0;
while i < len(array):
    result += str(array[i])
    i += 1;
result = int(result)
if result > (2**32)/2 - 1 or result < -(2**32)/2:
    result = 0

print(result)