# Mass assign a new project leader to multiple Moco projects
This python script helps to change the project leader of multiple projects in the Moco App.

## How it works
Download this script or clone this repository and replace the {{DOMAIN}} part in the URL and paste your API KEY, which you can get from your Moco Profil. This script uses the Moco API, the documentation can be found: https://github.com/hundertzehn/mocoapp-api-docs/blob/master/README.md#moco-api-documentation

After replacing the mentioned values above, you are asked to enter the ID of the current project leader. The script fetches all assigned projects of this person and asks for the ID of the new project leader. After entering, it replaces the project leader for all the previously fetched projects and confirms it.

## Requirements
You will need
* A Moco Account: https://www.mocoapp.com/
* Python3 installed
* The Python library Requests: https://docs.python-requests.org/en/latest/user/install/
