import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
"Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
"Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
"Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim","Afghanistan", "Albania", "Algeria", "Argentina", "Australia", "Austria", "Bangladesh",
"Belarus", "Belgium", "Bhutan", "Bolivia", "Botswana", "Brazil", "Bulgaria", "Cambodia",
"Cameroon", "Canada", "Chile", "China", "Colombia", "Croatia", "Cuba", "Czech Republic",
"Denmark", "Dominican Republic", "Ecuador", "Egypt", "Estonia", "Ethiopia", "Fiji",
"Finland", "France", "Germany", "Ghana", "Greece", "Hungary", "Iceland", "Indonesia",
"Iran", "Iraq", "Ireland", "Israel", "Italy", "Japan", "Jordan", "Kazakhstan", "Kenya",
"Malaysia", "Maldives", "Mexico", "Morocco", "Nepal", "Netherlands", "New Zealand",
"Norway", "Pakistan", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania",
"Russia", "Saudi Arabia" ,"Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal","Alabama", "Alaska","Arizona", "Arkansas", "California", "Colorado", "Connecticut",
"Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
"Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
"Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
"New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina",
"North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
"South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
"Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

chosen_word = random.choice(word_list).lower()
lives = 6
game_over = False
correct_letters = []

# Create placeholder with spaces intact
display = ""
for char in chosen_word:
    if char == " ":
        display += " "
    else:
        display += "_"

print(display)

while not game_over:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please guess a single valid letter.")
        continue

    if guess in correct_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    if guess in chosen_word:
        correct_letters.append(guess)
        print(f"Good guess: '{guess}' is in the word!")
    else:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        print(stages[6 - lives])
        if lives == 0:
            game_over = True
            print("You lose.")
            print(f"The correct word was: {chosen_word.title()}")
            break

    # Update display string
    new_display = ""
    for letter in chosen_word:
        if letter == " ":
            new_display += " "
        elif letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    print(new_display)
    display = new_display

    if "_" not in display:
        game_over = True
        print("Congratulations! You win!")

    # Show remaining hangman stage
    print(stages[lives])
