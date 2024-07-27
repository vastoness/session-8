oldBread = int(input("How many old bread do you want"))
freshBread = int(input("How many fresh bread do u want"))
def payment(oldBread,freshBread):
    freshCoast=3.49*freshBread
    oldCoast=((3.49*oldBread)*0.06)
    totalCoast=(freshCoast)+(oldCoast)
    print("fresh cost :")
    print(freshCoast)
    print("old coast :")
    print(oldCoast)
    print("total cost:")
    print(totalCoast)

payment(oldBread,freshBread)