import os
import subprocess
from datetime import datetime, timedelta

# Configure these variables
REPO_PATH = './'  # Set to your local repo path
START_DATE = datetime(2024, 1, 1)  # Adjust your start date here
STRING_TO_PAINT = "ALIREZA SABERI"  # The string you want to paint
FILENAME = 'contribution.txt'  # The file to modify for each commit

# Define a simple 5x7 pixel font for capital letters (A-Z) and space
FONT = {
    'A': ["0110", "1001", "1111", "1001", "1001"],
    'B': ["1110", "1001", "1110", "1001", "1110"],
    'C': ["0111", "1000", "1000", "1000", "0111"],
    'D': ["1110", "1001", "1001", "1001", "1110"],
    'E': ["1111", "1000", "1111", "1000", "1111"],
    'F': ["1111", "1000", "1111", "1000", "1000"],
    'G': ["0111", "1000", "1011", "1001", "0111"],
    'H': ["1001", "1001", "1111", "1001", "1001"],
    'I': ["111", "010", "010", "010", "111"],
    'J': ["0011", "0001", "0001", "1001", "0110"],
    'K': ["1001", "1010", "1100", "1010", "1001"],
    'L': ["1000", "1000", "1000", "1000", "1111"],
    'M': ["10001", "11011", "10101", "10001", "10001"],
    'N': ["1001", "1101", "1011", "1001", "1001"],
    'O': ["0110", "1001", "1001", "1001", "0110"],
    'P': ["1110", "1001", "1110", "1000", "1000"],
    'Q': ["0110", "1001", "1001", "0110", "0001"],
    'R': ["1110", "1001", "1110", "1010", "1001"],
    'S': ["0111", "1000", "0110", "0001", "1110"],
    'T': ["11111", "00100", "00100", "00100", "00100"],
    'U': ["1001", "1001", "1001", "1001", "0110"],
    'V': ["10001", "10001", "01010", "01010", "00100"],
    'W': ["10001", "10001", "10101", "11011", "10001"],
    'X': ["10001", "01010", "00100", "01010", "10001"],
    'Y': ["1001", "1001", "0110", "0010", "0010"],
    'Z': ["1111", "0001", "0010", "0100", "1111"],
    ' ': ["000", "000", "000", "000", "000"]
}

def create_commit(date, content):
    with open(os.path.join(REPO_PATH, FILENAME), 'a') as file:
        file.write(content)
    
    subprocess.run(['git', 'add', FILENAME], cwd=REPO_PATH)
    subprocess.run(['git', 'commit', '--date', date.strftime('%Y-%m-%dT%H:%M:%S'), '-m', f'Commit on {date.strftime("%Y-%m-%d")}'], cwd=REPO_PATH)

def main():
    current_date = START_DATE
    for char in STRING_TO_PAINT:
        if char not in FONT:
            continue
        for row in FONT[char]:
            for pixel in row:
                if pixel == "1":
                    create_commit(current_date, f'Commit for {char} on {current_date.strftime("%Y-%m-%d")}\n')
                current_date += timedelta(days=1)
            current_date += timedelta(days=1)  # Add slight space between rows
        current_date += timedelta(days=2)  # Add space between characters

    subprocess.run(['git', 'push', 'origin', 'main'], cwd=REPO_PATH)

if __name__ == '__main__':
    main()
