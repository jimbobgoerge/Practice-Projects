import sys
def main():
    Shoplist=[]

    def writetolist(arg_list):
            f = open('/home/nobs-employee/Desktop/Project 1/Shopping_list.txt', 'w+')
            f.write(str(arg_list)) #str converts to string
            f.close()
            sys.exit()
    def list():
        add = input('Would you like to add an item to your Shopping List or View your list? Add or View?')
        
        while add.lower() == "add":
            item = input("Enter your item to the list: ")
            Shoplist.append(item)
            add = input("Want to add another Item to your list or View your list? Add or View?")
        
        if add.lower() == "view":
            print("Here is your Shopping List.")
            for listitem in Shoplist:
                print(listitem)
            View()


    def View():

        view = input("Would you like to add another item or exit your list: ")

        if view.lower() == "add":
            list()
        if view.lower() == "exit":
            writetolist(Shoplist)
        else:
            print("Unrecognised Command")
            return
    list()

    






if __name__== "__main__":
    main()