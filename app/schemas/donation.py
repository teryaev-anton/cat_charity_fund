from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field


class DonationBase(BaseModel):
    """Базовый класс для схем пожервования"""
    full_amount: int = Field(..., gt=0)
    comment: Optional[str]

    class Config:
        extra = Extra.forbid


class DonationCreate(DonationBase):
    """Схема для создания пожертвования"""
    pass


class DonationDBPartial(DonationBase):
    """Схема для получения своих пожертвований из БД"""
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationDBFull(DonationDBPartial):
    """Схема для получения всех пожертвований из БД"""
    user_id: Optional[int]
    invested_amount: int
    fully_invested: bool
    close_date: datetime = Field(None)
