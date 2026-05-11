devices = [
    {
        "name": "SW-DIST",
        "device_type": "cisco_ios",
        "host": "10.0.99.1",
        "username": "YOUR_USERNAME",
        "password": "YOUR_PASSWORD",
        "disabled_algorithms": {
            "pubkeys": ["rsa-sha2-256", "rsa-sha2-512"]
        },
        "conn_timeout": 20,
    },

    {
        "name": "Router-A",
        "device_type": "cisco_ios",
        "host": "10.0.100.2",
        "username": "YOUR_USERNAME",
        "password": "YOUR_PASSWORD",
        "disabled_algorithms": {
            "pubkeys": ["rsa-sha2-256", "rsa-sha2-512"]
        },
        "conn_timeout": 20,
    },

    {
        "name": "Router-B",
        "device_type": "cisco_ios",
        "host": "10.0.101.2",
        "username": "YOUR_USERNAME",
        "password": "YOUR_PASSWORD",
        "disabled_algorithms": {
            "pubkeys": ["rsa-sha2-256", "rsa-sha2-512"]
        },
        "conn_timeout": 20,
    },
]