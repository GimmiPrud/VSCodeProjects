# Giammarco Prudenzi                       18/04/2024

# ES. 2-3:
'''Use a variable to represent a person’s name, and print a message to that person.
Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”'''

# Soluzione ES. 2-3:
name: str = "Alessio"

print(f"Ciao {name} would you like to learn some python today")

# ES. 2-4:
'''Use a variable to represent a person’s name. 
then print that person’s name in lowercase, uppercase, and title case.'''

# Soluzione ES. 2-4:
N: str = "Carletto"

print(N.upper(), N.title(), N.lower())
# oppure:
N: str = "Carletto"

N_lower = N.lower()
N_upper = N.upper()
N_title = N.title()

print(N_lower)
print(N_title)
print(N_upper)

# ES. 2-5:
'''Find a quote from a famous person you admire. Print the quote and the name of its author.
Your output should look something like the following, including the quotation marks:
Albert Einstein once said, “A person who never made a mistake never tried anything new.”'''

# Soluzione ES. 2-5:

name: str = "Thomas Edison"
cit: str = "\"Molti dei fallimenti della vita sono persone che non si sono rese conto di quanto fossero vicine al successo quando hanno rinunciato\""
print(f"{name} una volta disse:\n {cit}")


  






