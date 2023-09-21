upper_str = ""
    for letter in str:
        chr_code = ord(letter)
        if 97 <= chr_code <= 122:
            upper_str += chr(chr_code - 32)
        else:
            upper_str += letter
    
