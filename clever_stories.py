"""
Program: Clever Stories
Author: Bryan Quiros

Description: It interacts with the user to tell a Mad Libs game story.

"""



print("Please enter the following: ")

adjective = input("Adjective: ")
animal = input("Animal: ")
verb = input("Verb: ")
exclamation = input("Exclamation: ")
verb_1 = input("Verb: ")
verb_2 = input("Verb: ")

print("Your story is: ")

print(f"The other day, I was really in trouble. It all started when I saw a very {adjective.lower()} {animal.lower()} {verb.lower()} down the hallway. \"{exclamation.capitalize()}!\" ")
print(f"I yelled. But all I could think to do was to {verb_1.lower()} over and over.")
print(f"Miraculously, that caused it to stop, but not before it tried to {verb_2.lower()} right in front of my family.")