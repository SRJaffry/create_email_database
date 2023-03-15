
# The function to extract email IDs is in the file find_email.py
# The file "find_email.py" should be in the same folder as this file
from find_email import *

# Start of Program to extract the email IDs

# Start by reading the file. The file mbox-short.txt should be in the same folder
fhandle = open('mbox-short.txt')

# create an empty list of email addresses
email_list = list()

# This for loop will run till the end of the line. 
for line in fhandle:
    # This is used to strip the \n at the end of each line. 
    # (I think this may not be needed for this particular code, but it is a good practice to use it always.)
    line.rstrip()
    
    # Call the function find_email()). We have imported this function above as : from find_email import *
    # This function is present in the file of the same name find_email.py
    # This function returns a list of two elements. 
    # First element shows if the email is found (return > 0) or not (return -1), 
    # Second element is the email address if first-element is not -1, else second element is empty. 
    email_found = find_email(line)
    
    # If not email address found
    if(email_found[0] == -1):
        continue;
    # else, if email address is found append it to the list.
    else:
        email_list.append(email_found[1])                
    

# Writing the email addresses to the file now
f = open("email_database.txt", 'w')

for email in email_list:    
    f.write(email+'\n')
f.close()
