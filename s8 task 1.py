m =[]
final=int(input("Enter the number of elements"))
for i in range(0,final):
    element=int(input("Enter element of the list"))
    m.append(element)
for i in range(0,len(m)-1):
    for x in range(i+1,len(m)):
        if (m[i]>m[x]):
            print(False)
            print("List isnt in an accending order")
        else:
            print(True)