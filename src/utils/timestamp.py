from datetime import datetime

def gen_timestamp():
    dt = datetime.now()

    if dt.hour < 18:
        return f"[#F5F2E3]{dt.strftime("%d/%m/%y")} [#FCBF49]☼[#F5F2E3] {dt.strftime("%H:%M:%S")}"
    else:
        return f"{dt.strftime("%d/%m/%y")} ☾ {dt.strftime("%H:%M:%S")}"