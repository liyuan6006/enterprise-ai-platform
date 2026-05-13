async def get_expense_policy(category):

    policies = {
        "Travel":
            "Travel expenses under $3000 are allowed.",
        "Food":
            "Meals under $200 are allowed.",
        "Entertainment":
            "Entertainment requires manager approval."
    }

    return policies.get(
        category,
        "No policy found."
    )