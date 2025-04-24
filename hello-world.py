# This is a test file. Simply use it to see if you've setup your packages & slack web hook app correctly.
# If you've set everything up correctly. The message should display in your slack channel
from utils import post





if __name__ == "__main__":
  # Example usage
  post.post_to_slack_webhook(
      "Hello World: ⭐⭐⭐⭐⭐ 'Love this app!'"
  )
