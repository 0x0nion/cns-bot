from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    ADS_BUY = State()
    CODE_BUY = State()