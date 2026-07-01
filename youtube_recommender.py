# Welcome to the YouTube Video Recommendation Assistant! Based on your interests, this program will suggest some popular YouTube channels for you to explore.
#To start the program, we chose the language python, so to run the program in the terminal, you can use the command: python youtube_recommender.py :)

#Main menu
while True:

    print("=== YouTube Video Recommendation Assistant ===")
    print("\nChoose a category:")
    print("1. Gaming")
    print("2. Music")
    print("3. Education")
    print("4. Sports")

    #User choice input
    choice = input("\nEnter your choice (1-4) or 'q' to quit: ")

    # Recommendations based on user choice
    if choice == "1":
        print("\nRecommended Channels:")
        print("- PewDiePie")
        print("- Markiplier")
        print("- Jacksepticeye")

    elif choice == "2":
        print("\nRecommended Channels:")
        print("- T-Series")
        print("- Vevo")
        print("- NCS")

    elif choice == "3":
        print("\nRecommended Channels:")
        print("- Khan Academy")
        print("- Crash Course")
        print("- freeCodeCamp")

    elif choice == "4":
        print("\nRecommended Channels:")
        print("- ESPN")
        print("- FIFA")
        print("- NBA")

    elif choice == "q" or choice == "Q":
        print("\nThank you for using the YouTube Video Recommendation Assistant! Enjoy exploring the channels!")
        break

    #Input validation for invalid choices
    else:
        print("\nInvalid choice. Please input the correct choice.")
        continue

    again = input ("\nWould you like to choose another category? (Y/N): ").upper()

    if again != "Y":
        print("\nThank you for using the YouTube Video Recommendation Assistant! Enjoy exploring the channels!")
        break