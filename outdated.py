def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date_input = input("Date: ").strip()

        try:
            if "/" in date_input:
                month, day, year = date_input.split("/")

                month = int(month)
                day = int(day)
                year = int(year)

                if month < 1 or month > 12 or day < 1 or day > 31:
                    raise ValueError

                print(f"{year:04}-{month:02}-{day:02}")
                break

            else:
                month_name, day_year = date_input.split(" ", 1)
                day, year = day_year.split(", ")

                month = months.index(month_name) + 1

                day = int(day)
                year = int(year)

                if day < 1 or day > 31:
                    raise ValueError

                print(f"{year:04}-{month:02}-{day:02}")
                break

        except (ValueError, IndexError):
            continue

if __name__ == "__main__":
    main()

