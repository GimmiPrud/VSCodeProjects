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

# Soluzione ES. 3-3:

machine: list = ["bmv","audi","toyota"]

print(f"mi piacerebbe sfrecciare con una {machine[0]} M5  ")

print(f"vorrei tanto possedere un {machine[1]} R1")

print(f"spero un giorno di correre con una {machine[2]} Supra")

# ES. 3-4:

'''If you could invite anyone, living or deceased, to dinner, who would you invite?
Make a list that includes at least three people you’d like to invite to dinner.
Then use your list to print a message to each person, inviting them to dinner'''

# Soluzione ES. 3-4:

people: list = ["Giulio Cesare","Napoleone","Dio"]

for p in people:
    
    print(f" Ciao {p} ci saresti questo fine settimana per una cena, ho già sentito gli altri")

# ES. 3-5:

'''You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4.
Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.'''

# Soluzione ES. 3-5:

people: list = ["Giulio Cesare","Napoleone","Dio"]

for p in people:
    
    print(f" Ciao {p} ci saresti questo fine settimana per una cena, ho già sentito gli altri")
    
print(f" Niente ,{people[2]} come sempre non c'è ")

people[2] = "Maradona"

for p in people:
    print(f" Ciao {p}, cena ore 20:00, puntuale")
    
# ES. 3-6:
'''
You just found a bigger dinner table, so now more space is available.
Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5.
Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.'''

# Soluzione ES. 3-6:

people: list = ["Giulio Cesare","Napoleone","Dio"]

for p in people:
    
    print(f" Ciao {p} ci saresti questo fine settimana per una cena, ho già sentito gli altri")
    
print(f" Niente ,{people[2]} come sempre non c'è ")

people[2] = "Maradona"

for p in people:
    print(f" Ciao {p}, cena ore 20:00, puntuale")
    
print("aspettate ho trovato un tavolo più grande, quinidi penso che inviterò qualcun'altro")

people.insert(0,"Dante Alighieri")

people.insert(1,"Ozzy Osbourne")

people.append("Bruce Lee")

for p in people:
    print(f" Buonasera {p} alla fine siamo sei, ci vediamo direttamente a ristorante")
    
# ES. 3-7:
'''
You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6.
Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list.
Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list.
Print your list to make sure you actually have an empty list at the end of your program.'''

# Soluzione ES. 3-7




    

    





























  






