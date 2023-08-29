from pydantic import BaseModel
from typing import Optional, List, Dict


class User(BaseModel):
    name: Optional[str]
    mail: Optional[str]
    address: Optional[str]


user = User(name='URJ', mail='extrayanat@gmail.com', address='Turon: 59')
print(user)


class Banks(BaseModel):
    name: Optional[str]
    rating: Optional[str]
    opened: Optional[str]


bank = Banks(name='HALK-BANK', rating='top100', opened='20 hours')
print(bank)


class Cards(BaseModel):
    cardholder: User
    which_bank: Banks
    opened: Optional[str]


cards = Cards(cardholder=user, which_bank=bank, opened='20 hours')
print(cards)


class Balance(BaseModel):
    card: Cards
    amount: Optional[int]
    currency: List[Dict[str, int]]


balance = Balance(card=cards, amount=5000, currency=[{'EUR': 6000}])
print(balance)
