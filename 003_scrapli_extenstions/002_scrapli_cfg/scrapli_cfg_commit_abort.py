#!/usr/bin/env python

import os

from dotenv import load_dotenv
from scrapli import Scrapli
from scrapli_cfg import ScrapliCfg
from scrapli.logging import enable_basic_logging

load_dotenv()

# Enable logging. Create a log file in the current directory.
enable_basic_logging(file=True, level="debug")
from helpers import read_file

load_dotenv()

BACKUP_FILENAME = "running-config.txt"

# Create device dict()
device = {
    "host": "172.29.151.7",
    "auth_username": os.getenv("LAB_USERNAME"),
    "auth_password": os.getenv("LAB_PASSWORD"),
    "auth_strict_key": False,
    "platform": "arista_eos",
}

# Scrapli context manager - Instantiate, open and close connection
with Scrapli(**device) as conn:
    # Instantiate Scrapli Cfg
    cfg_conn = ScrapliCfg(conn=conn)

    # Prepare Scrapli connection, call prepare_on() etc
    cfg_conn.prepare()

    # Load configuration as candiate
    load_result = cfg_conn.load_config(
        config=read_file(filename=BACKUP_FILENAME), replace=True
    )

    # Perform validation on load_config
    if load_result.failed:
        cfg_conn.abort_config()
        print("load_config aborted")
    else:
        commit_result = cfg_conn.commit_config()
        print(f"commit_config = {commit_result}")
