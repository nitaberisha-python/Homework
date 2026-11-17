
valid_readings = 0
invalid_readings = 0
overheating_readings = 0
total_temp = 0

for i in range(1, 7):
    temperature = float(input(f"Enter temperature {i}: "))

    if temperature < -40 or temperature > 120:
        invalid_readings += 1
        print(f"Reading {i}: INVALID - skipped")
    else:
        valid_readings += 1
        total_temp += temperature

        if temperature >= 85:
            overheating_readings += 1
            print(f"Reading {i}: OK - overheating")
        else:
            print(f"Reading {i}: OK")

if valid_readings == 0:
    average_temp = 0
else:
    average_temp = total_temp / valid_readings

if valid_readings == 0:
    status = "NO DATA"
elif overheating_readings >= 2 or average_temp >= 80:
    status = "CRITICAL"
elif overheating_readings == 1:
    status = "WARNING"
else:
    status = "HEALTHY"

print("====== SENSOR REPORT ======")
print(f"Valid Readings: {valid_readings}")
print(f"Invalid Readings: {invalid_readings}")
print(f"Average Temperature: {average_temp:.2f} C")
print(f"Overheating Readings: {overheating_readings}")
print(f"Server Status: {status}")
print("===========================")
