class Library_Mangement:
    
    def __init__(self,name,listofbooks, emailid,key):
        '''This class takes input as name of person,nameof library,list of books,emailId and a access key.Object is made from the name of a person but everything else is stored on the name of library'''
        owners.append(name)
        self.Library_name=name
        self.list_of_books=listofbooks
        
        self.access_key=key
        self.borrowerdict={}
        self.emailid=emailid
    def printdetails(self, keyinput):
        if keyinput == self.access_key:
            print(f"The owner is {self}\nYour library name is {self.Library_name.capitalize()}\nThe books in your library are: {self.list_of_books}\nYour email id is: {self.emailid}\nYour access key is: {self.access_key} ")
            if bool(self.borrowerdict)==True:    
                for items in self.borrowerdict.items():
                    print(f"{items[1]} has borrowed {items[0]}")
            elif bool(self.borrowerdict)==False:
                    print("You don't have a person who has borrowed any of your books in library")
        else:
            print("please enter a valid access key")
    
    def lendbook(self):
        print("Please enter your name")
        name=input()
        print("Which book you want to borrow from the following:\n")
        for items in self.list_of_books:
            print(items.capitalize(),end=", ")
        print()
        a=input()
        try:
            self.list_of_books.remove(a.lower())
            self.borrowerdict.update({a.lower():name.lower()})
            print("Book borrowed successfully")
        except Exception as e:
            print(f"Sorry,The book is not available and is borrowed by {self.borrowerdict[a]}")
    def return_book(self):
        print("please enter your name")
        b=input()
        print("Please enter the book name")
        book_name=input()
        if book_name.lower() in list(self.borrowerdict.keys()) and b.lower() in self.borrowerdict.values():
            self.list_of_books.append(book_name)
            self.borrowerdict.pop(book_name.lower())
            print("The book has been returned successfully")
        elif book_name.lower() not in list(self.borrowerdict.keys())  :
            print("You have not borrowed any book")
    
    def addbook(self):
        print("Please enter book name")
        s=input()
        self.list_of_books.append(s.lower())
        
        print("Book added successfully")
    
                        




if __name__ == "__main__":
    owners=[]
    try:    
        while True:
            print("To create library press 0 and to view library press 1",end=" ")
            a=input()
            
            if a=="0":
                print("Please enter  unique library name",end=" ")
                name=input()
                print()
                print("Please enter the number of books in your library",end=" ")
                a=int(input())
                print()
                i=1
                listofbooks=[]
                if a==0:
                    pass
                elif a!=0:    
                    print("please enter name of a book and then press enter",end=" ")
                    while i<=a:
                        k=input()
                        listofbooks.append(k.lower())
                        i=i+1                                                       
                print("Please enter Email ID",end=" ")
                email=input()
                print()
                print("Please enter security key",end=" ")
                key=input()
                print()
                print("Processing....\n\n")
                locals()[name.lower()]=Library_Mangement(name.lower(),listofbooks,email,key)
                print("The library is created successfully")
                
            elif a=="1":  
                print(f"The libraries available are ",end=" ")
                if len(owners)==0:
                    print("There are no available libraries")
                elif len(owners)!=0:    
                    for items in owners:
                        print(items.capitalize(),end=", ")
                    print("\n")
                    print("Please choose the library name",end=" ")
                    lib=input().lower()
                    print("\n")
                    print("If you are the owner press 1 else 0")
                    z=input()
                    if z=="1":
                        print("Please enter your access key")
                        key=input()
                        locals()[lib].printdetails(key)
                    elif z=="0":
                        if bool(locals()[lib].list_of_books)==True:
                            print("The books availble are")
                            for items in locals()[lib].list_of_books:
                                print(items,end=" ")
                            print("\n")
                            print("Press 1 to borrow book,2 to donate book,3 to return book")
                            k=input()
                            if k=="1":
                                locals()[lib].lendbook()
                            elif k=="2":
                                locals()[lib].addbook()
                            elif k=="3":
                                locals()[lib].return_book()
                            else:
                                print("Please give a valid input\n\n\n")      
                        elif bool(locals()[lib].list_of_books)==False:
                            print("There are no available books")  

                        
                else:
                    print("Please give a valid input\n\n\n")
            else:
                print("Please give a valid input\n\n\n")
    except Exception as e:
        print("Please try again")            
  
