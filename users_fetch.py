#!/usr/bin/env python3
"""
Fetch users from https://jsonplaceholder.typicode.com/users
Print Name, Username, Email, City for each user.

Optional filter: only show users whose city starts with a given letter.
"""

import sys
import argparse
import requests


API_URL = "https://jsonplaceholder.typicode.com/users"


def fetch_users():
    try:
        resp = requests.get(API_URL, timeout=10)
    except requests.RequestException as e:
        raise RuntimeError(f"Network error while calling API: {e}") from e

    if resp.status_code != 200:
        raise RuntimeError(f"API returned status code {resp.status_code}")

    try:
        data = resp.json()
    except ValueError as e:
        raise RuntimeError("Failed to parse JSON response") from e

    if not isinstance(data, list) or len(data) == 0:
        raise RuntimeError("API returned empty or unexpected data")

    return data


def format_user(i, user):
    name = user.get("name", "N/A")
    username = user.get("username", "N/A")
    email = user.get("email", "N/A")
    city = user.get("address", {}).get("city", "N/A")

    return (
        f"User {i}:\n\n"
        f"Name: {name}\n\n"
        f"Username: {username}\n\n"
        f"Email: {email}\n\n"
        f"City: {city}\n"
    )


def main():
    parser = argparse.ArgumentParser(description="Fetch and display users from public API")
    parser.add_argument(
        "--city-start",
        "-c",
        metavar="LETTER",
        help="Optional: only print users whose city starts with LETTER (case-insensitive)",
    )
    args = parser.parse_args()

    try:
        users = fetch_users()
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)

    filtered = users
    if args.city_start:
        letter = args.city_start.strip().lower()
        if len(letter) == 0:
            print("Error: --city-start requires a non-empty letter")
            sys.exit(1)
        filtered = [
            u for u in users
            if isinstance(u.get("address", {}).get("city"), str)
            and u["address"]["city"].lower().startswith(letter)
        ]

    if not filtered:
        print("No users matched the filter or API returned no users.")
        sys.exit(0)

    for idx, user in enumerate(filtered, start=1):
        print(format_user(idx, user))
        if idx != len(filtered):
            print("-" * 40)


if __name__ == "__main__":
    main()
