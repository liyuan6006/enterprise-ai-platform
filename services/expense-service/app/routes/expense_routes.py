from fastapi import APIRouter

from app.schemas.expense_schema import ExpenseCreate
from app.services.expense_service import ExpenseService

router = APIRouter()

expense_service = ExpenseService()

@router.post("/expenses")
async def create_expense(
    expense: ExpenseCreate
):
    return await expense_service.create_expense(expense)

@router.get("/expenses")
async def get_expenses():
    return await expense_service.get_expenses()