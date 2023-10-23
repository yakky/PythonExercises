class User:
    name
    email
    role


class Review:
    vote
    reviewer
    notes


class EditorReview:
    vote
    editor
    notes


class Paper:
    title
    content
    author


def evaluate_review(review):
    return review.vote > 6


def review_paper(reviewed_paper, reviews):
    votes = [
        (evaluate_review(review), hasattr(review, "editor"), review.notes)
        for review in reviews
    ]
    editors_ok = all(vote[0] for vote in votes if vote[1])
    reviewers_ok = all(vote[0] for vote in votes if not vote[1])
    if editors_ok and reviewers_ok:
        reviewed_paper.accept = True
        return "accept", None, reviewed_paper
    if not editors_ok or not reviewers_ok:
        reviewed_paper.accept = False
        return "revision", [vote[2] for vote in votes if not vote[1]], reviewed_paper
    else:
        reviewed_paper.accept = False
        return "declined", [vote[2] for vote in votes], reviewed_paper


paper = Paper()
submitted_reviews = [Review(), EditorReview(), Review(), EditorReview()]
status, notes, paper = review_paper(paper, submitted_reviews)
