import datetime

current = datetime.datetime.now()
now = current + datetime.timedelta(hours=3)
now_date_full = str(now).split()[0]
now_date_day_month = "-".join(now_date_full.split("-")[1:])
print(now_date_full, now_date_day_month)
print(now.weekday())

print(current.isoformat())
new_date = datetime.datetime.strptime("2023-04-11T14:53:49Z", "%Y-%m-%dT%H:%M:%SZ")
print(new_date.isoformat() + "Z")