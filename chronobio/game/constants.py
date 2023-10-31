"""Constants for the game."""

import types

CLIMATE_DISASTER_THRESHOLD = 1_000_000
COMMON_VEGETABLE_LOSS = 50
DAYS_OFF_PER_FIRE = 40
DAYS_OFF_PER_FLOOD = 20
FARM_MONEY_PER_DAY = 30
FIELD_MONEY_PER_DAY = 50
FIELD_PRICE = 10_000
GREENHOUSE_GAS_PER_TRACTOR = 100
LOAN_DURATION_IN_MONTHS = 24
LOAN_INTEREST = 1.1
MAX_LOANS = 10
MAX_NB_PLAYERS = 8
NB_DAYS_TO_HARVEST = 1  # plus one day to sell: 1 means two days off
NB_SOUPS_PER_DAY = 100  # must be a divisor of VEGETABLE_PER_STOCK_DELIVERY
NEEDED_WATER_BEFORE_HARVEST = 10
SALARY_RAISE_FACTOR = 1.01
SERVER_CONNECTION_TIMEOUT = 5
SOUP_PRICES_PER_VETEGABLE = types.MappingProxyType(
    {
        1: 1,
        2: 2,
        3: 4,
        4: 6,
        5: 8,
    },
)
TRACTOR_PRICE = 30_000
VEGETABLE_PRICE = 3_000
VEGETABLE_PER_STOCK_DELIVERY = 2_000
