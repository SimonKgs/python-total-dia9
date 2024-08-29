import datetime

mi_hora = datetime.time(19, 9)
ahora = datetime.datetime.now()
print(mi_hora)
print(f'{ahora.hour}:{ahora.minute}:00')


# dates
today = datetime.date(2024, 8, 9)
print(today)

print(today.ctime())

print(today.today())

multidata_date = datetime.datetime(2024, 9, 5, 15, 15, 1, 1)
print(multidata_date)

multidata_date = multidata_date.replace(second=3)

print(multidata_date)


born = datetime.date(1995, 3, 5)
death = datetime.date(2095, 1, 2)

life = death - born

print(life.days)


awake = datetime.datetime(2022, 10, 5, 7, 30)
sleep = datetime.datetime(2022, 10, 5, 21, 15)

time_awake = sleep - awake
print(time_awake.seconds)

minutos = datetime.datetime.now().minute
print(minutos)
