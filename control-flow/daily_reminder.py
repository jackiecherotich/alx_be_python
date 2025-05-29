task = input("Enter your task: ")
priority = input("Priority (high/medium/low): " )
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task using match-case
match priority:
    case "high":
        message = f"High-priority task: {task}"
    case "medium":
        message = f"Medium-priority task: {task}"
    case "low":
        message = f"Low-priority task: {task}"
    case _:
        message = f"Unknown priority for task: {task}"

# Adjust the message if the task is time-sensitive
if time_bound == "yes":
    message += " — that requires immediate attention today!"

# Print the reminder three times as a loop-based simulation of urgency
count = 0
while count < 3:
    print(f"Reminder: {message}")
    count += 1