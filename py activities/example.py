name = "Carmela"
age = 21
aged = age + 5
height_cm = 149.86
height_m = height_cm / 100
qoute = "Hello World"

steps = [2045, 778, 1803, 479, 5020, 1340, 1204]
steps_sum = 0
for n in steps:
    steps_sum += n
steps_avg = steps_sum / len(steps)

prices = [250, 200, 100, 50, 20]
prices_sum = 0
for n in prices:
    prices_sum += n

print("Welcome to the Personal Data Analyzer")
print("Hello, %s!" % name)
print("\n")

print("---- Personal Data Report ----")
print("Name: %s" % name)
print("Age: %d (In 5 years: %d)" % (age, aged))
print("Height: %f (%f cm)" % (height_cm, height_m))
print('Qoute: "%s"' % qoute)
print("\n")

print("Average Steps This Week: %s" % steps_avg)
print("Total Expenses: $%s" % prices_sum)