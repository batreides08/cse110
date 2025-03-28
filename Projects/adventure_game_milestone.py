# Funny Office Adventure

print("You're on your way to the office when disaster strikes: YOU FORGOT SOMETHING IMPORTANT. Do you check for your LAPTOP or your PANTS?")
choice = input("Type LAPTOP or PANTS: ").lower()

if choice == "laptop":
    print("You frantically unzip your bag... it's just a sandwich and three pens. Your laptop is still at home. Do you want to GO BACK or BLUFF your way through the day?")
    sub_choice = input("Type GO BACK or BLUFF: ").lower()

    if sub_choice == "go back":
        print("You sprint home, but by the time you return, you’ve missed the morning meeting... but gained 5,000 steps on your fitness tracker. Win?")
    elif sub_choice == "bluff":
        print("You log into the Zoom meeting using your phone and nod aggressively any time someone says 'synergy'. Nobody notices. You’re a legend.")
    else:
        print("You freeze. The moment of indecision causes a coworker to ask you to lead the next presentation. NOOOO!")

elif choice == "pants":
    print("You look down. Yep... pajama bottoms with flying tacos. Fashion statement or office faux pas? Do you want to BORROW from Lost and Found or PRETEND it’s intentional?")
    sub_choice = input("Type BORROW or PRETEND: ").lower()

    if sub_choice == "borrow":
        print("You find a pair of 1980s neon gym shorts in Lost and Found. Technically, you’re dressed. Spiritually, you’re thriving.")
    elif sub_choice == "pretend":
        print("You walk in confidently and claim it’s 'Pajama Productivity Day.' Your manager actually makes it a thing. You’re promoted. Somehow.")
    else:
        print("You hesitate, and your boss walks by and says, 'Nice pants!' Was that sarcasm? We'll never know.")

else:
    print("That’s not a valid option. You walk into the building, unsure of your purpose, and accidentally join a Zoom call that never ends.")
