from datetime import datetime, timedelta

def date_range(start, end):
    delta = end - start  # as timedelta
    days = [start + timedelta(days=i) for i in range(delta.days + 1)]
    days = [{"date": x, "day_of_the_week": x.strftime('%A')} for x in days]
    return days

start_date = datetime.now()
end_date = datetime(2022, 12, 31)

print(date_range(start_date, end_date))