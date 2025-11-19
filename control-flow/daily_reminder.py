# A python program that reminds a user of his or her tasks at hand.


# get user's input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


# processing the task based on priority and time sensitivity
match priority:
    case "high":
        string = f"Reminder: '{task}' is a {priority} priority task"
    case "medium":
        string = f"Reminder: '{task}' is a {priority} priority task"
    case "low":
        string = f"Reminder: '{task}' is a {priority} priority task"
    case _:
        print("Reminder: the priority you typed doesn't exist in the software.")
        quit()


# check if the reminder is time-bound and address the user
if time_bound == "yes":
    print(f"{string} that requires your immediate attention today.")
elif time_bound == "no":
    print(f"{string}. Consider completing it when you have free time.")
else:
    print("Incorrect time-bound type selected. Enjoy!")
