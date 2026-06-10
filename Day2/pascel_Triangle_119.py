def Rowfind(rownum):
    rownum-=1
    result=[]
    pre=1
    result.append(pre)
    for i in range(1,rownum+1):
        curr = (pre*(rownum - i + 1))//i
        result.append(curr)
        pre= curr
    return result


print(Rowfind(5))

