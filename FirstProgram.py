#FirstProgram.py
#Name: Connor Pell
#Date: 8/31/2025
#Assignment: Lab 1

def main():
  print("First Program")
  #Say hello
  print("Hello!")
  #Ask for the user's name
  usr_name = input("What is your name?    ")

  #Use the user's name in the program.
  print(f"Nice to meet you, {usr_name}!")
  #Ask the user for their age.
  usr_age = int(input("How old are you?   "))

  #Tell the user what year they were born in.
  #Assume that they have not had their birthday yet this year.
  #2024 since they haven't had their birthday yet.
  usr_birthyear = 2024 - usr_age
  print(f"You must have been born in {usr_birthyear}, {usr_name}.")
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
