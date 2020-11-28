# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 07:39:29 2020

@author: Aaron Dabak
"""


import numpy as np
import pandas as pd





#library_stat = pd.read_csv('Library_statistics.csv')

details = pd.read_csv('Profile.csv')

class Profile():
    """
    This class contains the data of the user
    
    """
    def __init__(self, User_Id):
        
        
        ## Determine the index of the user based on the User_Id given
        # This index will determine the user's roe oon the database.
        #This is to void having to go through the row each time to find the user data
        self.index = -1
        for i in pd.read_csv('Profile.csv').User_Id:
            self.index += 1
            if i == User_Id:
                print(self.index)
                break
        self._user_id = User_Id
        
            
            
            
        """# Capture the name that corresponds to the given 
        #index/user_id on the database
        self.name = pd.read_csv('Profile.csv').iloc[self.index].Name
        
        #Capture the Email that corresponds to the given 
        #index/user_id on the database
        self.email = pd.read_csv('Profile.csv').iloc[self.index].Email
        
        #Capture the Phone number that corresponds to the given
        #index/user_id on the database
        self.phone = pd.read_csv('Profile.csv').iloc[self.index].Phone
        
        
        #Capture the User that corresponds to the given
        #index/user_id on the database
        self.user_id = pd.read_csv('Profile.csv').iloc[self.index].User_Id
        """
        
        
        
    def get_name(self):
        '''
        1. Capture the name that corresponds to the given index/user_id on the database
           <Profile.csv>

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        return pd.read_csv('Profile.csv').iloc[self.index].Name
    
    
    
    def get_email(self):
        '''
        1. Capture the email that corresponds to the given index/user_id on the database
           <Profile.csv>
           
           
        Returns  The email of the user
        -------
        TYPE
            DESCRIPTION.

        '''
        return pd.read_csv('Profile.csv').iloc[self.index].Email
    
    
    
    def get_phone(self):
        
        '''
        1. Capture the Phone number that corresponds to the given index/user_id on the database
           <Profile.csv>
           

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        return pd.read_csv('Profile.csv').iloc[self.index].Phone
    
    def set_email(self, new_email):
        
        """
        1. Locate the user email on the profile database and change it to 
            the formal_parameter given above
           <Profile.csv>
        
        
        """
        
        
        #Extract the data before changing and saving
        #AVOID CHAINED ASSIGNMENT
        #CHAINING IS BACK TO BACK INDEXING E.G 
        #(pd.read_csv('Profile.csv').iloc[self.index]).Email
        


        
        
        '''
        #read the profile.csv into a dataframe
        data = pd.read_csv('Profile.csv')
        
        #locate the user email using his/her index and the 'Email_column' index
        #Change this user email to the new email
        data.iloc[self.index,3] = new_email
        
        #save the dataframe to replace the old file
        #'index = False' to avoid creating a new column
        data.to_csv('Profile.csv', index = False)'''
        
        
        '''The Above code works, but uses the indexes of columns
        and will thus break if the arrangement of columns is changed manually''' 
        
        
        ##----------------(1)-------------##
        ##
        #read the profile.csv into a dataframe
        data = pd.read_csv('Profile.csv')
        ##
        #locate the user email using his/her user_id on the row, and the 'Email' column
        #Change this email to the new email
        data.loc[data.User_Id == self.__user_id,'Email'] = new_email
        ##
        #save the dataframe to replace the old file
        #index = False' to avoid creating a new column
        data.to_csv('Profile.csv', index = False)
        ##
        ##--------------------------------##
        

        
    
    
    # ()098
        
    def set_phone(self, new_phone):
        
        """
        1. Locate the user phone on the profile database and change it to 
            the formal_parameter given above
           <Profile.csv>
        
        
        """
        
        ##----------------(1)-------------##
        ##
        #read the profile.csv into a dataframe
        data = pd.read_csv('Profile.csv')
        ##
        #locate the user_email using his/her user_id as the row, and the 'Phone' column
        #change this phone number to the new phone number
        data.loc[data.User_Id == self.__user_id,'Phone'] = new_phone
        ##
        #save the dataframe to replace the old file
        # use 'index = False' to avoid creating a new column
        data.to_csv('Profile.csv', index = False)
        ##
        ##--------------------------------##

        
        
        
        
        
