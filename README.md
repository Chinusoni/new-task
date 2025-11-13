# Users Fetch Script

Fetches users from the public API https://jsonplaceholder.typicode.com/users and prints selected fields.

Requirements
- Python 3.7+
- requests

Install
1. Create and activate a virtual environment (optional):
   python -m venv venv
   source venv/bin/activate   # on Windows use: venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt

Run
- To print all users:
  python users_fetch.py

- To print only users whose city starts with S:
  python users_fetch.py --city-start S

- To see help:
  python users_fetch.py --help

Notes
- The script handles HTTP errors and empty responses.
- Output is printed in a readable numbered format.
