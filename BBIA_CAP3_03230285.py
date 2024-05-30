# 
# Sonam Dema
# BBI A
# 03230285
#reference
#Your Solution Score: <total sum>
import os

def read_input(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines
    else:
        print(f"Error: File {file_path} not found.")
        return []

def extract_digits(line):
    digits = []
    for char in line:
        if char.isdigit():
            digits.append(char)
    if len(digits) >= 2:
        return int("".join(digits[-2:]))
    return 0

def print_solution(file_path, answer): 
    print(f"The total sum of two-digit numbers from the given input file {file_path} is {answer}")

def solve(lines):
    total_sum = 0 
    for line in lines: 
        two_digit_number = extract_digits(line.strip()) 
        if two_digit_number != 0:
            total_sum += two_digit_number 
    return total_sum

def main():
    input_file_path = "285.txt"  # Replace with your input file name
    lines = read_input(input_file_path)
    answer = solve(lines)
    print_solution(input_file_path, answer)

if __name__ == "__main__":
    main()