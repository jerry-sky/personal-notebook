#!/usr/bin/env python3
import asyncio
import simpleobsws
import json
from sys import argv

loop = asyncio.get_event_loop()
ws = simpleobsws.obsws(host='127.0.0.1', port=4444, password='merdasmerdas2137', loop=loop)

chosen_scene = argv[1]

async def make_request():
    await ws.connect()
    result = await ws.call('SetCurrentScene', {
        'scene-name': chosen_scene
    })
    print(json.dumps(result, indent=4))
    await asyncio.sleep(1)
    await ws.disconnect()

loop.run_until_complete(make_request())
