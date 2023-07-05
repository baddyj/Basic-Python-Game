print('''
                                          .      .
                                 ./       |      |        \.
                               .:(        |i __ j|        ):`.
                             .'   `._     |`::::'|     _.'    `.
                           .'        "---.j `::' f.---"         `.
                     _____/     ___  ______      __    __   ___   \_   __
                    |      \   |   ||      |`__'|  \  /  | |   | |" \ |  |
                    |  .-.  | .'   `|_    _|\--/|   \/   |.'   `.|   \|  |
                    |  |_|  | |  i  | |  |  :"":|        ||  i  ||    |  |
                    |       / | .^. | |  |  ::::|        || .^. ||       |
                    |  .-.  \ | | | | |  |   :: |        || | | ||  |\   |
                    |  | |  |.' """ `.|  |      |  i  i  j' """ `.  | \  | LS
                    |  `-'  ||   _   ||  |      |  |\/|  |   _   |  | [  |
                   [|      / |  | |  ||  |      |  |  |  |  | |  |  | |  |].
                  ] `-----'  :--' `--::--'      `--' ::--"--::`--"--' `--':[
                  |      __  ::-"""`.:' "--.    .----::.----:: ,.---._    :|
                  [  .-""  "`'              \  /      "      `'       `-. :].
                 ]:.'                        \/                          `.:[
                 |/                                                        \|

''')
print("Welcome to Batman control-room.")
print("Your mission is to find the batman.")

#Write your code below this line 👇

choice1 = input('You\'re at the front-gate of the control room. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('Do you wanna attack the incoming enemy with your mysterious weapon?. Type "yes" to activate and "no" to hide \n').lower()
  if choice2 == "no":
    choice3 = input("You arrived at the main control-room unharmed. There are three doors in front of you. One red, one yellow and one blue. Choose the correct door? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found Bat-Man! You Won!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")