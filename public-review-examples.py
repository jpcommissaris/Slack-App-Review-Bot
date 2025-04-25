# Modify this file to get reviews. Any app you want via app ID.
from google_play_scraper import reviews, Sort
from utils.parse import parse_review, parse_many_reviews
from utils.post import post_to_slack_webhook
from datetime import datetime, timedelta


def latest_review(appId: str) -> str:
    result, _continuation_token = reviews(
        appId,
        lang="en",  # defaults to 'en'
        country="us",  # defaults to 'us'
        sort=Sort.NEWEST,  # defaults to Sort.NEWEST
        count=50,  # defaults to 100
        # filter_score_with=5 # defaults to None(means all score)
    )

    if result:
        post_to_slack_webhook(parse_review(result[0]))


def latest_bad_review(appId: str) -> str:
    one_star, _ = reviews(appId, count=1, filter_score_with=1)
    two_star, _ = reviews(appId, count=1, filter_score_with=2)

    if one_star:
        post_to_slack_webhook(parse_review(one_star[0]))
    elif two_star:
        post_to_slack_webhook(parse_review(two_star[0]))
    else:
        post_to_slack_webhook("You have no new bad reviews!")


def top_reviews(appId: str, score: int = None) -> str:
    top_reviews, _ = reviews(
        appId, count=5, sort=Sort.MOST_RELEVANT, filter_score_with=score
    )
    manyReviews = parse_many_reviews(
        top_reviews,
        title=f'🌟 Top reviews of rating {score if score else '1-5'}" 🌟\n\n',
        empty_msg="No reviews found.",
    )
    post_to_slack_webhook(manyReviews)


def reviews_with_keyword_time(
    appId: str, count: int = 10, days: int = 1, keyword: str = None, score=None
) -> str:
    result, _ = reviews(appId, count=count, sort=Sort.NEWEST, filter_score_with=score)

    filtered_reviews = []
    cutoff_date = datetime.now() - timedelta(days=days)

    # Filter reviews for date & keyword
    for review in result:
        review_date = datetime.strptime(review["at"].strftime("%Y-%m-%d"), "%Y-%m-%d")
        print(review_date, cutoff_date)
        if (
            not keyword or (keyword.lower() in review["content"].lower())
        ) and review_date >= cutoff_date:
            filtered_reviews.append(review)

    # max
    manyReviews = parse_many_reviews(
        filtered_reviews,
        title=f'🌟 Top reviews in the last {days} days with keyword "{keyword}" 🌟\n\n',
        max_reviews=5,
        empty_msg='No reviews found with keyword "{keyword}" in the last {days} days.',
    )
    post_to_slack_webhook(manyReviews)


if __name__ == "__main__":
    # latest_bad_review('com.openai.chatgpt')
    # reviews_with_keyword_time(
    #     "com.quicken.acme", count=1000, days=30, keyword="finance"
    # )
    top_reviews("com.quicken.acme", score=5)
