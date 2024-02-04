import datetime

def get_timestamp():
    now = datetime.datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    if now.hour > 18 or now.hour < 5:
        return f"{date} 🌙 {time}"
    else: 
        return f"{date} ☀️ {time}"