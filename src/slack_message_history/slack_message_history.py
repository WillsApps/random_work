#!/usr/bin/env python3
from collections import Counter
from datetime import datetime, timedelta
from os import getenv

from slack_sdk import WebClient

from general_utils.consts import load_env


def top_10_users_by_dm(slack_token: str, start_iso: datetime, end_iso: datetime, exclude_users: list = None):
    """
    Get the top 10 users based on direct message interaction counts within the given time period.
    Only counts messages *from* other users.

    Parameters:
    slack_token (str): Slack API token
    start_iso (datetime): Start of the time period in ISO format
    end_iso (datetime): End of the time period in ISO format
    exclude_users (list): List of usernames to exclude from the top 10 (optional)

    Returns:
    list: Top 10 users with message counts.
    """
    exclude_users = exclude_users or []

    # Initialize Slack Client
    client = WebClient(token=slack_token)

    # Convert datetime to timestamps strings (as expected by API)
    start_time_ts = start_iso.timestamp()
    end_time_ts = end_iso.timestamp()

    # Fetch direct message conversations (DMs)
    response = client.conversations_list(types="im")
    im_channels = response["channels"]

    # To track message counts (from other users)
    message_counts = Counter()

    # Iterate over each DM conversation
    for channel in im_channels:
        other_user_id = channel["user"]

        # Fetch user info to apply the exclusion filter
        user_info = client.users_info(user=other_user_id)
        other_user_name = user_info["user"]["name"]

        # Skip excluded users
        if other_user_name in exclude_users:
            continue

        # Paginate through conversation history
        next_cursor = None
        while True:
            # Fetch message history for this DM, with pagination support
            history = client.conversations_history(
                channel=channel["id"],
                oldest=str(start_time_ts),
                latest=str(end_time_ts),
                limit=100,  # Limit the result size to 100 (Slack's default)
                cursor=next_cursor,  # Use next_cursor for pagination
            )

            # Only count messages sent *from* the other user (not from yourself)
            for message in history["messages"]:
                if message.get("user") == other_user_id:
                    message_counts[other_user_id] += 1

            # Check if more messages are available (pagination)
            next_cursor = history.get("response_metadata", {}).get("next_cursor")
            if not next_cursor:
                break  # Exit the loop when no more pages are available

    # Get the top 10 users based on message count
    top_10_users = message_counts.most_common(10)

    # Convert user IDs to usernames
    users_info = {user["id"]: user["name"] for user in client.users_list()["members"]}

    # Filter only the top 10 users, and ensure we are skipping excluded users
    return [(users_info.get(user_id, "Unknown"), count) for user_id, count in top_10_users]


def main():
    load_env()
    slack_token = getenv("SLACK_USER_TOKEN")
    start_iso = datetime.now() - timedelta(days=180)
    end_iso = datetime.now()
    exclude_users = ["google_calendar"]  # Users to exclude from top 10

    top_users = top_10_users_by_dm(slack_token, start_iso, end_iso, exclude_users)

    # Print the result
    for user, count in top_users:
        print(f"User: {user}, Messages: {count}")


if __name__ == "__main__":
    main()
