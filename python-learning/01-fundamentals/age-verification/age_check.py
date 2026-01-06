def get_valid_age():
    """Prompts user for age until a valid integer is entered."""
    while True:
        try:
            age = int(input("How old are you? "))
            return age
        except ValueError:
            print("That is not a valid integer")


def classify_age(age):
    """Classifies a person as adult or child based on age."""
    if age >= 18:
        return "You are an adult"
    else:
        return "You are a child"


def main():
    """Main function to run the age classification program."""
    age = get_valid_age()
    result = classify_age(age)
    print(result)


if __name__ == "__main__":
    main()