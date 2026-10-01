print("ABANDONED HOUSE MYSTERY")

name = input("Detective name: ").strip()
print("Welcome,", name)

living_room = True
bedroom = True
basement = True
kitchen_first = True

flashlight = False

kitchen_visited = False
kitchen_hint = False

found_footprints = False
found_glove = False
found_window = False
found_body = False
found_note = False

# Kitchen action flags
cupboard_available = True
counter_available = True
glass_available = True

playing = True

while playing:

    print("\nWhere do you go?")

    if living_room:
        print("1 - Living Room")
    if bedroom:
        print("2 - Bedroom")
    if basement:
        print("3 - Basement")

    if kitchen_first:
        print("4 - Kitchen")
    elif kitchen_hint:
        print("4 - Return to Kitchen")

    print("5 - Quit")

    choice = input("Choice: ").strip()

    # Living Room
    if choice == "1" and living_room:
        print("\nYou enter the Living Room.")
        print("You notice dusty footprints.")

        investigate = input("Investigate the footprints? (yes/no): ").strip().lower()
        if investigate == "yes":
            print("They lead toward the kitchen.")
            found_footprints = True
        else:
            print("you think: Maybe I should have looked closer.")

        living_room = False

    # Bedroom
    elif choice == "2" and bedroom:
        print("\nYou enter the Bedroom.")
        print("A drawer is open.")

        search = input("Search the drawer? (yes/no): ").strip().lower()
        if search == "yes":
            print("You find a bloody glove.")
            found_glove = True
        else:
            print("you think: Something could be hiding in there.")

        bedroom = False

    # Basement
    elif choice == "3" and basement:
        print("\nYou go into the Basement...")
        print("It is DARK.")

        if flashlight == False:
            print("You can't see anything.")

            if kitchen_visited == False:
                print("you think: I need to find a flashlight.")
            else:
                print("you think: I think I remember seeing a flashlight in the kitchen.")
                kitchen_hint = True

        else:
            print("With the flashlight, you see a BODY on the floor.")
            found_body = True

            check = input("Search nearby for evidence? (yes/no): ").strip().lower()
            if check == "yes" and found_note == False:
                print("You find a torn note: 'I can't take it anymore... -H'")
                print("you think: That sounds like the husband.")
                found_note = True
            else:
                print("you think: I shouldn't touch anything else.")

            basement = False

    # Kitchen
    elif choice == "4" and (kitchen_first or kitchen_hint):
        print("\nYou enter the Kitchen.")
        kitchen_visited = True

        if kitchen_first:
            print("Broken window. Glass everywhere.")
            kitchen_first = False

        in_kitchen = True
        while in_kitchen:

            print("\nKitchen actions:")

            if cupboard_available:
                print("A - Check cupboard")
            if counter_available:
                print("B - Look on counter")
            if glass_available:
                print("D - Search broken glass")

            print("C - Leave kitchen")

            action = input("Choose an option: ").strip().lower()

            if action == "a" and cupboard_available:
                print("\nYou open the cupboard...")
                print("you think: I didn’t find anything useful.")
                cupboard_available = False

            elif action == "b" and counter_available:
                if flashlight == False:
                    take = input("You see a flashlight. Take it? (yes/no): ").strip().lower()
                    if take == "yes":
                        flashlight = True
                        print("You picked up the flashlight.")
                    else:
                        print("you think: I might need that later.")
                else:
                    print("you think: I didn’t find anything useful.")

                counter_available = False

            elif action == "d" and glass_available:
                look = input("Look closely at the window area? (yes/no): ").strip().lower()
                if look == "yes":
                    print("Mud on the sill. Someone climbed in.")
                    found_window = True
                else:
                    print("you think: I didn’t find anything useful.")

                glass_available = False

            elif action == "c":
                print("You leave the kitchen.")
                in_kitchen = False

            else:
                print("you think: I didn’t find anything useful.")

    elif choice == "5":
        playing = False

    else:
        print("you think: I didn’t find anything useful.")

    # Ending
    if found_footprints and found_glove and found_window and found_body and found_note:
        print("\nYou connect everything together...")
        print("you think: The glove, the break-in, the footprints... it all fits.")
        print("Conclusion: the husband killed the wife.")
        playing = False

print("\nThanks for playing!")
