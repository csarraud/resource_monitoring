#!/bin/python3

from PyQt6.QtWidgets import QApplication, QWidget
import sys
import redis
import argparse

def main():
    # Parse arguments and
    parser = argparse.ArgumentParser("resource_monitoring_server.py")
    parser.add_argument("--server-address", action="store", dest="server_address", default="localhost", help="set the server address ip (default: localhost)")
    parser.add_argument("--server-port", action="store", dest="server_port", default=6379, help="set the server port (default: 6379)")
    args = parser.parse_args()

    redis_server = redis.Redis(host=args.server_address, port=args.server_port)

    app = QApplication([])

    window = QWidget()

    window.setWindowTitle("Resource monitoring server")
    
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()