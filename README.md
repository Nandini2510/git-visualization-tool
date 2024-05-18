# Git Repository Analyzer

This Python script allows you to analyze Git repositories within a directory structure and visualize commit activity using Matplotlib.

## Requirements

- Python 3.x
- GitPython library (`pip install GitPython`)
- Matplotlib library (`pip install matplotlib`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/git-repo-analyzer.git
   cd git-repo-analyzer
Install dependencies:
bash

Usage
Run the script to analyze Git repositories:

bash
Copy code
python app.py /path/to/search --email user@example.com --days 30
Replace:

/path/to/search with the root directory containing Git repositories to analyze.
user@example.com with the email address of the author whose commit activity you want to analyze.
30 with the number of days to analyze commits (default: 30 days).

Script Explanation
app.py: Main script for analyzing Git repositories and visualizing commit activity.

Functionality
Analyzes total commits, unique contributors, and commit activity for each repository.
Generates a contribution graph for each repository, showing commit count by contributor email.
