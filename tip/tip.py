def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove the '$' and convert to float
    # Example: "$50.00" -> "50.00" -> 50.0
    return float(d.replace("$", ""))


def percent_to_float(p):
    # Remove the '%' and convert to float, then divide by 100
    # Example: "15%" -> "15" -> 15.0 -> 0.15
    return float(p.replace("%", "")) / 100


main()
