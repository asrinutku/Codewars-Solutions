def increment_string(string):
    
    a = string.rstrip('0123456789')
    b = string[len(a):]
    
    if b == "": 
      return string+"1"
    
    return a + str(int(b) + 1).zfill(len(b))
