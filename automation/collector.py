from netmiko import ConnectHandler
from devices import devices
from datetime import datetime
import os

commands = [
    "show ip interface brief",
    "show ip route",
    "show ip ospf neighbor",
    "show running-config",
]

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
folder = f"outputs/{timestamp}"
os.makedirs(folder, exist_ok=True)

for device in devices:
    print(f"Connecting to {device['name']}...")

    try:
        netmiko_device = device.copy()
        netmiko_device.pop("name")

        connection = ConnectHandler(**netmiko_device)

        output = f"Device: {device['name']}\n"
        output += f"Host: {device['host']}\n"
        output += f"Collected: {timestamp}\n"
        output += "=" * 60 + "\n\n"

        for command in commands:
            print(f"Running '{command}' on {device['name']}...")
            result = connection.send_command(command)
            output += f"\n\n### {command} ###\n"
            output += result
            output += "\n"

        filename = f"{folder}/{device['name']}.txt"

        with open(filename, "w") as file:
            file.write(output)

        connection.disconnect()
        print(f"Saved: {filename}")

    except Exception as error:
        print(f"Failed on {device['name']}: {error}")