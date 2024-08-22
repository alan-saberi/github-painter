# GitHub Contribution Graph Manipulator

This Python script automates the creation of commits to manipulate your GitHub contribution graph. By running this script, you can generate a series of commits over a specified period, allowing you to create patterns or fill in your contribution graph up until today.

## How It Works

The script:
1. Iterates through each day from a specified start date to the current date.
2. Makes a small change to a file (e.g., `contribution.txt`).
3. Commits the change with the commit date set to each specific day.
4. Pushes the changes to GitHub, updating your contribution graph.

## Requirements

- Python 3.x
- Git installed and configured
- A GitHub repository (new or existing)

## Setup

1. **Clone your GitHub repository:**
   ```bash
   git clone https://github.com/alan-saberi/github-painter
   cd github-painter
   ```

## Example
```
REPO_PATH = '/path/to/your/repo'
START_DATE = datetime(2023, 1, 1)
END_DATE = datetime.today()
```

## Disclaimer
This script is intended for personal use and should be used responsibly. Manipulating your GitHub contribution graph can be fun, but please ensure that you are not misleading others or misrepresenting your actual work.

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

