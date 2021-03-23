## Date: 12/03/2020
##Author:K.K.Dinali Indeewari


# function for check the range
def rangeChecking(userInput):
    if userInput <= 120 and userInput >= 0 and userInput % 20 == 0:
        savingOption1 = True


    else:
        print("range error")
        savingOption1 = False
        return savingOption1

# function for progression outcome
def progressChecking():
    if passCredit == 120:
        print("------Progress------")

    elif passCredit == 100:
        print("------Progress–module trailer------")

    elif failCredit >= 80:
        print("!!!!! Exclude !!!!! ")

    else:
        print("Do not progress–module retriever")


# --------------------------------------------------------------------------------------------------------------------------------------

print("\n")
print("             ✦ __✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__ ✦")
print("                 Welcome to the Student Progression Program - Student Version                ")
print("             ✦ __✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__✦__ ✦")
# --------------------------------------------------------------------------------------------------------------------------------------
print("\n")
print("#_______________________# USER INSTRUCTIONS #_______________________#")

print("01.Please use only enter 0  / 20 / 40 / 60 / 80 / 100 / 120 as your marks.")
print("02.Please do not use letters / symbols / special characters as your inputs.")

print("\n")
student_id = input("Please enter your Student ID number : ")
print("Hi " + str(student_id))
print("\n")
# --------------------------------------------------------------------------------------------------------------------------------------

save_2 = False
while save_2 == False:

    boolean_range_student_version = False
    while boolean_range_student_version == False:
        try:
            passCredit = int(input("Please enter your PASS credit :"))
            boolean_range_student_version = rangeChecking(passCredit)

        except ValueError:
            print("Integers required")
            boolean_range_student_version = False

    boolean_range_student_version = False
    while boolean_range_student_version == False:
        try:
            deferCredit = int(input("Please enter your DEFER credit :"))
            boolean_range_student_version = rangeChecking(deferCredit)

        except ValueError:
            print("Integers required")
            boolean_range_student_version = False

    boolean_range_student_version = False
    while boolean_range_student_version == False:
        try:
            failCredit = int(input("Please enter your FAIL credit:"))
            boolean_range_student_version = rangeChecking(failCredit)

        except ValueError:
            print("Integers required")
            boolean_range_student_version = False
    # ---------------------------------------------------------------------------------------------------------------------------------------
    total_marks_of_student_version = passCredit + failCredit + deferCredit  # Total calculated by the sum of 3 credit types
    if total_marks_of_student_version == 120:
        save_2 = True
        print("\n")
    else:
        print("Total incorrect")
        save_2 = False

progressChecking()

print("___________________________________________________________________")  # program exit message
print("Thanks for using Student progression Program. Have a nice day!")
print("\n")
# --------------------------------------------------------------------------------------------------------------------------------------
#                              end of the programme
