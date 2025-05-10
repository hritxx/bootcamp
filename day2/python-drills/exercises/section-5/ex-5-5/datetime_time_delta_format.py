from datetime import datetime, timedelta

now = datetime.now()
future = now + timedelta(days=7)

print("Now:", now.strftime("%Y-%m-%d %H:%M"))
print("7 Days Later:", future.strftime("%Y-%m-%d %H:%M"))