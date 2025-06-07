from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from handlers.handlers_templates import main_menu_handler, buy_ads_handler_1, buy_codes_handler_1, fortune_handler, \
    coffe_tips, buy_codes_handler_2, buy_ads_handler_2, buy_ads_handler_3
from states import UserStates

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    await main_menu_handler(message, state)


@router.callback_query(F.data.in_(["buy_ads","buy_code","fortune","coffee","back"]))
async def main_callback(callback: CallbackQuery, state: FSMContext):
    match callback.data:
        case "buy_ads":
            await buy_ads_handler_1(callback, state)
        case "buy_code":
            await buy_codes_handler_1(callback, state)
        case "fortune":
            await fortune_handler(callback)
        case "coffee":
            await coffe_tips(callback)
        case "back":
            await main_menu_handler(callback, state)
        case _:
            await main_menu_handler(callback, state)


@router.callback_query(UserStates.CODE_BUY)
async def code_buy(callback: CallbackQuery, state: FSMContext):
    match callback.data:
        case "back":
            await main_menu_handler(callback, state)
        case value if value.startswith("code_"):
            await buy_codes_handler_2(callback, state)
        case _:
            await main_menu_handler(callback, state)


@router.callback_query(UserStates.ADS_BUY)
async def ads_buy(callback: CallbackQuery, state: FSMContext):
    match callback.data:
        case "back":
            await main_menu_handler(callback, state)
        case value if value.startswith("ads_spot_"):
            await buy_ads_handler_2(callback, state)
        case value if value.startswith("ads_buy_"):
            await buy_ads_handler_3(callback, state)
        case _:
            await main_menu_handler(callback, state)