import os

from dotenv import load_dotenv
from scrapli.driver.core import (
    AsyncEOSDriver,
    AsyncIOSXEDriver,
    AsyncJunosDriver,
    AsyncNXOSDriver,
)

load_dotenv()

DEVICES = [
    {
        "auth_username": os.getenv("LAB_USERNAME"),
        "auth_password": os.getenv("LAB_PASSWORD"),
        "host": "172.29.151.1",
        "port": 22,
        "transport": "asyncssh",
        "auth_strict_key": False,
        "driver": AsyncNXOSDriver,
    },
    {
        "auth_username": os.getenv("LAB_USERNAME"),
        "auth_password": os.getenv("LAB_PASSWORD"),
        "host": "172.29.151.2",
        "port": 22,
        "transport": "asyncssh",
        "auth_strict_key": False,
        "driver": AsyncNXOSDriver,
    },
    {
        "auth_username": os.getenv("LAB_USERNAME"),
        "auth_password": os.getenv("LAB_PASSWORD"),
        "host": "172.29.151.3",
        "port": 22,
        "transport": "asyncssh",
        "auth_strict_key": False,
        "driver": AsyncIOSXEDriver,
    },
    {
        "auth_username": os.getenv("LAB_USERNAME"),
        "auth_password": os.getenv("LAB_PASSWORD"),
        "host": "172.29.151.4",
        "port": 22,
        "transport": "asyncssh",
        "auth_strict_key": False,
        "driver": AsyncIOSXEDriver,
    },
    {
        "auth_username": os.getenv("LAB_USERNAME"),
        "auth_password": os.getenv("LAB_PASSWORD"),
        "host": "172.29.151.5",
        "port": 22,
        "transport": "asyncssh",
        "auth_strict_key": False,
        "driver": AsyncJunosDriver,
    },
    {
        "auth_username": os.getenv("LAB_USERNAME"),
        "auth_password": os.getenv("LAB_PASSWORD"),
        "host": "172.29.151.6",
        "port": 22,
        "transport": "asyncssh",
        "auth_strict_key": False,
        "driver": AsyncJunosDriver,
    },
    {
        "auth_username": os.getenv("LAB_USERNAME"),
        "auth_password": os.getenv("LAB_PASSWORD"),
        "host": "172.29.151.7",
        "port": 22,
        "transport": "asyncssh",
        "auth_strict_key": False,
        "driver": AsyncEOSDriver,
    },
    {
        "auth_username": os.getenv("LAB_USERNAME"),
        "auth_password": os.getenv("LAB_PASSWORD"),
        "host": "172.29.151.8",
        "port": 22,
        "transport": "asyncssh",
        "auth_strict_key": False,
        "driver": AsyncEOSDriver,
    },
]
