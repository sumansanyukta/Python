a = "Jack and Jill went up the hill"
print(a.capitalize()) # Capitalizes the first character of the string
print(a.casefold())   # Converts the string to lowercase, more aggressive than lower()
print(a.center(50, '*')) # Centers the string in a field of 50 characters
print(a.count('a'))   # Counts occurrences of 'a' in the string
print(a.encode())     # Encodes the string to bytes using default encoding (UTF-8)
print(a.endswith('hill')) # Checks if the string ends with 'hill'
print(a.find('and'))  # Finds the first occurrence of 'and' and returns its index
print(a.index('and')) # Similar to find, but raises an error if 'and' is not found
print(a.isalnum())    # Checks if all characters are alphanumeric
print(a.isalpha())    # Checks if all characters are alphabetic
print(a.isdigit())    # Checks if all characters are digits
print(a.islower())    # Checks if all characters are lowercase
print(a.isupper())    # Checks if all characters are uppercase
print(a.join(['Start: ', ' End'])) # Joins the string with a list of strings
print(a.lower())      # Converts the string to lowercase
print(a.lstrip())     # Removes leading whitespace from the string
print(a.replace('hill', 'mountain')) # Replaces 'hill' with 'mountain'
print(a.rfind('and')) # Finds the last occurrence of 'and' and returns its index
print(a.rindex('and')) # Similar to rfind, but raises an error if 'and' is not found
print(a.rstrip())     # Removes trailing whitespace from the string
print(a.split())      # Splits the string into a list of words
print(a.splitlines()) # Splits the string into a list of lines
print(a.startswith('Jack')) # Checks if the string starts with 'Jack'
print(a.strip())      # Removes leading and trailing whitespace from the string
print(a.title())      # Converts the first character of each word to uppercase
print(a.upper())      # Converts the string to uppercase
print(a.zfill(50))    # Pads the string with zeros on the left to fill to 50 characters
print(a.swapcase())   # Swaps the case of all characters in the string
print(a.removeprefix('Jack ')) # Removes the prefix 'Jack '
print(a.removesuffix('hill')) # Removes the suffix 'hill'
print(a.partition('and')) # Splits the string at the first occurrence of 'and'
print(a.rpartition('and')) # Splits the string at the last occurrence of 'and'
print(a.format_map({'name': 'Jack', 'activity': 'hill climbing'})) # Formats the string using a mapping
print(a.format('Jack', 'hill climbing')) # Formats the string using positional arguments
print(a.split(' '))   # Splits the string by spaces into a list
print(a.rsplit(' ', 2)) # Splits the string from the right by spaces, limiting to 2 splits
print(a.translate(str.maketrans('aeiou', '12345'))) # Translates vowels to numbers
print(a.removeprefix('Jack ')) # Removes the prefix 'Jack ' from the string
print(a.removesuffix('hill')) # Removes the suffix 'hill' from the string
print(a.casefold())   # Converts the string to lowercase, more aggressive than lower()
print(a.isprintable()) # Checks if all characters in the string are printable
print(a.format('Jack', 'hill climbing')) # Formats the string using positional argumentsname': 'Jack', 'activity': 'hill