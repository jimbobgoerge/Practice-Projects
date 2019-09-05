import sys
def main():
    f = open('/home/nobs-employee/Desktop/Project 1/Shopping_list.txt', 'r+')
    lines = f.read()
    string_list = lines
    regular_list= list(string_list[1:-1].replace("'","").split(","))
    #completely ignore this line, old code to be deleted later.
    #clean_text = lines.replace('[','').replace(']','').replace("'","").replace(" ","").replace(",","")
    Shoplist = regular_list

    def writetolist(arg_list):
            f = open('/home/nobs-employee/Desktop/Project 1/Shopping_list.txt', 'r+')
            f.read
            f.write(str(arg_list)) #str converts to string
            f.close()
            sys.exit()

    def currentlist():
        add = input('Would you like to add an item to your Shopping List or View your list? Add or View? ')
        
        while add.lower() == "add":
            item = input("Enter your item to the list: ")
            Shoplist.append(item)
            add = input("Want to add another Item to your list or View your list? Add or View? ")
        
        if add.lower() == "view":
            print("Here is your Shopping List.")
            for listitem in Shoplist:
                print(listitem)
            View()
        else:
            print("Unrecognised Command")
            unrecognised = currentlist()    
            
    def View():

        view = input("Would you like to add another item or exit your list: ")

        if view.lower() == "add":
            currentlist()
        if view.lower() == "exit":
            writetolist(Shoplist)
        else:
            print("Unrecognised Command")
            unrecognised = View()
    currentlist()

    






if __name__== "__main__":
    main()