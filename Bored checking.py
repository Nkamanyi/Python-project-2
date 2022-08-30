
def main():
    word = True
    while word:
        an = input("Answer Y or N: ")
        if an != "y" and an != "n" and an != "Y" and an != "N":
            print("Incorrect entry.")
        else:
             word = False
             print(f"You answered {an}")
main()
