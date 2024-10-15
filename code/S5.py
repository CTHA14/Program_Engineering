def find_max_power(cars: list, power: list):
    if not cars or not power or len(cars) != len(power):
        return ("Error", 0)
    max_power = power.index(max(power))
    return (cars[max_power], power[max_power])

cars1 = ["E63s", "RS 6", "M5", "SRT Hellcat"]
power1 = [612, 630, 625, 820]

cars2 = ["Supra", "GT-R", "Impreza WRX", "NSX"]
power2 = [320, 320, 290, 280]

cars3 = ["RAM TRX", "F150 Raptor", "Trackhawk"]
power3 = [1014, 700, 710]

print(find_max_power(cars1, power1))
print(find_max_power(cars2, power2))
print(find_max_power(cars3, power3)) 