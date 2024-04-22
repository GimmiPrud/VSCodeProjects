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

# ES. 2-8:

'''Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename.
Then use the removesuffix() method to display the filename without the file extension, like some file browsers do'''

# Soluzione ES. 2-8:

File_name: str = 'python_notes.txt'

print(File_name.removesuffix('.txt'))

# ES. 3-1:

'''Store the names of a few of your friends in a list called names. 
Print each person’s name by accessing each element in the list, one at a time.'''

# Soluzione ES. 3-1:

names: list = ["Michele","Mattia","Giacomo","Andrea","Federico"]

name1 = names[0]
name2 = names[1]
name3 = names[2]
name4 = names[3]
name5 = names[4]  

print(name1, name2, name3, name4, name5 )

# ES. 3-2:

'''Start with the list you used in Exercise 3-1,
but instead of just printing each person’s name, 
print a message to them. 
The text of each message should be the same, 
but each message should be personalized with the person’s name.'''

# Soluzione ES. 3-2:

namess: list = ["Michele","Mattia","Giacomo","Andrea","Federico"]
for name in namess:
    print(f"{name} cosa fai oggi pomeriggio ?")

# Es. 3-3:

'''Think of your favorite mode of transportation,
such as a motorcycle or a car, and make a list that stores several examples.
Use your list to print a series of statements about these items, 
such as “I would like to own a Honda motorcycle.”'''

# Soluzione ES. 3-3

machine: list = ["bmv","audi","toyota"]


















  






