
import sys
doghnut=4000
samosa=2000
burger=10000
submarine=20000
kebab=5000
choice_list = ['m', 't', 'w', 'q']
while True:
    choice= input("Enter 'm' for Monday, 't' for Tuesday, 'w' for Wednesday, 'q' to quit: ")
    choice = choice.lower()
    if choice not in choice_list:
        print("Invalid choice. Please select: 'm' for Monday, 't' for Tuesday, 'w' for Wednesday, 'q' to quit.")
        continue
    else:
        if choice.lower()=='m':
            print("Mondays are for doughnuts and submarines")
            subchoice_list = ['d', 's']
            while True:
                subchoice = input("Enter 'd' for doughnut, 's' for submarine, 'b' to go back: ")
                if subchoice.lower()=='d':
                    print("The price of doughnuts is: %d" % doghnut)
                    break
                elif subchoice.lower()=='s':
                    print("Our sweet submarine price is: %d" % submarine)
                    break
                elif subchoice.lower() == 'b':
                    break
                else:
                    print("Invalid choice. Please select: 'd' for doughnut, 's' for submarine, 'b' to go back.")
                    continue

        if choice.lower()=='t':
            print("The second day of the week is better with samosas and burgers")
            subchoice_list=['sa','b']
            while True:
                subchoice =input("Enter 'sa' for samosa, 'b' for burger, 'b' to go back: ")
                if subchoice.lower()=='sa':
                    print("Samosa price is: %d" % samosa)
                    break
                elif subchoice.lower()=='b':
                    print("We have chicken burgers and their price today is: %d" % burger)
                    break
                elif subchoice.lower() == 'b':
                    break
                else:
                    print("Invalid choice. Please select: 'sa' for samosa, 'b' for burger, 'b' to go back.")
                    continue

        if choice.lower()=='w':
            print("Kebab day is today")
            subchoice_list=['k']
            while True:
                subchoice = input("Enter 'k' for kebab, 'b' to go back: ")
                if subchoice.lower()=='k':
                    print("Wednesdays are for kebabs")
                    print("The price of kebab today is: %d" % kebab)
                    break
                elif subchoice.lower() == 'b':
                    break
                else:
                    print("Invalid choice. Please select: 'k' for kebab, 'b' to go back.")
                    continue

        if choice.lower()=='q':
            confirm = input("Are you sure you want to quit? Type 'yes' or 'no': ")
            if confirm.lower()=='yes':
                print("We will be happy to serve you next time.")
                break
            elif confirm.lower()=='no':
                continue
            else:
                print("Invalid choice. Please select: 'yes' or 'no'.")
                continue



#Converting the snack_price function to a stand alone program.It requires removal of the definition of the price and executing
#it using Python in a terminal. Path to the file is provided in double quotes.

#TERMINAL REPRESENTATION
            
PS C:\Users\msaim\Downloads\Functions-in-python> python ./gulo_snack.py ".C:/Users/msaim/Downloads/Functions-in-python" " C:/Users/msaim/Downloads/Functions-in-python/glo.txt"
Enter 'm' for Monday, 't' for Tuesday, 'w' for Wednesday, 'q' to quit: M
Mondays are for doughnuts and submarines
Enter 'd' for doughnut, 's' for submarine, 'b' to go back: D
The price of doughnuts is: 4000
Enter 'm' for Monday, 't' for Tuesday, 'w' for Wednesday, 'q' to quit: q
Are you sure you want to quit? Type 'yes' or 'no': yes
We will be happy to serve you next time.

