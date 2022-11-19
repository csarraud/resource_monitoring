#!/bin/python3

from time import sleep
import argparse
import redis
import json
import psutil

def main():
    # Parse arguments and
    parser = argparse.ArgumentParser("resource_monitoring_client.py")
    parser.add_argument("--server-address", action="store", dest="server_address", default="localhost", help="set the server address ip (default: localhost)")
    parser.add_argument("--server-port", action="store", dest="server_port", default=6379, help="set the server port (default: 6379)")
    parser.add_argument("--client-name", action="store", dest="client_name", default="client_name", help="set the client name (default: client_name)")
    args = parser.parse_args()

    redis_server = redis.Redis(host=args.server_address, port=args.server_port)

    cpu_load_avg_time_name = ["1_min", "5_min", "15_min"]

    # Main loop
    while True:

        sensor_temperature = {}
        for sensor_name, sensor_infos in psutil.sensors_temperatures().items():
            for info in sensor_infos:
                for name, value in info._asdict().items():
                    sensor_temperature = {sensor_name: {
                        name: value
                    }}

        # See https://psutil.readthedocs.io/en/latest/
        resource_values = {
            # CPU
            "cpu_count": psutil.cpu_count(),
            "cpu_percent": {
                f"id_{index}" : value for index, value in enumerate(psutil.cpu_percent(interval=None, percpu=True))
                },
            "cpu_freq": {
                f"id_{index}" : {
                    "current": values[0],
                    "min": values[1],
                    "max": values[2]
                } for index, values in enumerate(psutil.cpu_freq(percpu=True))
            },
            "cpu_load_avg": {
                cpu_load_avg_time_name[index]: value for index, value in enumerate(psutil.getloadavg())
            },

            # Memory
            "virtual_memory": {
                name: value for name, value in psutil.virtual_memory()._asdict().items()
            },
            "swap_memory": {
                name: value for name, value in psutil.swap_memory()._asdict().items()
            },

            # Disks
            "disk_usage": {
                name: value for name, value in psutil.disk_usage("/")._asdict().items()
            },
            "disk_io": {
                disk_name: {
                    name: value for name, value in disk_info._asdict().items()
                } for disk_name, disk_info in psutil.disk_io_counters(perdisk=True).items()
            },

            # Network
            "network_io": {
                network_name: {
                    name: value for name, value in network_info._asdict().items()
                } for network_name, network_info in psutil.net_io_counters(pernic=True).items()
            },

            # Sensors
            "sensor_temperature": sensor_temperature,
            "sensor_fan": {
                sensor_fan_name: {
                    name: value for name, value in sensor_fan_info._asdict().items()
                } for sensor_fan_name, sensor_fan_info in psutil.sensors_fans().items()
            },
            "sensor_battery": {
                name: value for name, value in psutil.sensors_battery()._asdict().items()
            }
        }

        redis_server.set(f"resource_monitoring_client:{args.client_name}", json.dumps(resource_values))

        sleep(0.5)


if __name__ == "__main__":
    main()