import requests

def get_open_pull_requests(owner, repo):
    # Construct the URL to query the GitHub API for open pull requests
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=open"
    
    # Define headers for the API request
    headers = {
        "Accept": "application/vnd.github.v3+json",
    }
    
    try:
        # Send an HTTP GET request to the GitHub API
        response = requests.get(url, headers=headers)
        
        # Check for HTTP errors and raise an exception if needed
        response.raise_for_status()
        
        # Parse the JSON response and count the number of open pull requests
        return len(response.json())
    except requests.exceptions.RequestException as e:
        # Handle API request errors and print an error message
        print(f"Error querying GitHub API: {e}")
        return -1

def main():
    print("Welcome to Multitudes CLI! Let’s process some Github Data!")
    
    # Prompt the user for the repository owner and name
    owner = input("Who is the repo owner? ")
    repo = input("What is the repo name? ")
    
    # Get the count of open pull requests for the specified repository
    open_pr_count = get_open_pull_requests(owner, repo)
    
    if open_pr_count >= 0:
        # Display the results if the count is non-negative
        print(f"Excellent! Querying {owner}/{repo} for open PRs!")
        print(f"# of open PRs: {open_pr_count}")
    else:
        # Print an error message if there was an issue with the API request
        print("An error occurred. Please check the owner and repo name.")
    
    print("Bye!")

if __name__ == "__main__":
    main()
