import datetime
import os



class Lms:
    def __init__(self,list_of_book,library_name):
        self.list_of_book= "library_managment_system/list_of_book.txt"
        self.library_name=library_name
        self.books_dict ={}
        with open (self.list_of_book) as bk:
            content = bk.readlines()
            
            Id =101
            for line in content :
              self.books_dict.update({str(Id) :{"book_title":line.replace("\n" ,"") , "status":"Avaliable"}})
              Id+=1

    def display_books(self):
        print ("__________________List Of Book_______________")
        print ("Book ID" ,"\t\t", "Title" )
        print ("_____________________________________________")
        for key , value in self.books_dict.items() :
            print (key ,"\t\t", value.get("book_title") , "\t\t" ,value.get("status"))




l=Lms("library_managment_system/list_of_book.txt","library_managment_system")
print(l.display_books())
