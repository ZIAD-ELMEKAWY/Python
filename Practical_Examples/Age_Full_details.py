#  Your age full details
age = int(input("Enter your age : ").strip())
months = age * 12
weeks = age * 52
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f"You lived for : \n {months:,} months. \n {weeks:,} weeks. \n {days:,} days. \n {hours:,} hours. \n {minutes:,} minutes. \n {seconds:,} seconds.")
