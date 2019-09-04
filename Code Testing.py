def main():
    Shoplist=[]

    add = input('Would you like to add an atem to your Shopping List? Y or N?')

    while add.lower() == "y":
        item = input("Enter your item to the list:")
        Shoplist.append(item)
        add = input("Want to add another Item to your list? Y or N?")
        
    
    print("Here is your Shopping List.")
    for listitem in Shoplist:
        print(listitem)


    f = open('/home/nobs-employee/Desktop/Project 1/Shopping_list.txt', 'w+')
    f.write(str(Shoplist)) #str converts to string
    f.close()





if __name__== "__main__":
    main()