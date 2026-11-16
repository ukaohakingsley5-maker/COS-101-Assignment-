while True:
    print("\n===== PHYSICS FORMULA SOLVER =====")
    print("1. Speed")
    print("2. Force")
    print("3. Density")
    print("4. Pressure")
    print("5. Work Done")

    choice = input("\nPick a formula (1-5): ")

    if choice == "1":
        distance = float(input("Enter distance (m): "))
        time = float(input("Enter time (s): "))
        if time == 0:
            print("Time cannot be zero.")
        else:
            answer = distance / time
            print("Speed =", answer, "m/s")

    elif choice == "2":
        mass = float(input("Enter mass (kg): "))
        acceleration = float(input("Enter acceleration (m/s^2): "))
        answer = mass * acceleration
        print("Force =", answer, "N")

    elif choice == "3":
        mass = float(input("Enter mass (kg): "))
        volume = float(input("Enter volume (m^3): "))
        if volume == 0:
            print("Volume cannot be zero.")
        else:
            answer = mass / volume
            print("Density =", answer, "kg/m^3")

    elif choice == "4":
        force = float(input("Enter force (N): "))
        area = float(input("Enter area (m^2): "))
        if area == 0:
            print("Area cannot be zero.")
        else:
            answer = force / area
            print("Pressure =", answer, "Pa")

    elif choice == "5":
        force = float(input("Enter force (N): "))
        distance = float(input("Enter distance (m): "))
        answer = force * distance
        print("Work Done =", answer, "J")

    else:
        print("Invalid choice! Pick a number from 1 to 5.")
        continue

    again = input("\nDo you want to pick a new formula? (yes/no): ")

    if again.strip().lower() != "yes":
        print("Thank you for using the Physics Solver!")
        break
