#!/usr/bin/env python3

import asyncio
import websockets

from server import client_handler

start_server = websockets.serve(client_handler, '0.0.0.0', 8080)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
