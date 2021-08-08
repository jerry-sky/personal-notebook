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

chosen_scene_key = argv[1]

async def make_request():
    await ws.connect()
    try:
        # pick the scene that has the key at the beginning of its name
        # (discard any other scenes that also begin with the same character
        # that happens to be the key)
        chosen_scene, *_ = [
            scene['name'] for scene in (await ws.call('GetSceneList'))['scenes']
            if scene['name'].startswith(chosen_scene_key)
        ]
    except ValueError as e:
        exit(1)

    result = await ws.call('SetCurrentScene', {
        'scene-name': chosen_scene
    })
    print(json.dumps(result, indent=4))
    await asyncio.sleep(1)
    await ws.disconnect()

loop.run_until_complete(make_request())
