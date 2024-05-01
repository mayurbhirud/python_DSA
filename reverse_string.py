# reverse string prblem basic approach
def reverseString(strings):
    return strings[::-1]
strings = 'hello'
print(reverseString(strings))
## so time complexity is O(n) because it visit each character at once 

# solve using loop and concatenation
def reverseString(strings):
    reversed_str = " "
    for ch in strings:
        reversed_str = ch + reversed_str
    return reversed_str
print(reverseString(strings))

# loop with list
def reverseString(strings):
    reversed_list = []
    for char in strings:
        reversed_list.insert(0, char)
    return ''.join(reversed_list)
print(reverseString(strings))

def reverseString(strings):
    string = strings
    r_str= ""
    for ch in string:
        r_str = ch + r_str
    return r_str
strings= 'hello'
print(reverseString(strings))
 
strings="12345"
s= ""
for ch in strings:
    
    s = ch + s
s = int(s)
print(s)

