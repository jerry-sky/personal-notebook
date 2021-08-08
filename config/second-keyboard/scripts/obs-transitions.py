#!/usr/bin/env python3
import asyncio
import simpleobsws
import json
from sys import argv, exit
import os

f = open(os.path.dirname(os.path.realpath(__file__)) + '/.ws')
password = f.read()
f.close()

loop = asyncio.get_event_loop()
ws = simpleobsws.obsws(host='127.0.0.1', port=4444, password=password, loop=loop)

transition = argv[1]

async def make_request():
    await ws.connect()

    duration = 200 if transition == 'Fade' else 300

    result = await ws.call('SetCurrentTransition', {
        'transition-name': transition
    })
    print(result)
    result = await ws.call('SetTransitionDuration', {
        'duration': duration
    })
    print(result)

    await asyncio.sleep(1)
    await ws.disconnect()

loop.run_until_complete(make_request())
