from __future__ import print_function
import sys


# for task 3 and 4
def loops(list_1, list_2, list_3, list_4):
    print()
    for z in range(len(list_1)):
        print("          progress - ", list_1[z])
    for j in range(len(list_2)):
        print("          Progress (module trailer) - ", list_2[j])
    for k in range(len(list_3)):
        print("          Module retriever - ", list_3[k])
    for r in range(len(list_4)):
        print("          Excluded - ", list_4[r])
    print()


# for task 2
def vertical(counts, num):
    for h in range(0, counts):
        list2[num].append('*')


# we have to use list for append user's input.thats why this used
def list_count(list_all, input_1, input_2, input_3):
    list_fun = [input_1, input_2, input_3]
    list_all.append(list_fun)


# I had to use this print type for twice thats why use this
def finish():
    print("\n     |----------------------------|")
    print("     |           FINISH           |")
    print("     |----------------------------|")


progress = 0
Trailer = 0
Retriever = 0
Excluded = 0
outcome = 0
prograss_list = []
Trailer_list = []
Retriever_list = []
Excluded_list = []


def task1(prog, tra, ret, exclud, out_come, prog_list, tra_list, retr_list, excl_list):
    """ this for task one. I used while loop for get this input untill user do stop.
      also i wat to count input and print conditions for do task 2, 3, 4 """
    range_req = range(0, 121, 20)
    while True:
        try:
            pass1 = int(input("| Please enter your credits at pass: | "))
            if pass1 in range_req:
                defer = int(input("| Please enter your credit at defer: | "))
                if defer in range_req:
                    fail = int(input("| Please enter your credit at fail:  | "))
                    if fail in range_req:
                        if pass1 + defer + fail == 120:
                            if pass1 == 120:
                                print("\n          Progress\n", " ")
                                list_count(prog_list, pass1, defer, fail)
                                prog += 1

                            elif pass1 in range(100, 120):
                                print("\n          Progress (module trailer)\n", "")
                                list_count(tra_list, pass1, defer, fail)
                                tra += 1

                            elif fail >= 80:
                                print("\n          Exclude\n", " ")
                                list_count(excl_list, pass1, defer, fail)
                                exclud += 1

                            elif fail < 80:
                                print("\n          Do not progress – module retriever\n", "")
                                list_count(retr_list, pass1, defer, fail)
                                ret += 1
                            out_come += 1
                        else:
                            print("\n          Total incorrect\n", "")
                            continue
                    else:
                        print("\n          Out of range\n", "")
                        continue
                else:
                    print("\n          Out of range\n", "")
                    continue
            else:
                print("\n          Out of range\n", "")
                continue
            statement = input("| Would you like to enter another set of data? |\n"
                              "| (Enter 'y' for yes or 'q' to quit and view results) : | ")
            print()
            if statement.upper() == 'Y':
                continue
            elif statement.upper() == 'Q':
                return prog, tra, ret, exclud, out_come, prog_list, retr_list, excl_list, tra_list

            else:
                print("          'y' or 'q'  required")
                continue
        except ValueError:
            print("\n          Integer required\n", "")
            continue


print("     |------------------------------|")
print("     | Enter the number according   |")
print("     | to the version you wan       |")
print("     |    1 - for 'Staff Version'   |")
print("     |    2 - for 'Student Version' |")
print("     |------------------------------|")
b = input("     | Provide the version you want |")
print("     |------------------------------|")
if b == "1":
    result = task1(0, 0, 0, 0, 0, [], [], [],[])
    progress = result[0]
    Trailer = result[1]
    Retriever = result[2]
    Excluded = result[3]
    outcome = result[4]
    prograss_list = result[5]
    Retriever_list = result[6]
    Excluded_list = result[7]
    Trailer_list = result[8]

    ''' i used this while loo[ for to stop doing task 1 again and again.
    so user can go to through this task avoiding for input numbers again and again *//'''
    while True:
        # this only for user to know what want he do now
        print("     |----------------------------|")
        print("     | Enter the number according |")
        print("     | to the task you want       |")
        print("     |    1 - for 'TASK 1'        |")
        print("     |    2 - for 'TASK 2'        |")
        print("     |    3 - for 'TASK 3'        |")
        print("     |    4 - for 'TASK 4'        |")
        print("     |    5 - for 'END THIS'      |")
        print("     |----------------------------|")
        NUM_input = input("     |    Enter Your MAIN NUM :   - ")
        print("     |----------------------------|")
        # this option will give task1 horizontal histogram
        if NUM_input == "1":
            print('--------------------------------------------------------------\n'
                  'Horizontal Histogram\n')
            print("Progress  ", progress, ":", '*' * progress)
            print("Trailer   ", Trailer, ":", "*" * Trailer)
            print("Retriever ", Retriever, ":", "*" * Retriever)
            print("Excluded  ", Excluded, ":", "*" * Excluded)
            print('''
                                        ''')
            print(outcome, " outcomes in total.")
            print('---------------------------------------------------------------- \n')
            continue
        elif NUM_input == "2":
            # this option will give task1 horizontal hostogram
            list1 = [progress, Trailer, Retriever, Excluded]
            list2 = [[], [], [], []]
            vertical(progress, 0)
            vertical(Trailer, 1)
            vertical(Retriever, 2)
            vertical(Excluded, 3)
            a = max(list1)
            print("Progress Trailing Retriever Excluded")
            for i in range(0, a):
                for x in list2:
                    try:
                        print(" ", x[i], end='       ')
                    except:
                        print(" ", ' ', end='       ')
                print()
            continue
        elif NUM_input == "3":
            # this for task 3
            loops(prograss_list, Trailer_list, Retriever_list, Excluded_list)
            continue
        elif NUM_input == "4":
            '''this for task 4 and i divided it to two parts
            1 - you can read what you entered previous time and you stored results  to text file
            2 - you can print what you entered results  to text file '''
            print("")
            print("     |--------------------------------|")
            print("     |   Enter the number according   |")
            print("     |   1 - for ' READ STORED DATA ' |")
            print("     |   2 - for '  TO STORE DATA  '  |")
            print("     |--------------------------------|")
            sec_sell = input("     |        ENTER YOUR NUMBER       - ")
            print("     |--------------------------------|")
            print("")
            if sec_sell == "1":
                try:
                    file = open(".\\CW.txt")
                    s = file.read()
                    print(s)
                    file.close()
                except:
                    print("     |       File not found       |")
                continue
            elif sec_sell == "2":
                '''from stack overflow ( https://stackoverflow.com/questions/51629294/why-sys-stdout-in-python-doesnt
                -have-default-method-to-restore-to-default-val ) '''
                temp = sys.stdout
                sys.stdout = open(".\\CW.txt", "w")
                loops(prograss_list, Trailer_list, Retriever_list, Excluded_list)
                sys.stdout.close()
                sys.stdout = temp
                continue
        elif NUM_input == "5":
            finish()
            break
        else:
            print("     PLZ ENTER GIVEN NUMBER")
            continue

else:
    task1(0, 0, 0, 0, 0, [], [], [],[])
    finish()
