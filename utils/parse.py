from typing import TypedDict, Optional
from datetime import datetime


class RawReview(TypedDict):
    reviewId: str
    userName: str
    userImage: Optional[str]
    content: str
    score: int
    thumbsUpCount: int
    reviewCreatedVersion: Optional[str]
    at: datetime
    replyContent: Optional[str]
    repliedAt: Optional[datetime]


def parse_review(review: RawReview) -> str:
    stars = "⭐" * review["score"] + "☆" * (5 - review["score"])
    created_at = review["at"].strftime("%b %d, %Y %I:%M %p")
    version = review.get("reviewCreatedVersion")
    version_line = f"📱 Version: {version}" if version else ""
    important = "🚨 " if int(review["score"]) == 1 else ""

    return (
        "-----\n"
        f"*{review['userName']}* left a review:\n\n"
        f"> {review['content']}\n\n"
        f"{important}{stars} ({review['score']}/5)   👍 {review['thumbsUpCount']} likes {important}\n"
        f"🕓 {created_at}\n"
        f"{version_line}\n"
        "-----"
    )


def parse_many_reviews(
    reviews: RawReview,
    title: str = "Many reviews below:",
    max_reviews: int = 10,
    empty_msg: str = "No reviews found",
) -> str:
    # max
    filtered_reviews = reviews[:max_reviews]
    if filtered_reviews:
        reviewJoin = title
        for review in filtered_reviews:
            reviewJoin += parse_review(review) + "\n\n"
    else:
        reviewJoin = "No reviews found"
    return reviewJoin
