from backend.fake_review_detector import detect_fake_review

def test_fake_review():
    text = "Best product ever"
    label, confidence = detect_fake_review(text)
    assert label in ["fake", "genuine"]
    assert 0 <= confidence <= 1
