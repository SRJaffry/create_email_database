
from find_email import *

'''Start of Program to extract the email IDs'''
fhandle = open('mbox-short.txt')

email_list = list()
line_cnt = 0
for line in fhandle:
    line_cnt=line_cnt+1
    line.rstrip()
    email_found = find_email(line)
    
    if(email_found[0] == -1):
        continue;
    else:
        email_list.append(email_found[1])        
        #print('line {}, :{}'.format(line_cnt, email_found[1]))
    

#print('Total email addresses  = {}'.format(len(email_list)))

# Writing the email addresses to the file now
f= open("email_database.txt", 'w')

for email in email_list:    
    f.write(email+'\n')
f.close()
