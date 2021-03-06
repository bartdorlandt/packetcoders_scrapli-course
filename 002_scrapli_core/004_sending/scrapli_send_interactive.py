#!/usr/bin/env python

import os

from dotenv import load_dotenv
from rich import print
from scrapli import Scrapli

load_dotenv()


# Create device dict()
device = {
    "host": "172.29.151.1",
    "auth_username": os.getenv("LAB_USERNAME"),
    "auth_password": os.getenv("LAB_PASSWORD"),
    "auth_strict_key": False,
    "platform": "cisco_nxos",
}

# Scrapli context manager - Instantiate, open and close connection
with Scrapli(**device) as conn:
    # Send commands based on returned prompts
    interactive = conn.send_interactive(
        [
            ("ping", "Vrf context to use [default] :", False),
            ("default", "Target IP address or Hostname:", False),
            ("3.3.3.3", "Repeat count [5] :", False),
            ("2", "Packet-size [56] :", False),
            ("5", "Timeout in seconds [2] :", False),
            ("2", "Sending interval in seconds [0] :", False),
            ("0", "Extended commands [no] :", False),
            ("no", "Sweep range of sizes [no] :", False),
            ("no", "spine1-nxos#", False),
        ]
    )

# print result of send_interactive
print(interactive.result)
