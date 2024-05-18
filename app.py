import os
import argparse
import git
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


class GitRepoStats:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.repo = git.Repo(repo_path)

    def total_commits(self):
        return len(list(self.repo.iter_commits()))

    def unique_contributors(self):
        return len(
            set(commit.author.email for commit in self.repo.iter_commits()))

    def commit_activity(self, days, author_email):
        since_date = (datetime.now() - timedelta(days=days)).isoformat()
        commits = list(self.repo.iter_commits(since=since_date))
        activity = {commit.author.email: 0 for commit in commits if
                    commit.author.email == author_email}
        for commit in commits:
            activity[commit.author.email] += 1
        return activity


def find_git_repos(directory):
    git_repos = []
    for root, dirs, files in os.walk(directory):
        if '.git' in dirs:
            git_repos.append(root)
    return git_repos


def main():
    parser = argparse.ArgumentParser(
        description='Find git repositories within a directory structure and '
                    'analyze commits by author.')
    parser.add_argument('directory', type=str,
                        help='The root directory to search for Git '
                             'repositories.')
    parser.add_argument('--email', type=str, required=True,
                        help='Email address of the author to analyze commits.')
    parser.add_argument('--days', type=int, default=30,
                        help='Number of days to go back when analyzing '
                             'commits (default: 30).')
    args = parser.parse_args()
    directory = args.directory
    author_email = args.email
    days = args.days
    git_repos = find_git_repos(directory)

    if git_repos:
        print("Found Git repositories in the following directories:")
        for repo_path in git_repos:
            print(repo_path)
            stats = GitRepoStats(repo_path)
            activity = stats.commit_activity(days, author_email)
            print(f"Commit activity by {author_email} (last {days} days):")
            for email, count in activity.items():
                print(f"- {email}: {count} commits")

            # Plotting Contribution Graph
            plt.figure(figsize=(10, 5))
            plt.bar(activity.keys(), activity.values(), color='green')
            plt.xlabel('Contributor Email')
            plt.ylabel('Commit Count')
            plt.title(f'Contribution Graph for {author_email}')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
    else:
        print("No Git repositories found in the specified directory.")


if __name__ == "__main__":
    main()
