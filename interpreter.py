def main():
    try:
        expression = input("Expression: ").strip()
        x, operator, z = expression.split()

        x = int(x)
        z = int(z)

        if operator == "+":
            result = x + z
        elif operator == "-":
            result = x - z
        elif operator == "*":
            result = x * z
        elif operator == "/":
            result = x / z
        else:
            print("Invalid operator.")
            return

        print(f"{result:.1f}")

    except ValueError:
        print("Invalid input. Make sure the expression is in the format 'x operator z', where x and z are integers.")


main()

