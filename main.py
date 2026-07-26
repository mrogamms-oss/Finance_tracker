import json
from datetime import datetime, date

#================ NICE DISPLAY =============================#
print("-" * 40)
print("Welcome to Finance Tracker")
print("-" * 40)

#================= NAME OF THE USER ========================#
name = input("Please enter your name: ")


#================ CALCULATING THE BALANCE ==================#
def calculate(name, income, expend):
    balance = income - expend
    if balance <= 1 and expend >= income:
        return (
        f"sorry {name.title()}, so your account now 0.00GHC "
        "\nWarning you are now 0 you spend more than you earned."
        )
    elif balance <= 9:
        return (
            f"Dear {name.title()}, your current balance is "
            f"{balance} GHC.\n This is not enough topup."
        )
    else:
        return (
            f"Dear {name.title()}, your current balance is {balance} GHC."
            )


#=============== SAVE USER FINANCE DATA ====================#
def save(choice):
    if choice.lower() == "yes":
        with open("balance.json", "w") as f:
            json.dump(u_data, f, indent=4)
            
            return (
                "Your Balance and finance data saved successfully."
            )
    else:
        return (
            f"Thanks, {name.title()}, for using Finance Tracker!"
            )

#=============== TO MANAGE USER INPUT ERROR ================#
try:
    income = int(input("Enter your income: "))
except ValueError:
    print("enter number not letter or hyphens")
try:
    expend = int(input("Enter your expenditure: "))
except ValueError:
    print("enter number not letter or hyphens")


balance = income - expend
percentage = balance / income
now = datetime.now()
today = date.today()

#============= USER DICTIONARY TO STORE ====================#
u_data = {
    name.title(): {"Daily income": f"{income}GH cedis",
           "Daily expenditure": f"{expend}GH cedis",
           "saved percentage out of income": f"{percentage*100} %",
           "Date and Time": now.strftime('%H : %M : %S'),
           "Date ": today.strftime('%B %d, %Y')
           }
}

#============= LIKE MAIN ===================================#
message = calculate(name, income, expend)
print(message)
choice = input("Do you want to save your balance? (yes/no): ")
print(save(choice))