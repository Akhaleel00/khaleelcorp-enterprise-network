from netmiko import ConnectHandler
from devices import devices
import json
import os
from datetime import datetime

commands = {
    "interfaces": "show ip interface brief",
    "routes": "show ip route",
    "ospf": "show ip ospf neighbor",
    "vlans": "show vlan brief",
    "trunks": "show interfaces trunk",
}

network_data = {
    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "devices": {}
}

for device in devices:
    device_name = device["name"]
    print(f"Collecting data from {device_name}...")

    netmiko_device = device.copy()
    netmiko_device.pop("name")

    try:
        connection = ConnectHandler(**netmiko_device)

        network_data["devices"][device_name] = {}

        for section, command in commands.items():
            try:
                output = connection.send_command(command)
                network_data["devices"][device_name][section] = output
            except Exception as error:
                network_data["devices"][device_name][section] = f"Command failed: {error}"

        connection.disconnect()

    except Exception as error:
        network_data["devices"][device_name] = {
            "error": str(error)
        }

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

network_data["last_updated"] = timestamp

os.makedirs("data/snapshots", exist_ok=True)

snapshot_path = f"data/snapshots/{timestamp}.json"
latest_path = "data/latest.json"

with open(snapshot_path, "w") as file:
    json.dump(network_data, file, indent=4)

with open(latest_path, "w") as file:
    json.dump(network_data, file, indent=4)

print(f"Saved snapshot: {snapshot_path}")
print(f"Updated latest: {latest_path}")

print("Dashboard data saved to data.json")