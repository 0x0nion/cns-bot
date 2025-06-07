async def get_tips_wallets():
    # TODO: DATA from DB

    EVM = "0xA1b2C3d4E5F678901234567890abcdef12345678"
    BTC = "bc1qw508d6qejxtdg4y5r3zarvary0c5xw7k4x3jhd"
    XMR = "47zQ5Vf1VnX8DcTq9kPv1zy4oXMt3M2nLk9gJKdVWy4HVtVygfdoJw5ewvYXqqN7s9VZqqVSTiZ2hFZxYA9DgbxR1pLxg5t"
    return EVM, BTC, XMR


async def get_ads_spot_dates():
    # TODO: DATA from DB

    DATES = [
        "2024-11-22",
        "2024-08-13",
        "2025-02-26",
        "2025-04-04",
        "2024-12-27",
        "2025-06-02",
        "2024-07-18",
        "2025-01-11"
    ]
    return DATES


async def get_ads_price():
    # TODO: $PRICES from DB
    PRICES = ["1:100", "3:300", "6:600", "12:1200"]
    return PRICES


async def get_codes_price():
    # TODO: $PRICES from DB
    PRICES = ["1 DAY:100", "3 DAYS:300", "1 WEEK:600", "1 MONTH:1200", "1 YEAR: 12000"]
    return PRICES