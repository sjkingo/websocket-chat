#!/usr/bin/env python3

LISTEN_ADDRESS = ('0.0.0.0', 8080)

import websockets
from server import client_handler
start_server = websockets.serve(client_handler, *LISTEN_ADDRESS)

import asyncio
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
