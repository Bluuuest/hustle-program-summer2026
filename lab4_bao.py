# Bao Pham, Lab 4, Intro to Python

#Ticket 1

ages = [17, 11, 25, 13, 9]

for age in ages:
    if age >= 13:
        print(f"{age} Welcome")
    else:
        print(f"{age} You are too old, or young to enter")

#PREDICT; The ages which will get access granted, will be 13, 17, and 25. The excluded are 9 and 11.

#Explain; The variable "age" temporarily holds the index item from the "ages" list, and explicitly states the limit.

#Ticket 2

verify = "yes"

while verify == "yes":
    age = int(input("Please type your age. = "))
    if age >= 13:
        print("Hello there!")
    else:
        print("Sorry, you can't enter.")
    verify = input("Wanna try another age? yes/no = ")

#PREDICT; If the user types no, I feel like the block wouldn't have to verify ages further.

#Explain; You can write new variables within a while loop environment, making it easier to change how functions work as they happen instead of using predefined values.

#Ticket 3

while True:
    age = input("Please type in your age, or the word stop = ")
    if age == "stop":
        break
    elif int(age) >= 13:
        print("Welcome back!")
    else:
        print("Sorry, too young to enter")

#PREDICT; If I forgot the "break" statement, the loop would infinitely run.

#Explain; This while 'true' loop is able to run without any circumstances of another variable, so it runs freely.

#Ticket 4


def grant_access(age):
    if int(age) >= 13:
        return True
        approved += 1
    else:
        return False

for age in ages:
    if grant_access(age) == True:
        print("yo whats good yall")
    else:
        print("nuh uh")

#PREDICT; Now, instead of relying on variables to age check the system, we now have a predefined function to verify for us.

#Explain; As you don't have to write it over and over again.

#Ticket 5;

new_users = [22, 10, 15, 8, 19, 13]
approved = 0

def signup_log(new_users):
    
    for entry, age in enumerate(new_users, start=1):
        print(f"Registered; no.{entry} / User is {age} / Access: {grant_access(age)}")
    print(f"Approved; {approved} out of {len(new_users)}")

for age in new_users:
    if grant_access(age):
        approved += 1
    else:
        continue

signup_log(new_users)

#PREDICT; Registered no.# / User is 'age' / Access: (True or False), Approved 4 out of 6.

#Explain; After defining the 'signup_log(new_users)' function, I had to use a for loop for enumerating the users list after each entry. After that, it will print an f string which formats the data about the user.

#Personal note, it took me 3 EXTRA hours (with help from awesome people) to figure out how to track the amount of approved users, and I have no idea if this method is still allowed /mn /nsrs.