# Counter-CLI
CLI that extracts data from GitHub and counts the number of open pull requests for a given repository owner and name

### Installation

1. Install Python from [python.org](https://www.python.org/downloads/).
2. Install the `requests` library by running `pip install requests`.

### Usage

1. Clone this repository or download the `github_pr_counter.py` file.
2. Open your terminal and navigate to the directory containing `github_pr_counter.py`.
3. Run the CLI by executing the following command:
4. 4. Follow the prompts to enter the repository owner and name.
5. The script will query GitHub and display the number of open pull requests.

### Example
$ python github_pr_counter.py
Welcome to Multitudes CLI! Let’s process some Github Data!
Who is the repo owner?
microsoft
What is the repo name?
TypeScript
Excellent! Querying microsoft/Typescript for open PRs!
of open PRs: 265


### Note
- Be cautious about the rate limit on the GitHub API.

