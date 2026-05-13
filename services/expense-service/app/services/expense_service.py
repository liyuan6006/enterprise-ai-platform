from sqlalchemy import select

from app.database import AsyncSessionLocal
from app.models.expense import Expense

from app.messaging.kafka_producer import kafka_producer

class ExpenseService:

    async def create_expense(self, request):

        async with AsyncSessionLocal() as session:

            expense = Expense(
                employee_name=request.employee_name,
                category=request.category,
                amount=request.amount,
                description=request.description
            )

            session.add(expense)
            print("STEP 1")
            await session.commit()

            await session.refresh(expense)

            event = {
                "expense_id": expense.id,
                "employee_name": expense.employee_name,
                "category": expense.category,
                "amount": expense.amount,
                "description": expense.description
            }
            print("STEP 2")
            await kafka_producer.publish(
                "expense-created",
                event
            )
            print("STEP 3")
            return {
                "id": expense.id,
                "status": "created"
            }
            print("STEP 4")

    async def get_expenses(self):

        async with AsyncSessionLocal() as session:

            result = await session.execute(
                select(Expense)
            )

            expenses = result.scalars().all()

            return expenses
