from datetime import datetime
from dateutil.relativedelta import relativedelta

from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards import inline as kb
from states import UserStates
from utils.utils import get_tips_wallets, get_ads_spot_dates, get_ads_price, get_codes_price


# MAIN MENU
async def main_menu_handler(msg: Message | CallbackQuery, state: FSMContext):
    await state.clear()
    text = (f"🚀 WELCOME  🚀\n"
            f"🤖 CHECK'n'SEND BOT\n\n"
            f"📰 ADS || 🔑 CODE || 🎰 FORTUNE || ☕️ COFFEE\n\n"
            f"⬇️ Choose option: ⬇️")

    keyboards = kb.create_mix_ikb(
        btns={
            "📰 BUY ADS SPACE 📰": "buy_ads",
            "🔑 BUY CODE 🔑": "buy_code",
            "🎰 FORTUNE 🎰": "fortune",
            "☕️ COFFEE ☕️": "coffee",
        },
        sizes=(1,)
    )
    if isinstance(msg, Message):
        await msg.answer(text=text, reply_markup=keyboards)
    elif isinstance(msg, CallbackQuery):
        await msg.message.edit_text(text=text, reply_markup=keyboards)


# ADS
async def buy_ads_handler_1(callback: CallbackQuery, state: FSMContext):
    DATES = await get_ads_spot_dates()

    text = f"CHOOSE SPOT PLACE \n\n"
    btns = {}

    for i in range(len(DATES)):
        text += f"{i+1}. Available from {DATES[i]}\n"
        btns[f"ADS SPOT {i+1}"] = f"ads_spot_{i+1}"

    btns["BACK"] = "back"

    keyboards = kb.create_mix_ikb(
        btns=btns,
        sizes=(2, 2, 2, 2, 1)
    )
    await state.set_state(UserStates.ADS_BUY)
    await callback.message.edit_text(text=text, reply_markup=keyboards)


async def buy_ads_handler_2(callback: CallbackQuery, state: FSMContext):
    ads_spot = callback.data.split("_").pop()

    PRICES = await get_ads_price()
    text = f"Choose duration : \n\n"
    btns = {}

    for i in range(len(PRICES)):
        month, price = PRICES[i].split(':')
        btns[f"{month} MONTH = {price} STARS ⭐️"] = f"ads_buy_{ads_spot}_{price}"

    btns["BACK"] = "back"

    keyboards = kb.create_mix_ikb(
        btns=btns,
        sizes=(1,)
    )
    await state.set_state(UserStates.ADS_BUY)
    await callback.message.edit_text(text=text, reply_markup=keyboards)


async def buy_ads_handler_3(callback: CallbackQuery, state: FSMContext):
    # TODO: STARS BUYS
    _, _, spot, price = callback.data.split("_")

    PRICES = await get_ads_price()
    DATES = await get_ads_spot_dates()

    duration = 0

    for i in range(len(PRICES)):
        date_dur, price_check = PRICES[i].split(":")
        if price == price_check:
            duration = int(date_dur)
            break

    from_date = datetime.strptime(DATES[int(spot)-1], "%Y-%m-%d")

    until_date = from_date + relativedelta(months=duration)

    text = (f"THNX YOUR ADS IN QUEUE \n\n"
            f"ADS {spot} WINDOW\n"
            f"DATES:\n"
            f"FROM: {from_date.strftime('%Y-%m-%d')}\n"
            f"UNTIL: {until_date.strftime('%Y-%m-%d')}"
            )
    keyboards = kb.create_mix_ikb(
        btns={
            "BACK": "back"
        },
        sizes=(1,)
    )
    await state.set_state(UserStates.CODE_BUY)
    await callback.message.edit_text(text=text, reply_markup=keyboards)

# CODES
async def buy_codes_handler_1(callback: CallbackQuery, state: FSMContext):

    prices = await get_codes_price()
    text = f"CHOOSE CODE DURATION \n\n"

    btns = {}

    for i in range(len(prices)):
        time, price = prices[i].split(":")
        # text += f"{i+1}. {time} = {price} STARS ⭐️\n"
        btns[f"{time} = {price} STARS ⭐️"] = f"code_{price}"

    btns["BACK"] = "back"

    keyboards = kb.create_mix_ikb(
        btns=btns,
        sizes=(1, )
    )
    await state.set_state(UserStates.CODE_BUY)
    await callback.message.edit_text(text=text, reply_markup=keyboards)


async def buy_codes_handler_2(callback: CallbackQuery, state: FSMContext):
    # TODO: STARS BUY

    code = "YOUR_CODE_HERE"

    text = (f"THNX WRITE YOUR CODE WE DIDNT STORE ANY DATA \n\n"
            f"<code>{code}</code>\n"
            )
    keyboards = kb.create_mix_ikb(
        btns={
            "BACK": "back"

        },
        sizes=(1,)
    )
    await state.set_state(UserStates.CODE_BUY)
    await callback.message.edit_text(text=text, reply_markup=keyboards)


# FORTUNE
async def fortune_handler(callback: CallbackQuery):
    # TODO: from DB
    codes = True

    if codes:
        text = "Today we have $NUM Test Codes\n"
        btns = {
            "GET ONE": "get_free_code",
            "BACK": "back"
        }
    else:
        text = "No codes today\n"
        btns = {
            "BACK": "back"
        }

    keyboards = kb.create_mix_ikb(
        btns=btns,
        sizes=(1, )
    )

    await callback.message.edit_text(text=text, reply_markup=keyboards)


# COFFEE
async def coffe_tips(callback: CallbackQuery):
    EVM, BTC, XMR = await get_tips_wallets()
    text = (f"☕️☕️☕️ TIPS FOR COFFEE: ☕️☕️☕️\n\n"
            f"EVM: <pre>{EVM}</pre>\n"
            f"BTC: <pre>{BTC}</pre>\n"
            f"XMR: <pre>{XMR}</pre>\n"
            
            f""
            )
    keyboards = kb.create_mix_ikb(
        btns={
            "BACK": "back"
        },
        sizes=(1, )
    )

    await callback.message.edit_text(text=text, reply_markup=keyboards)