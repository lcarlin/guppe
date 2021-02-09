idade = int(input("Entre com a Idade :-> "))
msg = ""

if 5 <= idade <= 7:
    msg = "Infantil A"
elif 8 <= idade <= 10:
    msg = "Infantil B"
elif 11 <= idade <= 13:
    msg = "JUvenil A"
elif 14 <= idade <= 17:
    msg = "Juvenbil B"
elif idade >= 18:
    msg = "Senior "
else:
    msg = "Muito Jovem"

print(msg)