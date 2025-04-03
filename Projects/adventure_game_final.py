print("YOU WAKE UP LATE FOR WORK AND REALIZE SOMETHING IS MISSING. DO YOU CHECK FOR YOUR LAPTOP, YOUR PANTS, OR YOUR COFFEE?")
choice1 = input("Type LAPTOP, PANTS, or COFFEE: ").lower()

if choice1 == "laptop":
    print("YOUR BAG IS LIGHT... TOO LIGHT. NO LAPTOP. DO YOU GO BACK HOME OR TRY TO BLUFF THROUGH THE DAY?")
    choice2 = input("Type GO BACK or BLUFF: ").lower()

    if choice2 == "go back":
        print("YOU RUSH HOME, GRAB THE LAPTOP, AND RETURN... JUST IN TIME FOR A ZOOM MEETING THAT NEVER ENDS. DO YOU FAKE TECH ISSUES OR TURN OFF YOUR CAMERA?")
        choice3 = input("Type FAKE or CAMERA: ").lower()

        if choice3 == "fake":
            print("YOU UNPLUG YOUR ROUTER AND EAT SNACKS FOR TWO HOURS. SMART MOVE.")
        elif choice3 == "camera":
            print("BIG MISTAKE. YOU ACCIDENTALLY LEAVE THE CAMERA ON WHILE DOING YOGA. YOU’RE NOW A MEME IN THE OFFICE SLACK CHANNEL.")
        else:
            print("CONFUSED, YOU HIT ALL THE BUTTONS AND ACCIDENTALLY SCREEN SHARE YOUR SHOPPING CART FOR SPAGHETTI HATS.")

    elif choice2 == "bluff":
        print("YOU LOG IN FROM YOUR PHONE. DO YOU NOD AGGRESSIVELY OR TYPE GENERIC RESPONSES IN THE CHAT?")
        choice3 = input("Type NOD or CHAT: ").lower()

        if choice3 == "nod":
            print("EVERYONE THINKS YOU’RE REALLY ENGAGED. YOU GET ASKED TO LEAD A NEW PROJECT. OH NO.")
        elif choice3 == "chat":
            print("YOU TYPE 'AGREED' EVERY 3 MINUTES. NO ONE NOTICES YOU HAVE NO IDEA WHAT’S HAPPENING.")
        else:
            print("YOU TYPE 'LOL' AND REALIZE THIS ISN’T A GROUP CHAT. WHOOPS.")

    else:
        print("YOU FREEZE, UNSURE WHAT TO DO, AND TRIP OVER A ROAMING ROBOT VACUUM NAMED TODD.")

elif choice1 == "pants":
    print("YOU’RE WEARING TACO PAJAMA BOTTOMS. DO YOU BORROW FROM LOST AND FOUND OR PRETEND IT’S A THEME DAY?")
    choice2 = input("Type BORROW or PRETEND: ").lower()

    if choice2 == "borrow":
        print("YOU FIND A PAIR OF NEON GYM SHORTS LABELED 'PROPERTY OF THE CEO'. DO YOU WEAR THEM OR KEEP LOOKING?")
        choice3 = input("Type WEAR or LOOK: ").lower()

        if choice3 == "wear":
            print("THE CEO NODS IN APPROVAL. 'NICE SHORTS,' HE SAYS. PROMOTION UNLOCKED.")
        elif choice3 == "look":
            print("YOU FIND A VINTAGE SUIT FROM 1982. IT SMELLS LIKE POWER. PEOPLE RESPECT YOU TODAY.")
        else:
            print("YOU TRY ON A SCARF AS PANTS. CREATIVE, BUT SECURITY ESCORTS YOU OUT.")

    elif choice2 == "pretend":
        print("YOU WALK IN CONFIDENTLY AND DECLARE IT'S 'PAJAMA PRODUCTIVITY WEDNESDAY'. DO YOU EMAIL HR OR START A TREND?")
        choice3 = input("Type EMAIL or TREND: ").lower()

        if choice3 == "email":
            print("HR RESPONDS WITH A CONFUSED GIF. YOU’RE PUT ON A WATCHLIST.")
        elif choice3 == "trend":
            print("BY LUNCHTIME, HALF THE OFFICE IS IN SLIPPERS. YOU’RE A VISIONARY.")
        else:
            print("YOU DECLARE A HOLIDAY, BUT NO ONE LISTENS. SAD TACO PANTS DAY.")

    else:
        print("YOU SPIN IN A CIRCLE AND ACCIDENTALLY JOIN A DANCE CLASS ON THE 3RD FLOOR.")

elif choice1 == "coffee":
    print("YOU FORGOT YOUR COFFEE. DISASTER. DO YOU STOP AT THE CAFÉ OR POWER THROUGH?")
    choice2 = input("Type CAFE or POWER: ").lower()

    if choice2 == "cafe":
        print("THE BARISTA SPELLS YOUR NAME AS 'TOAST'. DO YOU CORRECT THEM OR EMBRACE IT?")
        choice3 = input("Type CORRECT or EMBRACE: ").lower()

        if choice3 == "correct":
            print("THE BARISTA APOLOGIZES BY GIVING YOU A FREE COOKIE. WORTH IT.")
        elif choice3 == "embrace":
            print("YOU INTRODUCE YOURSELF AS 'TOAST' ALL DAY. PEOPLE LOVE YOU.")
        else:
            print("YOU MUMBLE SOMETHING AND END UP WITH FOUR ESPRESSOS.")

    elif choice2 == "power":
        print("BOLD MOVE. BY 10AM, YOU’RE HALLUCINATING EMAILS. DO YOU TAKE A NAP IN THE SUPPLY CLOSET OR STARE INTO THE VOID?")
        choice3 = input("Type NAP or VOID: ").lower()

        if choice3 == "nap":
            print("YOU WAKE UP TO A POST-IT ON YOUR FOREHEAD THAT SAYS 'NICE SNORE'.")
        elif choice3 == "void":
            print("THE VOID STARES BACK. YOU FIND ENLIGHTENMENT AND ALSO A STAPLER YOU LOST LAST WEEK.")
        else:
            print("YOU ACCIDENTALLY EMAIL A POEM TO THE WHOLE COMPANY. IT WAS... EMOTIONAL.")

    else:
        print("YOU TRY TO MAKE COFFEE FROM TEA BAGS. THE OFFICE VENDING MACHINE SPITS OUT A SOCK.")

else:
    print("UNSURE WHAT TO DO, YOU WALK INTO A RANDOM MEETING LABELED 'THE FUTURE OF PAPERCLIPS'. YOU NEVER RETURN.")
