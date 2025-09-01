#MadLib.py
#Name: Connor Pell
#Date: 8/31/2025
#Assignment: Lab 1

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("Give me a noun: ")
  noun2 = input("Okay, now another noun: ")
  adj1 = input("I need an adjective as well: ")
  noun3 = input("Lot of nouns in this story, give me another one please: ")
  adj2 = input("Adjective please: ")
  adj3 = input("Another one of those adjectives: ")
  noun4 = input("This one needs to be a noun: ")
  adj4 = input("Another Adjective Already: ")
  verb1 = input("Just one verb: ")
  emotion1 = input("let's switch it up, give me an emotion: ")
  noun6 = input("Last one, need another noun.: \n")
  #Print the story with the user supplied words.

  #not the best madlib I won't lie.
  print(f"Yesterday, I saw a {noun1} walking down the street. It was carrying a {noun2} that looked very {adj1}.\nSuddenly, a {noun3} appeared out of nowhere and made a {adj2} noise. I felt {adj3}, but then I noticed a {noun4} wearing a {adj4} hat. \nThe {noun4} shouted, “Quick! Grab the {noun1} before it {verb1 + 's'} away!” \nEveryone around was {emotion1}, but I just stood there holding a {noun6}.\n")
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
