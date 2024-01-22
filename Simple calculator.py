# -------Create variables---------
option = 0
no_of_integers = 0
num = 0
max_num = 0
min_num = 0
total = 0
num_list = []
even_num_list = []
average = float()
valid_no_of_integers = "No"
select_another_option = "Yes"
valid_option = "No"

# -----------------------Create the main menu------------------------------------
print("\n")
print("                         SIMPLE CALCULATOR                      ")
print("                         =================                      ")
print("\n")
print("                            Main Menu                           ")
print("\n")
print("                  1. Enter positive integer numbers             ")
print("                  2. Display Highest value                      ")
print("                  3. Display Lowest value                       ")
print("                  4. Display Average value                      ")
print("                  5. Display even numbers                       ")
print("                  6. Exit                                       ")
print("\n")
print("             ------------------------------------------------   ")
print("             |  (:  SELECT   OPTION   1   TO   PROCEED  :)  |   ")
print("             ------------------------------------------------   ")
print("\n")

# ----------------Select the first option----------------------
while valid_option == "No":
    try:
        option = int(input("Please indicate your option :  "))
        if (option > 1) and (option < 7):
            print("ERROR...First select option 1 \n")
        elif (option > 6) or (option < 1):
            print("ERROR...Check the menu and enter the correct number\n")
        else:
            valid_option = "Yes"
    except ValueError:
        print("ERROR...Please do not enter decimal numbers\n")


# --------Enter the number of positive integers that the user wants to input--------
if option == 1:
    while valid_no_of_integers == "No":
        try:
            no_of_integers = int(input("\nHow many numbers do you want to input?  "))
            if no_of_integers < 1:
                print("ERROR...Enter a positive integer")
            else:
                valid_no_of_integers = "Yes"

        except ValueError:
            print("ERROR...Please do not enter decimal numbers\n")
            continue

        # -------------Entering the positive integers-------------------------
        if valid_no_of_integers == "Yes":
            for count in range(0, no_of_integers):
                try:
                    num = int(input("Enter a number :  "))
                    if num <= 0:
                        print("! Do not enter any negative integers or a zero value..Please enter another number!")
                        num = int(input("Enter a number :  "))
                    num_list.append(num)
                    del (num_list[-1])
                    if num > 0:
                        num_list.append(num)
                        print(num_list)
                except ValueError:                                          # When user enters decimal values
                    print("ERROR...Please do not enter decimal numbers\n")
                    num = int(input("Enter a number :  "))
                    num_list.append(num)

        # -------If the user wants to select another option-------------
        while select_another_option == "Yes":
            try:
                option = int(input("\nPlease indicate your option :  "))
                # ----------------When option 2 is selected-----------------
                if option == 2:
                    max_num = num_list[0]
                    for n in num_list:
                        if n > max_num:
                            max_num = n
                    print("**The highest value is ", max_num, "**")

                # ----------------When option 3 is selected-----------------
                elif option == 3:
                    min_num = num_list[0]
                    for n in num_list:
                        if n < min_num:
                            min_num = n
                    print("**The lowest value is ", min_num, "**")

                # ----------------When option 4 is selected-----------------
                elif option == 4:
                    total = 0
                    for n in num_list:
                        total += n
                    average = total / len(num_list)
                    print("**The average of all the numbers is ", format(average, ".2f"), "**")

                # ----------------When option 5 is selected------------------
                elif option == 5:
                    even_num_list = [n for n in num_list if n % 2 == 0]
                    print("**All the even numbers = ", even_num_list, "**")

                # ----------------When option 6 is selected------------------
                elif option == 6:
                    print("\n")
                    print("END...HOPE YOU ENJOYED USING THIS CALCULATOR...BYE...BYE...")
                    break

                elif (option < 1) or (option > 6):
                    print("ERROR...Check the menu and enter the correct number")

            except ValueError:
                print("ERROR...Please do not enter decimal numbers\n")

