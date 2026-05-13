from pydantic import BaseModel

class ExpenseCreate(BaseModel):

    employee_name: str

    category: str

    amount: float

    description: str