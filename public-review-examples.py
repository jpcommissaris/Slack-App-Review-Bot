# Modify this file to get reviews. Any app you want via app ID.
from google_play_scraper import reviews, Sort
from utils.parse_review import parse_review
from utils.post import post_to_slack_webhook


def latest_review(appId: str) -> str: 
  result, _continuation_token = reviews(
      appId,
      lang='en', # defaults to 'en'
      country='us', # defaults to 'us'
      sort=Sort.NEWEST, # defaults to Sort.NEWEST
      count=50, # defaults to 100
      # filter_score_with=5 # defaults to None(means all score)
  )

  if (result): 
    post_to_slack_webhook(parse_review(result[0]))

def latest_bad_review(appId: str) -> str: 
  one_star, _ = reviews(
    appId,
    count=1,
    filter_score_with=1 
  )
  two_star, _ = reviews(
    appId,
    count=1,
    filter_score_with=2 
  )

  if (one_star): 
    post_to_slack_webhook(parse_review(one_star[0]))
  elif (two_star):
    post_to_slack_webhook(parse_review(two_star[0]))
  else:
    post_to_slack_webhook('You have no new bad reviews!')



if __name__ == "__main__":
  latest_bad_review('com.openai.chatgpt')



