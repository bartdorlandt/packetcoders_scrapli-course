#!/usr/bin/env python

import os

from rich import print
from scrapli import Scrapli

# Create device dict()
device = {
    # "host": "172.29.151.1",
    "host": "nebula.packetflow.co.uk",
    "port": 9001,
    "auth_username": os.getenv("LAB_USERNAME"),
    "auth_password": os.getenv("LAB_PASSWORD"),
    "auth_strict_key": False,
    "platform": "cisco_nxos",
}

# Scrapli context manager - Instantiate, open and close connection
with Scrapli(**device) as conn:
    # Send command to device
    response = conn.send_command("show ip interface brief")

    # Genie parse response
    genie_parsed_response = response.genie_parse_output()

# Print parsed response
print(genie_parsed_response)
