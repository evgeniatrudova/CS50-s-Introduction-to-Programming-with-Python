def main():
    # Prompt the user for a time
    time = input("What time is it? ").strip()  # Strip any leading/trailing spaces

    # Check if the input is valid
    try:
        time_in_hours = convert(time)

        if 7.0 <= time_in_hours <= 8.0:
            print("breakfast time")
        elif 12.0 <= time_in_hours <= 13.0:
            print("lunch time")
        elif 18.0 <= time_in_hours <= 19.0:
            print("dinner time")
    except ValueError:
        print("Invalid time format")


def convert(time):
    try:
        hours, minutes = time.split(":")
    except ValueError:
        raise ValueError("Time must be in HH:MM format")

    hours = int(hours)
    minutes = int(minutes)

    return hours + minutes / 60.0

if __name__ == "__main__":
    main()
