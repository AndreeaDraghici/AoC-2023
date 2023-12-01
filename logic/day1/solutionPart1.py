def extract_calibration_values(lines):
    total_sum = 0

    for line in lines:
        digits = [char for char in line if char.isdigit()]
        if len(digits) >= 1:
            first_digit = int(digits[0])
            last_digit = int(digits[-1])
            combined_digit = first_digit * 10 + last_digit
            total_sum += combined_digit

    return total_sum


if __name__ == "__main__":
    try:
        with open("../../input/day1/part1/part1Input.txt", "r") as file:
            calibration_input = [line.strip() for line in file.readlines()]

        # Calculate the sum of all calibration values
        result = extract_calibration_values(calibration_input)

        # Print the result
        print(f"Sum of all of the calibration values is: {result}")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
