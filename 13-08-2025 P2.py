data = [
    "device1 vlan1",
    "device2 vlan2",
    "device3 vlan1",
    "device2 vlan3",
    "device1 vlan4",
    "device2 vlan1",
    "device3 vlan6"
]

result = {}

for line in data:
    device, vlan = line.split()

    if device not in result:
        result[device] = []

    result[device].append(vlan)

print(result)