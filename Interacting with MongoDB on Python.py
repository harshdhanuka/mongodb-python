#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:57:10 2020

@author: harshdhanuka
"""
# %%

from pymongo import MongoClient
import pprint

# Connect MongoDB local host to Python MongoDB

client = MongoClient('mongodb://localhost:27017/')
db = client.virtual_library2


# %%


# 1. Create 'eBooks' collection
# eBooks = db.eBooks

# Create array for inserting data into the collection 'eBooks'
books_array = [
        {"Book_ID": 1, "Title":"The Alchemist", "Primary_Author":"Paulho Coelho", 
         "Secondary_Author":"NA", "Date_of_First_Publication":"2000-02-03", 
         "No_of_Pages": 100, "Publisher":"PC Publishers", "Translator":"NA", 
         "Genre_of_Book":"Fiction", "Key_Topics":"Fiction"},
        
         {"Book_ID": 2, "Title":"Modelling", "Primary_Author":"Nelson N", 
         "Secondary_Author":"Dean", "Date_of_First_Publication":"1998-09-05", 
         "No_of_Pages": 500, "Publisher":"McGraw Hill", "Translator":"NA", 
         "Genre_of_Book":"Non Fiction", "Key_Topics":"Machine Learning"},
        
        {"Book_ID": 3, "Title":"Unhappier", "Primary_Author":"Shaheen Bhatt", 
         "Secondary_Author":"Mahesh Bhatt", "Date_of_First_Publication":"1996-01-10", 
         "No_of_Pages": 150, "Publisher":"Pearson", "Translator":"Alia Bhatt", 
         "Genre_of_Book":"Non Fiction", "Key_Topics":["Life", "Biography"]}
        ]

# Insert the data array into the collection
eBooks = db.eBooks.insert_many(books_array)


# %%


# 2. Create 'user_info' collection

# Create array for inserting data into the collection 'user_info'
users_array = [
        {"User_ID": 111, "User_Name":"Harsh Dhanuka", "Phone": 986748938, 
         "Address":"21 Bleecker St", "University_Affiliation":"Columbia University"},
         
         {"User_ID": 222, "User_Name":"Harshita Thumaa", "Phone": 475809858, 
          "Address":"90 Baker St", "University_Affiliation":"Pace University"},
         
         {"User_ID": 333, "User_Name":"Umay Ayyub", "Phone": 478590987, 
          "Address":"45 5th Ave", "University_Affiliation":"Columbia University"},
         
         {"User_ID": 444, "User_Name":"Arnab Dash", "Phone": 485909821, 
          "Address":"729 7th Ave", "University_Affiliation":"Columbia University"},
         
         {"User_ID": 555, "User_Name":"Dean Christakos", "Phone": 485127568, 
          "Address":"100 42nd St", "University_Affiliation":"New York University"},
         
         {"User_ID": 666, "User_Name":"Saloni Mohan", "Phone": 398000611, 
          "Address":"210 13th St", "University_Affiliation":"Columbia University"}
         ]

# Insert the data array into the collection
user_info = db.user_info.insert_many(users_array)


# %%


# 3. Create 'checkout_info' collection

# Create array for inserting data into the collection 'checkout_info'
checkout_array = [
        {"Checkout_ID": 11111, "Book_ID": 1, "Title":"The Alchemist", 
         "Key_Topics":"Fiction", "User_ID": 444, "User_Name":"Arnab Dash", 
         "University_Affiliation":"Columbia University", "Checkout_Date":"2020-09-06",
         "Comments":["Great Novel","Highly Recommend","Best Paulo Ever"]},
        
        {"Checkout_ID": 22222, "Book_ID": 2, "Title":"Modelling", 
         "Key_Topics":"Machine Learning", "User_ID": 111, "User_Name":"Harsh Dhanuka", 
         "University_Affiliation":"Columbia University", "Checkout_Date":"2020-10-01",
         "Comments":["Perfect for beginners","very elaborate and easy","worth buy"]},
        
        {"Checkout_ID": 33333, "Book_ID": 3, "Title":"Unhappier", 
         "Key_Topics":["Life", "Biography"], "User_ID": 222, "User_Name":"Harshita Thumma", 
         "University_Affiliation":"Pace University", "Checkout_Date":"2020-08-10",
         "Comments":["perfect read","beautiful biography","best for depression"]},
        
        {"Checkout_ID": 44444, "Book_ID": 2, "Title":"Modelling", 
         "Key_Topics":"Machine Learning", "User_ID": 555, "User_Name":"Dean Christakos", 
         "University_Affiliation":"New York University", "Checkout_Date":"2020-07-22",
         "Comments":["easy explained concepts","great for data scientists","good data concepts"]},
        
        {"Checkout_ID": 55555, "Book_ID": 1, "Title":"The Alchemist", 
         "Key_Topics":"Fiction", "User_ID": 333, "User_Name":"Umay Ayyub", 
         "University_Affiliation":"Columbia University", "Checkout_Date":"2020-06-02",
         "Comments":["must read","worth every second","highly recommend this"]},
        
        {"Checkout_ID": 66666, "Book_ID": 2, "Title":"Modelling", 
         "Key_Topics":"Machine Learning", "User_ID": 666, "User_Name":"Saloni Mohan", 
         "University_Affiliation":"Columbia University", "Checkout_Date":"2020-04-11",
         "Comments":["perfect for data analysts","modelling made easy","data understanding concepts"]},
        
        {"Checkout_ID": 77777, "Book_ID": 3, "Title":"Unhappier", 
         "Key_Topics":["Life", "Biography"], "User_ID": 333, "User_Name":"Umay Ayyub", 
         "University_Affiliation":"Columbia University", "Checkout_Date":"2020-04-15",
         "Comments":["great book on self reflection","life story","suggest all to read"]},
        
        {"Checkout_ID": 88888, "Book_ID": 1, "Title":"The Alchemist", 
         "Key_Topics":"Fiction", "User_ID": 555, "User_Name":"Dean Christakos", 
         "University_Affiliation":"New York University", "Checkout_Date":"2020-03-20",
         "Comments":["paulo's best","liked it very much","king of fiction"]}
        ]

# Insert the data array into the collection
checkout_info = db.checkout_info.insert_many(checkout_array)



# %%



# Question 1: 
# Which books have been checked out since such and such date

# I have selected the date 1st August 2020 to find the books

checkout_info = db.checkout_info

titles = checkout_info.find({"Checkout_Date":{"$gte":"2020-08-01"}}, {"Title":1, "_id":0})

for title in titles:
    pprint.pprint(title)


# Alternate method:
# for book in checkout_info.distinct("Title", {"$and": [{"Checkout_Date": {"$gte": "2020-08-01"}}]}):
#    pprint.pprint(book)


# %%


# Question 2:
# Which users have checked out such and such book

title1 = checkout_info.find({"Title":"Unhappier"}, {"User_Name":1, "_id":0});
title2 = checkout_info.find({"Title":"The Alchemist"}, {"User_Name":1, "_id":0});
title3 = checkout_info.find({"Title":"Modelling"}, {"User_Name":1, "_id":0});

for names in title1:
    pprint.pprint(names)

for names in title2:
    pprint.pprint(names)
    
for names in title3:
    pprint.pprint(names)


# Alternate method:
# for names in checkout_info.distinct("User_Name", {"$and": [{"Title": "Unhappier"}]}):
#    pprint.pprint(names)


# %%


# Question 3:
# How many books does the library have on such and such topic

eBooks = db.eBooks

# Genre Wise
eBooks.count_documents({"Genre_of_Book": "Fiction"})
eBooks.count_documents({"Genre_of_Book": "Non Fiction"})

# Key Topics Wise
eBooks.count_documents({"Key_Topics": "Life"})
eBooks.count_documents({"Key_Topics": "Biography"})
eBooks.count_documents({"Key_Topics": "Fiction"})
eBooks.count_documents({"Key_Topics": "Machine Learning"})


# Alternate method:
# print(db.eBooks.count_documents({"Genre_of_Book":"Fiction"}))


# %%


# Question 4:
# Which users from Columbia University have checked out books on 
# Machine Learning between this date and that date

names = checkout_info.find({"University_Affiliation":"Columbia University", 
                       "Key_Topics":"Machine Learning", 
                       "Checkout_Date":{"$gte":"2020-06-01", 
                       "$lte":"2020-12-31"}}, {"User_Name":1, "_id":0})

for names in names:
    pprint.pprint(names)
    
    
# Alternate method:
#for names in checkout_info.distinct("User_Name", 
#                                    {"$and": [{"Key_Topics": "Machine Learning"},
#                                    {"Checkout_Date": {"$gte": "2020-06-01"}},
#                                    {"Checkout_Date": {"$lte": "2020-12-31"}},
#                                   {"University_Affiliation":"Columbia University"}]}):
#    pprint.pprint(names)


# %%


# Question 5:
# What comments have been made by any User about such and such 
# book between such and such dates, ordered from the most recent to the least recent.

# I have selected the book title 'Modelling' for this purpose.

comments = checkout_info.find({"Title":"Modelling",
                               "Checkout_Date":{"$gte":"2020-01-01", "$lte":"2020-12-31"}},
                               {"Title":1, "Comments":1, "User_Name":1, "Checkout_Date":1,"_id":0})    

for comments in comments:
    pprint.pprint(comments)
    

# Alternate method:
#for comments in checkout_info.distinct("Comments", 
#                                       {"$and": [{"Title": "Modelling"}, 
#                                       {"User_Name":"Harsh Dhanuka"},
#                                       {"checkout_time": {"$gte": "2020-08-01"}},
#                                       {"checkout_time": {"$lte": "2020-12-31"}}]}):
#    pprint.pprint(comments)


# %%


# Question 6: 
# Show for a given User, what comments they have made about such and such book.

# I have selected user 'Umay Ayyub' and book title 'The Alchemist' for this purpose.

comments = checkout_info.find({"User_Name":"Umay Ayyub",
                               "Title":"The Alchemist"},
                               {"Title":1, "Comments":1, "User_Name":1,"_id":0})    

for comments in comments:
    pprint.pprint(comments)


# Alternate method:\
#for comment in checkout_info.distinct("Comments", 
#                                      {"$and": [{"User_Name": "Umay Ayyub"},
#                                      {"Title": "The  Alchemist"}]}):
#    pprint.pprint(comment)

