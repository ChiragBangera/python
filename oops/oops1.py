class Kettle(object):

    power_source = "electricity"  # class variable

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


milton = Kettle("Milton", 399)
print(milton.price)

milton.price = 499
print(milton.price)


prestige = Kettle("Prestige", 299)
print(prestige.make)


print(
    "Models: {} = {}, {} = {}".format(
        milton.make, milton.price, prestige.make, prestige.price
    )
)

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(milton, prestige))


print(milton.on)
milton.switch_on()
print(milton.on)


Kettle.switch_on(milton)
print(milton.on)

milton.power = 2.3
print(milton.power)
print("switching to atomic power")
Kettle.power_source = "atomic"
milton.power_source = "miltion not atomic"
print(Kettle.power_source)
print(milton.power_source)
print(prestige.power_source)
print(Kettle.__dict__)
print(milton.__dict__)
print(prestige.__dict__)
