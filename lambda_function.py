import requests
import pandas as pd
from datetime import datetime, timezone

# Replace these variables with your GitLab details
GITLAB_URL = 'https://gitlab.com'
PROJECT_ID = 'your_project_id'
PRIVATE_TOKEN = 'your_private_token'

# Function to get all branches from the GitLab repo
def get_branches():
    branches = []
    page = 1
    per_page = 100  # GitLab API allows up to 100 items per page

    while True:
        url = f"{GITLAB_URL}/api/v4/projects/{PROJECT_ID}/repository/branches"
        headers = {'PRIVATE-TOKEN': PRIVATE_TOKEN}
        params = {'page': page, 'per_page': per_page}
        response = requests.get(url, headers=headers, params=params)

        # Print the response status code and content for debugging
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.content}")

        # Check if the response is successful
        if response.status_code == 200:
            try:
                branch_page = response.json()
                if not branch_page:
                    break
                branches.extend(branch_page)
                page += 1
            except requests.exceptions.JSONDecodeError as e:
                print(f"JSON Decode Error: {e}")
                break
        else:
            print(f"Failed to fetch branches: {response.status_code}")
            break

    return branches

# Function to calculate days ago from a given date
def days_ago(date_str):
    commit_date = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
    now = datetime.now(timezone.utc)
    delta = now - commit_date
    return delta.days

# Fetch branches and their latest commit details
branches = get_branches()
branch_data = []
for branch in branches:
    branch_name = branch['name']
    commit_date = branch['commit']['committed_date']
    days_since_commit = days_ago(commit_date)
    branch_data.append((branch_name, days_since_commit))

# Sort branches by days ago (more recently committed first)
branch_data.sort(key=lambda x: x[1])

# Create a DataFrame and write to Excel
df = pd.DataFrame(branch_data, columns=['Branch Name', 'Days Ago'])
df.to_excel('branches.xlsx', index=False)
print("Branches have been written to branches.xlsx")
