
####### TASK 1 ###########
# Calculate number of days between current date and selected date
def get_days_from_today(date: str) -> int:
    """
    Calculate number of days between current date and selected date.
    Args:
        date (str): selected date, from which we want to calculate distance in days.
                    Example: '2025-10-20'
    Returns:
        days (int): number of full days from selected date to current date as integer. 
                    Positive if selected date < current date, negative otherwise.
                    Example: 10
    """

    from datetime import datetime

    try:
        date = datetime.strptime(date, '%Y-%m-%d').date()
    except Exception as e:
         print(f"Wrong data format: {e}.\n"
               "Expected format: YYYY-MM-DD. Example: 2026-12-25")
         return
    else:
        now = datetime.now()
        dist = now - date
        return dist.days



# assert get_days_from_today('2025-10-10') == 380
# assert get_days_from_today('2027-10-10') == -350
# assert get_days_from_today('2027.10.10') == None


####### TASK 2 ###########
def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """
    Returns random numbers from min to max in specified quantity. All numbers will be unique.
    Args:
        min (int): min number, >= 1.
        max (int): max number, <= 1000.
        quantity (int): >= min and <= max.
    
    Returns: 
        rand_nums (list): list of random numbers of specified quantity in range from min to max including.
    """
    if (min < 1 or max > 1000) or (max <= min) or (quantity < 1) or (quantity > max-min):
        print('Min must be >= 1 and Max must be <= 1000. Min must be < Max. Quantity must be >=1 and <= max-min.\n'
              f'Current values: min - {min}, max - {max}, quantity - {quantity}.')
        return []

    import random
    all_nums = [n for n in range(min, max+1)]
    return sorted(random.sample(all_nums, quantity))

# assert len(set(get_numbers_ticket(1,10, 2))) == 2
# assert len(set(get_numbers_ticket(1,10, 9))) == 9
# assert get_numbers_ticket(0,10, 9) == None
# assert get_numbers_ticket(1,1001, 9) == None
# assert get_numbers_ticket(1,10, 11) == None

lottery_numbers = get_numbers_ticket(44, 49, 5)
print("Ваші лотерейні числа:", lottery_numbers)



####### TASK 3 ###########
def normalize_phone(phone_number: str) -> str:
    """
    Normalize phone number to format +380XXXXXXXXX.
    Args:
        phone_number (str): varied format of phone number
    Returns:
        formatted_phone_number (str): formated version of the same phone number in format +380XXXXXXXXX.

    """
    import re
    formatted_phone_number = re.sub(r'[^0-9\+]', "" ,phone_number)
    if re.search(r'^0\d+', formatted_phone_number) and len(formatted_phone_number) == 10:
        formatted_phone_number = '+38' + formatted_phone_number
    elif re.search(r'^3\d+', formatted_phone_number) and len(formatted_phone_number) == 12:
        formatted_phone_number = '+' + formatted_phone_number

    return formatted_phone_number

# assert normalize_phone("    +38(050)123-32-34") == '+380501233234'
# assert normalize_phone("     0503451234") == '+380503451234'
# assert normalize_phone("(050)8889900") == '+380508889900'
# assert normalize_phone("38050-111-22-22") == '+380501112222'
# assert normalize_phone("38050 111 22 11   ") == '+380501112211'

raw_numbers = [
    "067\\t123 4567",
    "(095) <234-5678\\n",
    "+380 44 123 4567",
    "380501234567)*%",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 ?111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)



####### TASK 4 ###########
def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    """
    Congratulations to users for upcoming 7 days.
    Args:
        users (list of dicts): users with birthday dates.
    Returns:
        congrats (list of dicts):  users to congratulate during the upcoming 7 days. Congratulations only on weekdays.
                        If birthday on weekend - we congratulate next weekday.
    """
    from datetime import datetime, date, timedelta
    now = date.today()
    congrats = []
    for user in users:
        name = user.get('name')
        bd = user.get('birthday')
        bd = datetime.strptime(bd, '%Y.%m.%d').date()
        try:
            next_bd = date(year=now.year, month=bd.month, day=bd.day)
        except ValueError:
            next_bd = date(year=now.year, month=bd.month+1, day=1)
        if next_bd < now:
            try:
                next_bd = date(year=now.year+1, month=bd.month, day=bd.day)
            except ValueError:
                next_bd = date(year=now.year+1, month=bd.month+1, day=1)

        if (next_bd - now).days <= 7:
            if next_bd.isoweekday() >= 6:
                next_bd += timedelta(days=8-next_bd.isoweekday())
            congrats.append({'name': name,
                             'congratulation_date': next_bd.strftime('%Y.%m.%d')})

    return congrats

users = [
    # {"name": "John Doe", "birthday": "1985.10.28"},
    {"name": "Jane Smith", "birthday": "1992.02.29"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)



