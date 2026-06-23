#Bao Pham, TIGER Team Blue, Lab 3

#Ticket 1

username = "blu_uest"

#PREDICT; Starting from 0 to 8, this expression will print the amount of characters included within the username.

print(len(username))

#Answer; Instead, the output reads 9. Maybe I need to learn more about how indexes work? But yes, it counted every letter including the @.

#Ticket 2

#PREDICT; The two letters that should print is "b" and "t."

print(username[0], username[7])

#Answer; The reason why its offset by one number, is because the first index character is 0.

#Ticket 3

#PREDICT; Both lines should output identically on the screen.

subgreeting = "Welcome to Loop, @"
fullgreeting = subgreeting + username + "!"
print(fullgreeting)

print(f"Welcome to Loop, @{username}!")

#Answer; At first it was via concatenation, but after learning the f string, I can easily pull from a variable for use.

#Ticket 4

#username[0] = "X" #Error; username[0] = "X" TypeError: 'str' object does not support item assignment
#PREDICT; The whole file would simply not run.

print(username.upper()) #Output; BLU_UEST

#Answer; Immutable means unchangable, as the index is set in stone from the variable.

#Ticket 5

#PREDICT; The list would contain 3 respective entries, and the PS6 post would be printed first.

feed = ["unboxed that new ps6 brahhh", "#HELP", "woah"]

print(len(feed))
print(feed[0])

#Answer; The first index item explicitly says 0, but there are 3 items in the list respectively.

#Ticket 6

#PREDICT; This will respectively be the 4th item in the index, but will be counted as 3 intangibly.

feed.append("newest game just dropped")
print(feed)

#Answer; The fourth post is at index 3, because index 0 is counted as an entry.

#Ticket 7

#PREDICT; The oldest post should be removed via its index, and the rest of the captions will be sorted alphabetically.

feed.pop(0)
feed.sort() #Should sort all captions alphabetically.
print(feed)

#Answer; Methods I've used are .pop, to remove the oldest caption, and .sort, to sort alphabetically.

#Ticket 8

#PREDICT; The file will not run if profile[0] is present, and followers will be printed as 34.

profile = {
    "username": username,
    "followers": 34,
    "verified": False
}

#profile[0] #Error; profile[0] KeyError: 0

print(profile["followers"])

#Answer; Dictionaries are great for looking up values by explicit label, and have the added bonus of being changable (mutable).

#Ticket 9

#PREDICT; The file will simply not run, because "age" doesn't exist as a key.

profile["followers"] += 50
profile["bio"] = "Welcome to my profile!"
print(profile)
profile.get("age")

#Answer; Profile [age] may or may not create a new key, which is a problem for mutability. so .get can return an error.

#Ticket 10

#PREDICT; Hopefully, and I'm really hoping, this exactly prints as "@blu_uest has 84 followers and 3 posts. Top post: newest game just dropped"

print(f"@{profile["username"]} has {profile["followers"]} followers and {len(feed)} posts. Top post: {feed[2]}")

#Answer; There was significant usage of f strings throughout this line, which I took an extra 15 minutes to solve and troubleshoot. F strings allow you to use other functions as well, like grabbing dictionary keys and indexing lists.
#IT ACTUALLY RAN WHAT