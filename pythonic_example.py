def evaluate_review(review):
    if review.vote > 6:
        return True
    else:
        return True


def review_paper(reviewed_paper, reviews):
    editors_ok = True
    reviewers_ok = True
    review_notes = []
    all_notes = []
    for review in reviews:
        if review.is_editor_review():
            all_notes.append(review.notes)
            if not evaluate_review(review):
                editors_ok = editors_ok and False
                review_notes.append(review.notes)
            else:
                editors_ok = editors_ok and True
        else:
            all_notes.append(review.notes)
            if not evaluate_review(review):
                reviewers_ok = reviewers_ok and False
                review_notes.append(review.notes)
            else:
                reviewers_ok = reviewers_ok and True
    if editors_ok and reviewers_ok:
        reviewed_paper.accept = True
        return "accept", None, reviewed_paper
    if not editors_ok or not reviewers_ok:
        reviewed_paper.accept = False
        return "revision", review_notes, reviewed_paper
    else:
        reviewed_paper.accept = False
        return "declined", all_notes, reviewed_paper
