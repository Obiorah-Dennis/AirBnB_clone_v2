def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return None
    total = sum(numbers)
    average = total / len(numbers)
    return average


def main():
    """Entry point of the program."""
    data = [2, 4, 6, 8, 10]
    result = calculate_average(data)
    print(f"The average is: {result}")


if __name__ == '__main__':
    main()

