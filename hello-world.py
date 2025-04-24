# This is a test file. Simply use it to see if you've setup your packages & slack web hook app correctly.
# If you've set everything up correctly. The message should display in your slack channel
import os
from dotenv import load_dotenv
from utils.post import post_to_slack_webhook


load_dotenv()  

webhook_url = os.getenv("SLACK_WEBHOOK_URL")



if __name__ == "__main__":
  # Example usage
  post_to_slack_webhook(
      webhook_url,
      "Hello World: ⭐⭐⭐⭐⭐ 'Love this app!'"
  )
