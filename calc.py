
year = 30
pay = 6000
rate = 10

print("rate:", rate)
total = 0
for i in range(0, year):
    total += pay
    total *= 1 + rate/100
    print("year", i+1, total)
print("amp", total / (year * pay))


def get_amp(rate):
    total = 0
    for i in range(0, year):
        total += pay
        total *= 1 + rate/100
    return total / (year * pay)

for i in range(900, 910):
    r = i / 100
    amp = get_amp(r)
    print("Rate: {}, Amp: {}".format(r, amp))
