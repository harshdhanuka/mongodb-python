# mongodb-python
This repository describes a rather simple illustration, about creating collections in MongoDB, inserting documents in them, and calling numerous different queries to retrieve required information, but all this in executed through Python. All credits to be given to the owner.

For this project you will create a database for a virtual library and provide an interface to interact with it through a programming language in the manner that was taught to you in Module 10. It is expected that you will modify and extend the database design you created for Assignment 5 (Cassandra DB) or Assignment 6 (MongoDB). It is entirely your choice as to which of these two databases you have created that you want to use for this project.

Users can post and view comments about books they have checked out. Your database design must support this feature. This feature is in addition to all the specifications you were given for Assignments 5 and 6. The total specifications are given below.

In this assignment you will create a database for a virtual library. The books from the library can be “checked out” by Users for a fixed period of time. For this assignment let us assume that books cannot be renewed. A User may check out any number of books at a time. Since the books are eBooks, any number of Users can check out a book at the same time.
•	The library contains a collection of eBooks. Basic information about each book needs to be stored
o	Title, primary author, secondary authors (if any), date of first publication, number of pages, publisher, translator (if any)
o	For non-fiction books, a list of the key topics covered by the book needs to be stored. For works of fiction (including poems, plays, novels, collection of stories), the topic is just ‘fiction’.

•	For each book, we also need to store information about when it was checked out by which User.

•	For each User we need to store certain information
o	User id, name, phone, address, university affiliation (if any)

•	For each book and User, we need to store the comments made about the book by the User.

Insert at least 3 books, 5 users. The database must contain information about at least 5 check outs of books. Each check out must contain at least 3 comments about the book by the User who has checked out the book.


