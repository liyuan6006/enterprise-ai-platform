from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from app.database import Base

class Expense(Base):

    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)

    employee_name = Column(String)

    category = Column(String)

    amount = Column(Float)

    description = Column(String)