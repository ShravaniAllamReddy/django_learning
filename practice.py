

# # Print a separator.
# print('-' * 18)

# print(firstname)
# print(lastname)

# # Print a separator.
# print('-' * 18)

while True:
# Prompt user for student's identification information...
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
# Prompt for confirmation, and save what user entered.
    confirm = input("Is this information correct? (Y/N)")
    if confirm == 'Y':
        # Break kills a loop immediately.
        print(firstname + ' ' + lastname)
        break
    else:
        # You don't need an "else" branch, but we're using one just to
        # demonstrate how to use continue. It just means, "run the loop again."
        continue
