def outing_program():
    # Constants
    MIN_SENIORS = 10
    MAX_SENIORS = 36
    MIN_CARERS = 2
    EXTRA_CARER_THRESHOLD = 24

    # TASK 1: Calculate the cost of the outing
    num_seniors = int(input("Enter the number of senior citizens attending the outing (10-36): "))

    # Validate input
    if num_seniors < MIN_SENIORS or num_seniors > MAX_SENIORS:
        print(f"Error: The number of senior citizens must be between {MIN_SENIORS} and {MAX_SENIORS}.")
        return

    # Determine number of carers needed
    num_carers = MIN_CARERS
    if num_seniors > EXTRA_CARER_THRESHOLD:
        num_carers += 1

    # Determine cost bracket
    if 12 <= num_seniors <= 16:
        hire_cost = 150
        meal_cost = 14.00
        ticket_cost = 21.00
    elif 17 <= num_seniors <= 26:
        hire_cost = 190
        meal_cost = 13.50
        ticket_cost = 20.00
    elif 27 <= num_seniors <= 36:
        hire_cost = 225
        meal_cost = 13.00
        ticket_cost = 19.00

    # Calculate total and per person costs
    total_cost = hire_cost + (meal_cost + ticket_cost) * num_seniors
    cost_per_person = total_cost / num_seniors

    print(f"\nTASK 1: Cost Calculations")
    print(f"Total cost of the outing: ${total_cost:.2f}")
    print(f"Cost per senior citizen: ${cost_per_person:.2f}")

    # TASK 2: Record who is going on the outing and how much has been paid
    attendees = []
    total_collected = 0

    print(f"\nTASK 2: Record Attendance and Payments")

    # Infinite loop for recording attendees
    while True:
        name = input("Enter the name of the attendee: ")
        role = input("Is this person a 'senior' or a 'carer'? ").strip().lower()

        if role == "senior":
            amount_paid = float(input(f"Enter the amount paid by {name}: $"))
            total_collected += amount_paid
            attendees.append((name, amount_paid))
        elif role == "carer":
            attendees.append((name, 0.00))  # Carers do not pay
        else:
            print("Invalid role. Please enter 'senior' or 'carer'.")

        # Ask if more attendees are to be added
        more_attendees = input("Do you want to add another attendee? (yes/no): ").strip().lower()
        if more_attendees != 'yes':
            break

    print("\nList of Attendees and Amounts Paid:")
    for attendee in attendees:
        print(f"{attendee[0]} - ${attendee[1]:.2f}")

    print(f"\nTotal amount collected: ${total_collected:.2f}")

    # TASK 3: Identify break-even point or profit
    print(f"\nTASK 3: Break-even or Profit Analysis")
    if total_collected > total_cost:
        print(f"Profit: ${total_collected - total_cost:.2f}")
    elif total_collected == total_cost:
        print("Break-even: The outing has neither made a profit nor a loss.")
    else:
        print(f"Loss: ${total_cost - total_collected:.2f}")

# Run the program
outing_program()