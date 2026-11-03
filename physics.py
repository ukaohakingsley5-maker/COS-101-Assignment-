# PHYSICS FORMULA SOLVER
# A program that solves 5 physics formulas

print("===== PHYSICS FORMULA SOLVER =====")

print("1. Final Velocity: v = u + at")
print("2. Distance: s = ut + 0.5at^2")
print("3. Force: F = ma")
print("4. Weight: W = mg")
print("5. Power: P = W/t")

choice = int(input("\nChoose a formula (1-5): "))

if choice == 1:
    u = float(input("Enter initial velocity (u): "))
    a = float(input("Enter acceleration (a): "))
    t = float(input("Enter time (t): "))

    v = u + a * t

    print("Final velocity =", v, "m/s")

elif choice == 2:
    u = float(input("Enter initial velocity (u): "))
    a = float(input("Enter acceleration (a): "))
    t = float(input("Enter time (t): "))

    s = u * t + 0.5 * a * t**2

    print("Distance travelled =", s, "m")

elif choice == 3:
    m = float(input("Enter mass (m): "))
    a = float(input("Enter acceleration (a): "))

    F = m * a

    print("Force =", F, "N")

elif choice == 4:
    m = float(input("Enter mass (m): "))
    g = float(input("Enter gravitational acceleration (g): "))

    W = m * g

    print("Weight =", W, "N")

elif choice == 5:
    W = float(input("Enter work done (W): "))
    t = float(input("Enter time (t): "))

    if t == 0:
        print("Error: Time cannot be zero.")
    else:
        P = W / t

        print("Power =", P, "W")

else:
    print("Invalid choice. Please select 1 to 5.")