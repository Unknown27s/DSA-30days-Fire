# Count_Row=int(input("Enter the Row count"))
result=[] #declear the result list 
temp_list2=[] #another temp list
num1=5 #total number of row for pascal triangle
for i in range(1,num1+1):   #Loop throught 1 to num1+1 element 
    temp_list=[] #delcear a temp list to store the temp value to append in the result at final            
    for j in range(0,i):   #Loop thorught innner element 
        if j ==0 or j+1 == i:  #if the j value is first and last element append 1
            temp_list.append(1)
        else:       # else the append value is calculated by adding the pervisous element and current element of the temp_list2
            num=temp_list2[j-1]+temp_list2[j]
            temp_list.append(num)
    result.append(temp_list)
    temp_list2=temp_list



print(result)