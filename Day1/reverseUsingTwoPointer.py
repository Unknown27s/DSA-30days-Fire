#using two pointer to reverse a list element
input_values=["d","f","g","h","j","k"]
left=0
right=len(input_values)-1
while left < right:
    input_values[left],input_values[right]=input_values[right],input_values[left]
    left=left+1
    right=right-1
print(input_values)