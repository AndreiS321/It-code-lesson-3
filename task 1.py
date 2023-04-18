LOW_TEMP_MESSAGE = "Холодно, лучше остаться дома"
day = 18
month = 4
temperature = -1
print(f"Сегодня {day:>02}.{month:>02}. На уличе {temperature} градусов")
if temperature <= 0:
    print(LOW_TEMP_MESSAGE)
