# Github Repo link: # https://github.com/Sonam-888/03230285_BIA101_CAPlll
# Sonam Dema
# BBI A
# 03230285
#reference : https://www.youtube.com/watch?v=Uh2ebFW8OYM
# Solution Score: 478243


import os
# Function to read input from a file
def read_input(file_path):
    if os.path.exists(file_path):  #Check if the file exists
        with open(file_path, 'r') as file:    #open the file in read mode
            lines = file.readlines()    #read all lines from the file 
        return lines
    else:
        print(f"Error: File {file_path} not found.")    #print error message if file does not exist
        return []

# Function to extract the last two digits from a string
def extract_digits(line):
    digits = []
    for char in line:    # Iterate over each character in the line
        if char.isdigit():    #check if the character is a digit
            digits.append(char)    # add digit to the list
    if len(digits) >= 2:         # check if there are at least two digits
        return int("".join(digits[-2:]))  # Return the last two digits as an interger
    return 0      # Return 0 if there are less than two digits

# Function to print the solution
def print_solution(file_path, answer): 
    print(f"The total sum of two-digit numbers from the given input file {file_path} is {answer}")

# Function to solve the problem using the extracted lines
def solve(lines):
    total_sum = 0 
    for line in lines: 
        two_digit_number = extract_digits(line.strip()) # Extract two-digit number from the line
        if two_digit_number != 0:  #Check if the extracted number is not 0
            total_sum += two_digit_number   # Add the number to the total sum
    return total_sum

# Main function to execute the program
def main():
    input_file_path = "03230285_BIA101_CAPlll\\285.txt"  
    lines = read_input(input_file_path)  # Read input from the file
    answer = solve(lines)     # Solve the problem
    print_solution(input_file_path, answer)    #Print the solution

if __name__ == "__main__":
    main()        # Run the main function

