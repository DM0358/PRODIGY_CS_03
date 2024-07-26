def printStrongNess(input_string): 
    n = len(input_string)  
    #Checking lower alphabet in string
    hasLower = False
    hasUpper = False
    hasDigit = False
    specialChar = False
    normalChars = "abcdefghijklmnopqrstu"
    "vwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
    for i in range(n): 
        if input_string[i].islower(): 
            hasLower = True
        if input_string[i].isupper(): 
            hasUpper = True
        if input_string[i].isdigit(): 
            hasDigit = True
        if input_string[i] not in normalChars: 
            specialChar = True
    # Strength of password  

    print("Strength of password:-", end = "") 
    if (hasLower and hasUpper and 
        hasDigit and specialChar and n >= 8): 
        print("password is Strong") 
    elif ((hasLower or hasUpper) and 
          specialChar and n >= 6): 
        print("password is Moderate, you need to add more complex and long") 
    else: 
        print("password is Weak, add more letter,number,alphabet to make it strong") 
# Driver code  
if __name__=="__main__":
    input_string = "WSNjsjs229@#*"
    printStrongNess(input_string) 
