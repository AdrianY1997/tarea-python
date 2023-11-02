import datetime

now = datetime.datetime.now()
print("Fecha y hora actual:", now)

today = datetime.date.today()
print("Fecha actual:", today)

current_time = datetime.datetime.now().time()
print("Hora actual:", current_time)

delta = datetime.timedelta(days=7)
one_week_later = today + delta
print("Una semana después:", one_week_later)

formatted_date = today.strftime("%Y-%m-%d")
print("Fecha formateada:", formatted_date)

date_str = "2023-11-02"
parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
print("Fecha parseada:", parsed_date)
