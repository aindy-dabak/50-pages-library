"""
This module contains the resources for getting the data of a new reader
And generatimg a new ID for the user...
It also modifies the 'LIBRARY_STATISTICS' Table,to change the values of 
Number of Registered users..




------------------------------------------------------------------------------


It makes use of the year of registraion and the serial number for that year..
__For Example:
    
    The fourth user to register in  the year '2021' will get a  user_Id of
    "21/0004"
    
    The one-hundreth user to register in the year 2025 will get a user_ID of
    "25/0100"


"""
import numpy as np
import pandas as pd
import datetime






#Load The Library statistics Table to obtain the values of registered users
library_stat = pd.read_csv('Library_statistics.csv')

#v = New_Reg(Name,Email,Phone)
#()

class New_Reg():
    
    '''
      collect and store the user personal data
      
      
      Also manipulate Data concerning New Users
      
      

    '''
    def __init__(self,Name, Email, Phone):

        self.name = Name
        self.phone = Phone
        self.email = Email



        
        
        
        
    def create_id(self, **kwargs):
        """
        

        Parameters
        ----------
        **kwargs : TYPE
            DESCRIPTION.

        Returns
        -------
        A newly generated User_ID for a newly registered reader

        """
        
        serial_num = int(library_stat['Num_of_Reg_Users']) + 1
        
        """
        Find a way to make the serial numbers reset after a year ends
        
        """
        
        #Obtain the current year
        year = datetime.date.today().year
        #Convert to list for easy manipulation
        year_list = list(str(year)) 
        #Delete first two values of year
        #The last two are to be used in the USER_ID
        del year_list[2:]
        #Join these last two into a string
        year_value = ''
        year_value = year_value.join(year_list)
        
        
        
        #Get a serial number for the USER
        user_num = str(serial_num).zfill(4)
        
        
        #Create a user Id by concatenating  the 
        #1 Year value
        #2 a '/'
        #3 User serial number 
        #4 This ID is a string.
        user_id =  year_value+'/'+user_num
        
    
        

        
        
        return(user_id)

    
    def add_to_database(self):
        """
        1. add the new user details to the <Profile> database>
           <Profile.csv>
          
        2. Increase the total number of registered readers at the library
           <Library_statistics.csv>
        

        Returns
        -------
        None.

        """
        
        ##----------------(1)-------------##
        ##
        #Add the user details to a list
        user_df = [New_Reg.create_id(self),self.name,self.phone,self.email,0,0]
        ##
        #Create a dataframe  with the user details---use [user_df]
        #in a list to let pandas know that there are 'rows'
        user_df = pd.DataFrame([user_df],columns = ['User_Id','Name','Phone','Email','Num_of_Times_Borrowed','Pending_Returns'])
        ##
        #Save this dataframe to a csv file in append mode 'a'
        #Index = False to avoid creating a new column
        #header = False to creating a new header 
        user_df.to_csv('Profile.csv',mode = 'a',index = False,header = False)
        ##
        ##--------------------------------##
        
        
        
        
        ##----------------(2)-------------##
        ##
        #Increment the number of registered users on the library statistics database
        library_stat['Num_of_Reg_Users'] += 1
        library_stat.to_csv('Library_statistics.csv', index = False)#"index = False to prevent creating a new column
        ##
        ##--------------------------------##
        
        



    

        
    
