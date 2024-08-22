import os
import subprocess
from datetime import datetime, timedelta

# Configure these variables
REPO_PATH = './'
START_DATE = datetime(2024, 1, 1)  # Adjust your start date here
END_DATE = datetime.today()  # Set the end date to today
DAYS_BETWEEN_COMMITS = 5  # Change this to control commit frequency
FILENAME = 'contribution.txt'

def create_commit(date):
    # Touch a file or append to ensure it's modified
    with open(os.path.join(REPO_PATH, FILENAME), 'a') as file:
        file.write(f'Commit on {date.strftime("%Y-%m-%d %H:%M:%S")}\n')
    
    # Add and commit the file with a specific date
    subprocess.run(['git', 'add', FILENAME], cwd=REPO_PATH)
    subprocess.run(['git', 'commit', '--date', date.strftime('%Y-%m-%dT%H:%M:%S'), '-m', f'Commit on {date.strftime("%Y-%m-%d")}'], cwd=REPO_PATH)

def main():
    current_date = START_DATE
    while current_date <= END_DATE:
        create_commit(current_date)
        current_date += timedelta(days=DAYS_BETWEEN_COMMITS)

    # Push the changes to GitHub
    subprocess.run(['git', 'push', 'origin', 'main'], cwd=REPO_PATH)

if __name__ == '__main__':
    main()
