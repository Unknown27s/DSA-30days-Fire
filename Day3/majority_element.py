num=[1,4,3,1,4,1]
n=5
temp=[]
result=[]
temp_1=[]
for i in num:
    num1=num.count(i)
    temp.append(num1)
    temp_1.append(i)

for i in range(0,len(num)-1):
    if temp[i] > n//3 :
        if temp_1[i] not in result:
            result.append(temp_1[i])
        else:
            continue


#Another method to find the majority element in the list
# freq = {}

# for x in num:
#     freq[x] = freq.get(x, 0) + 1

# result = []

# for key, count in freq.items():
#     if count > n // 3:
#         result.append(key)

print(result)