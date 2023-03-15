# Function to find email addresses per line
def find_email(line):
    
    # Find the @ symbol since it is a necessity for email address syntax.
    # variable find_at stores the location of @ symbol, if any.
    # If there is no @ symbol in the string, the value of -1 is returned. 
    find_at = line.find('@')
    
    # If there is no @ symbol in the line, it means there is no email address.
    # Hence, exit the function without any email address.
    if find_at == -1:
        return [find_at, '']
    
    # If @ symbols is found, then email address ends (most probably) with the emtpy space.
    # Hence, here we are finding an empty space after the @ symbol.
    end_of_email = line.find(' ', find_at)
    email_id = line[:end_of_email]   
    
    # In email symtax, the domain (e.g. .org, .com, .xe etc.) appears to the right of the @ symbol
    # checking the domain now.
    # We check domain by finding a '.' (dot) symbol after the @ symbol.
    
    find_at = email_id.find('@') 
    domain_name_check = email_id.find('.', find_at)
    
    # Return the function without any email ID if the domain name not found
    # domain name is determined with a '.' (dot) symbol after @ symbol.
    if domain_name_check == -1:
        return [domain_name_check, '']
    
    # Now that all the checks are done, extract the actual email ID
    while True:
        
        start_of_email = email_id.find(' ')
                
        if start_of_email == -1:            
            break
        
        email_id = email_id[start_of_email+1:]
    
    return [find_at, email_id]