# Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values:

ascii_dict = {chr(i): i for i in range(ord('a'), ord('z') + 1)}
#chr command converts the ASCII integer to its corresponding character, ASCII value of 'a' is 97, so chr(97) gives string 'a'
#ord command gives the ASCII value of the character 

# Print the resulting dictionary
print("Dictionary with Alphabet as Keys and ASCII Values as Values:")
print(ascii_dict)