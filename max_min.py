# brute force approach to finding maximum and minimum elements
arr = [14,25,89,25,11,55,69,89,14,67,23,15]

min = arr[0]
max = arr[0]

for num in arr:
    if num < min:
        min= num
    elif num > max:
        max = num

print(min)
print(max)

##changes

