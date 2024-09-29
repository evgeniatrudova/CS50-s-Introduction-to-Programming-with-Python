def convert(text):
    """Convert emoticons to emoji."""
    # Replace :) with 🙂 and :( with 🙁
    text = text.replace(':)', '🙂')
    text = text.replace(':(', '🙁')
    return text

def main():
    """Prompt user for input and convert emoticons."""
    user_input = input("Enter text: ")
    result = convert(user_input)
    print(result)

# Call the main function
if __name__ == "__main__":
    main()
