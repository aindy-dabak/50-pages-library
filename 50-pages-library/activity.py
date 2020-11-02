# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 13:04:24 2020

@author: Aaron
"""
        
import numpy as np
import pandas as pd



from user_profile import Profile


class Reader_Activity(Profile):
    ''' The Person requires a user ID to be initiated'''
    
    def borrow(self,book_id):
        """
        1. Check the list of Books <Books log Table> for the book with the 'user_id'
        
        2. Change it's availability to 'not available'
           <Book_Log.csv>
        
        3. Increment the number of times that the particular book has been borrowed
           <Book_Log.csv>
           
        4. Add the num of borrows for the particular user
           <Profile.csv>
            
           
           
        5. Increment the number of pending returns for the particular user
           <Profile.csv>
        
        
        6. Increment the column for total number of books borrowed
           <Library_statistics.csv>

        Returns
        -------
        None.

        """
        
        ##-------------(1)--------------##
        ##
        #load the the book log table into a dataframe
        book_data = pd.read_csv('Book_Log.csv')
        ##
        ##--------------------------------##
        
        
        
        
        ##-------------(2)--------------##
        ##
        #locate the row for the book with that id
        #Change it's availability status to 'NO'
        book_data.loc[book_data.Book_Id == book_id,'Available'] = 'No'
        ##
        ##--------------------------------##
        

        ##-------------(3)--------------##
        ##
        #Increment the number of times that particular book has been borrowed
        book_data.loc[book_data.Book_Id == book_id,'Number_of_Times_Borrowed'] += 1
        ##
        #Save to a csv file to replace the original file
        book_data.to_csv('Book_Log.csv',index = False)
        ##
        ##--------------------------------##
        
        
        
        
 

       
        ##-------------(4)--------------##        
        ##       
        #load the user profile as a dataframe
        user_data = pd.read_csv('Profile.csv')
        ##
        #locate the row for the user on the dataframe 
        #increment the number of times borrowed for the user
        user_data.loc[user_data.User_Id == self.user_id,'Num_of_Times_Borrowed'] += 1
        ##
        ##--------------------------------##
        
        
        ##--------------(5)--------------##
        ##
        #increment the number of pending returns for that user
        user_data.loc[user_data.User_Id == self.user_id,'Pending_Returns'] += 1
        ##
        #save to a csv file to replace the original file
        user_data.to_csv('Profile.csv',index = False)
        ##
        ##--------------------------------##
        
        
        
        
        
        
        ##---------------(6)-------------##
        ##
        #load the library_data as a dataframe
        library_data = pd.read_csv('Library_statistics.csv')
        ##
        #locate and increment the total of books borrowed in the library
        library_data['Total_Num_of_Borrows'] += 1
        ##
        #save to a csv file to replace the original file
        library_data.to_csv('Library_statistics.csv', index = False)
        ##--------------------------------##
        
        
        
        
        
    
    def return_book(self,book_id):
        """
        1. Check the list of Books <Books log Table> for the book with the 'user_id'
           <Books_Log.csv>
           
        2. Change it's availbility to 'available'
           <Books_Log.csv>
           
        3. Reduce the number the number of pending returns for the user by 1
           <Profile.csv>
        
        Returns
        -------
        None.

        """
        ##----------------(1)-------------##
        ##
        #load the book log into a dataframe
        book_data = pd.read_csv('Book_Log.csv')
        ##
        ##--------------------------------##
        
        
        ##----------------(2)--------------##
        ##
        #locate the row for the book with that id
        #Change it's availability status to 'YES'        
        book_data.loc[book_data.Book_Id == book_id,'Available'] = 'Yes'
        ##
        #save to a csv file to replace the original file
        book_data.to_csv('Book_Log.csv',index = False)
        ##
        ##--------------------------------##
        
        
        ##----------------(3)---------------##
        ##
        #load the user profile as a dataframe
        user_data = pd.read_csv('Profile.csv')
        ##              
        #decrease the number of pending returns for that user
        user_data.loc[user_data.User_Id == self.user_id,'Pending_Returns'] -= 1
        ##
        #save to a csv file to replace the original file
        user_data.to_csv('Profile.csv',index = False) 
        ##
        ##--------------------------------##
        
        
        
class Library_Activity():
    def __init__(self, book_id,book_name,):
        self.__book_id = book_id
        self.__book_name = book_name
        
        
    def add_to_Books(self):
        book = [self.__book_id,self.__book_name,'Yes',0]
        book = pd.DataFrame([book], columns = ['Book_Id','Book_Name','Available','Number_of_Times_Borrowed'])
        book.to_csv('Book_Log.csv',mode = 'a',header = False,index = False)

        
        
    #def add_book():
        
    