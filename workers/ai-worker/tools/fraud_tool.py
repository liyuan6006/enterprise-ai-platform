async def check_fraud_risk(expense):

    suspicious_keywords = [
        "casino",
        "bitcoin",
        "gift card",
        "crypto",
        "wire transfer"
    ]

    description = expense["description"].lower()

    for keyword in suspicious_keywords:

        if keyword in description:

            return {
                "fraud_detected": True,
                "reason": f"Matched keyword: {keyword}"
            }

    if expense["amount"] > 5000:

        return {
            "fraud_detected": True,
            "reason": "High amount transaction"
        }

    return {
        "fraud_detected": False,
        "reason": "No suspicious patterns"
    }