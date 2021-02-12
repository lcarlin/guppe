i = 1
count = 1
while count < 21:
    if i % count != 0:
        i += 1
        count = 1

    count += 1

print(i)