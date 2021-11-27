def main():
    create_day()


# Creates the python-template for the day in question + files for storing input and test input
def create_day():
    print("Create templates for day number: ")
    day_num = input()
    day = f"day{day_num}"

    day_contents = (f"from adv_utils import read_file#, string_to_ints\n"
                    f"\n"
                    f"\n"
                    f"def main():\n"
                    f"    print(f\"day {day_num} part 1: {{part1()}}\")\n"
                    f"    print(f\"day {day_num} part 2: {{part2()}}\")\n"
                    f"\n"
                    f"\n"
                    f"def part1():\n"
                    f"    lines = read_file(\"input/{day}_test.txt\", \"lines\")\n"
                    f"    return -1\n"
                    f"\n"
                    f"\n"
                    f"def part2():\n"
                    f"    lines = read_file(\"input/{day}_test.txt\", \"lines\")\n"
                    f"    return -1\n"
                    f"\n"
                    f"\n"
                    f"if __name__ == \"__main__\":\n"
                    f"    main()\n"
                    f"\n")
    f = open(f"{day}.py", "w")
    f.write(day_contents)
    f.close()

    open(f"input/{day}.txt", "x")
    open(f"input/{day}_test.txt", "x")


# Reads a file and returns its contents depending on the output type
# lines: every line as a string
# lines + int: every line converted to int-lists
# int: the first line as an int-list
# int + sorted: the first line as a sorted int-list
def read_file(file_name, output_type):
    f = open(file_name, "r")
    if "lines" in output_type:
        lines = f.readlines()
        if "int" in output_type:
            int_lines = [string_to_ints(line) for line in lines]
            return int_lines
        else:
            return lines
    elif "int" in output_type:
        ints = string_to_ints(f.readline())
        if "sorted" in output_type:
            ints.sort()
            return ints
        else:
            return ints


# Turns a string with comma separated integers into a list of integers
def string_to_ints(string):
    num_strings = string.split(",")
    return [int(num) for num in num_strings]


if __name__ == "__main__":
    main()
