import random, time

print ("Welcome to the Python Future Predictor.")
print ("This will work out what you are destined to be... ")

allAdjectives = ["Brave", "Evil", "Angry" "Kind", "Sweaty"]
allThings = ["Toaster", "Animal", "Car", "Pizza", "Army"]
allJobs = ["Taster", "Doctor", "Fighter", "Leader", "Teacher"]

name = input("Please enter your name > ")

pastLife = random.choice(allAdjectives) + " " + random.choice(allThings) + " " + random.choice(allJobs)

print (name, "in the future you will be a...")
time.sleep(2)
print (pastLife)
