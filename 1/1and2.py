def numberInBuffer(buffer):
    numbers = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    for i, num in enumerate(numbers):
        if num in buffer:
            return i + 1

    return -1


with open("input.txt") as file:
    calibration_sum = 0

    for line in file:
        line = line.rstrip()

        first_digit = None
        last_digit = None
        buffer = ""
        numbers = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]

        for char in line:
            buffer += char
            print(buffer)

            if numberInBuffer(buffer) != -1:
                if first_digit == None:
                    first_digit = numberInBuffer(buffer)
                last_digit = numberInBuffer(buffer)
                buffer = buffer[-1]
            elif char.isnumeric():
                if first_digit == None:
                    first_digit = int(char)
                last_digit = int(char)
                buffer = ""

        calibration_value = first_digit * 10 + last_digit
        calibration_sum += calibration_value

    print(calibration_sum)
