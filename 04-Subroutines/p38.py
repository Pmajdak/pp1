def f(palindrome):
    cleaned_palindrome = ''.join(char.lower() for char in palindrome if char.isalnum())
    
    return cleaned_palindrome == cleaned_palindrome[::-1]
