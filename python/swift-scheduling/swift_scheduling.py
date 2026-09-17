"""Convert delivery date descriptions to actual delivery dates"""

# pylint: disable=missing-function-docstring

from datetime import datetime, date, time, timedelta
import re

def next_workday(day):
    weekday = day.weekday()
    return day + timedelta(days=0 if weekday < 5 else 7 - weekday)


def previous_workday(day):
    weekday = day.weekday()
    return day - timedelta(days=0 if weekday < 5 else weekday - 4)
    

def delivery_date(start, description):
    start_dt = datetime.fromisoformat(start)
    start_d = start_dt.date()

    if description == 'NOW':  # due two hours after start
        due_dt = start_dt + timedelta(hours=2)
        
    elif description == 'ASAP':  # due 5pm if before 1pm, else 1pm next day
        if start_dt.time() < time(13):
            due_dt = datetime.combine(start_d, time(hour=17))
        else:
            due_dt = datetime.combine(start_d + timedelta(days=1), time(hour=13))
            
    elif description == 'EOW':  # due 5pm Friday if Mon-Wed, else 8pm Sunday
        wkday_num = start_d.weekday()
        if wkday_num <= 2:
            due_dt = datetime.combine(start_d + timedelta(days=4 - wkday_num), time(hour=17))
        else:
            due_dt = datetime.combine(start_d + timedelta(days=6 - wkday_num), time(hour=20))

    elif match := re.fullmatch(r'(\d+)M', description):  # due 8am on first workday of target month
        due_month = int(match.group(1))
        due_year = start_d.year if start_d.month < due_month else start_d.year + 1
        due_date = next_workday(date(due_year, due_month, 1))
        due_dt = datetime.combine(due_date, time(hour=8))

    elif match := re.fullmatch(r'Q(\d+)', description):  # due 8am on last workday of target quarter
        due_quarter = int(match.group(1))
        due_month = due_quarter * 3
        due_year = start_d.year if start_d.month <= due_month else start_d.year + 1
        next_month = due_month % 12 + 1
        next_year = due_year + (due_month == 12)
        due_date = previous_workday(date(next_year, next_month, 1) - timedelta(days=1))
        due_dt = datetime.combine(due_date, time(hour=8))

    else:
        raise ValueError('invalid delivery description')

    return due_dt.isoformat()
