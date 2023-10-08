import requests

def get_open_pull_requests(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=open"
    
    headers = {
        "Accept": "application/vnd.github.v3+json",
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return len(response.json())
    else:
        return -1

def main():
    print("Welcome to Multitudes CLI! Let's process some Github Data!")
    owner = input("Who is the repo owner? ")
    repo = input("What is the repo name? ")
    
    open_pr_count = get_open_pull_requests(owner, repo)
    
    if open_pr_count >= 0:
        print(f"Excellent! Querying {owner}/{repo} for open PRs!")
        print(f"# of open PRs: {open_pr_count}")
    else:
        print("Error querying GitHub API. Please check the owner and repo name.")
    
    print("Bye!")

if __name__ == "__main__":
    main()
