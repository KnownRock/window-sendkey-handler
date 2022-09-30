import json
import os
import sys
from pathlib import Path

import argparse


def getConfig():

    parser = argparse.ArgumentParser(prog='myprogram')
    parser.add_argument('--main_hwnd', help='main window handle',
                        type=str, required=True)
    parser.add_argument('--server_port', help='server port',
                        type=int, required=True)
    parser.add_argument('--server_auth', help='server auth',
                        type=str, default='123456')
    
    args = parser.parse_args()
    
    return {
        "main_hwmd": args.main_hwnd,
        "server_port": args.server_port,
        "server_auth": args.server_auth
    }
