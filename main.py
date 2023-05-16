def is_palindrome(string: str) -> bool:
    limpa_string = string.lower().replace(" ","").replace(".","").replace(",","").replace("!","")
    return limpa_string == limpa_string[::-1]