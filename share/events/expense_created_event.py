from pydantic import BaseModel

class ExpenseCreatedEvent(BaseModel):

    expense_id: int

    employee_name: str

    category: str

    amount: float

    description: str