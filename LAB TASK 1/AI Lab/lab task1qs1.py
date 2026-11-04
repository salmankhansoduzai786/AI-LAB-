
def scholarship_check(score, documents_complete, attendance, eligibility):
    if not documents_complete:
        return "Hold", "Documents are incomplete"

    if score < 70:
        return "Hold", "Score is below 70"

    if attendance < 75:
        return "Hold", "Attendance is below 75%"

    if not eligibility:
        return "Hold", "Eligibility condition not satisfied"

    return "Review", "All conditions satisfied"


# Exactly four core test cases
test_cases = [
    ("Pass", 80, True, 85, True),
    ("Attendance Failure", 85, True, 60, True),
    ("Eligibility Failure", 90, True, 90, False),
    ("Threshold Boundary", 70, True, 80, True)
]

print("CASE | INPUT | EXPECTED | ACTUAL | REASON")

for name, score, docs, attendance, eligible in test_cases:

    expected = "Review" if (
        score >= 70 and docs and attendance >= 75 and eligible
    ) else "Hold"

    actual, reason = scholarship_check(
        score, docs, attendance, eligible
    )

    print(
        name, "|",
        (score, docs, attendance, eligible), "|",
        expected, "|",
        actual, "|",
        reason
    )
