import requests
import json

def post_to_slack_webhook(webhook_url, text):
    payload = {"text": text}
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        print('Successfully posted', text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    