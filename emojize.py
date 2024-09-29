emoji_dict = {
    ":thumbs_up:": "👍",
    ":thumbsup:": "👍",
    ":1st_place_medal:": "🥇",
    ":money_bag:": "💰",
    ":smile_cat:": "😸",
}

def main():
    user_input = input("Input: ")

    for code, emoji in emoji_dict.items():
        user_input = user_input.replace(code, emoji)

    print(f"Output: {user_input}")

if __name__ == "__main__":
    main()
