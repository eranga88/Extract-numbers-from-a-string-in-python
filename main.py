input = input("Please Enter string : ")

temp=[]
numlist = []
listA = []
listB = []


temp = input.split(' ')

for x in temp:

    try:
        num = int(x)
        numlist.append(num)
        if num %2 == 0:
            listB.append(num)
        else:
            listA.append(num)
    except ValueError:

        temp_str=""

        for str_num in  x:
            try:
                u = int(str_num)
                temp_str="".join((temp_str,str_num))
            except ValueError:
                pass

        for n in temp_str.split():
            if n.isdigit():
                y = int(n)
                numlist.append(y)
                if y%2==0:
                    listB.append(y)
                else:
                    listA.append(y)

print(numlist)
print("listA : ",listA)
print("listB : ",listB)

