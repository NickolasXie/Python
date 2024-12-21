userString = input("Enter a string: ").upper()
charShift = int(input("Enter an integer for the character shift: ")) #assume that the user will enter a value between 1 to 5 inclusive
cipherText = "" #initially blank (this caesar cipher exercise could've also been done with lists)
for x in userString:
    if ord(x) >= 65 and ord(x) <= 90: #determining whether or not a character in the string is in the alphabet (applies to all)
        # (ALTERNATIVELY: can also use isalpha() to identify letters from alphabet)
        numValue = ord(x)
        shiftedValue = ord(x) + charShift #rules of cipher, ASCII value will increase by user's input shift
        if shiftedValue > 90: # this indicates the wrap around for letters like Z
            shiftedValue -= 26 # e.g. ascii code of z = 90, but the maximum value is 90 and cannot be exceeded. therefore subtracting 26 gets to "B"
        cipherText += chr(shiftedValue) #add to overall cipher string
    else:
        cipherText += x #if character is special character or space, ignore --> it should be unchanged
print(cipherText)
