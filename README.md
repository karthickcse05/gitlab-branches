# gitlab-branches
repo to list all active branches in gitlab repo

Install Required Libraries: Ensure you have the necessary libraries installed. You can install them using pip if you haven't already:

pip install requests pandas openpyxl
Fetch Branches from GitLab: Use the GitLab API to get the list of branches and their latest commit details.

Sort Branches by Commit Date: Sort the branches based on the date of the latest commit.

Write to Excel: Use pandas to write the sorted data to an Excel file.

Explanation :
Pagination Handling: The script now includes a loop to handle pagination. It fetches branches page by page until no more branches are returned.
Parameters for Pagination: The params dictionary includes page and per_page parameters to control pagination.
Branch Aggregation: The branches from each page are aggregated into a single list.
Get Branches:

The get_branches function makes a GET request to the GitLab API to fetch all branches of the specified project.
The PRIVATE-TOKEN header is used for authentication.
Calculate Days Ago:

The days_ago function calculates the number of days between the current date and the commit date.
Fetch and Process Data:

The script fetches the branches and their latest commit details.
It then calculates the days since the last commit for each branch and stores this information in a list.
Sort and Write to Excel:

The branches are sorted based on the days since the last commit.
A pandas DataFrame is created and written to an Excel file named branches.xlsx.
