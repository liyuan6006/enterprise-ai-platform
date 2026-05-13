import os
from pathlib import Path

from openai import AsyncOpenAI

from tools.fraud_tool import (
    check_fraud_risk
)

from tools.policy_tool import (
    get_expense_policy
)


def load_local_env():

    env_path = Path(__file__).resolve().parents[1] / ".env"

    if not env_path.exists():
        return

    for line in env_path.read_text().splitlines():
        line = line.strip()

        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        os.environ.setdefault(
            key.strip(),
            value.strip().strip('"').strip("'")
        )


load_local_env()

client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

class AgentService:

    async def analyze_expense(
        self,
        expense
    ):

        fraud_result = await check_fraud_risk(
            expense
        )

        policy_result = await get_expense_policy(
            expense["category"]
        )

        prompt = f"""
You are a financial AI risk agent.

Expense:
{expense}

Fraud Result:
{fraud_result}

Policy Result:
{policy_result}

Analyze the expense.

Determine:
- fraud risk
- compliance risk
- business risk

Respond professionally.
"""

        response = await client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content":
                        "You are a fintech AI compliance agent."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        return {
            "fraud_result": fraud_result,
            "policy_result": policy_result,
            "ai_analysis":
                response.choices[0]
                .message
                .content
        }
