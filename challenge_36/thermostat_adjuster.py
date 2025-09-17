def adjust_thermostat(current_temp, target_temp):
    if current_temp < target_temp:
        return "heat"
    elif current_temp > target_temp:
        return "cool"
    else:
        return "hold"

print("\n" + adjust_thermostat(65, 70))
print("\n" + adjust_thermostat(75, 70))
print("\n" + adjust_thermostat(70, 70))