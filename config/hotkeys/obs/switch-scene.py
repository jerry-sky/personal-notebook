#!/usr/bin/env python3
from sys import argv, exit
from obs import OBS


obs = OBS()


chosen_scene_key = argv[1]


async def program():
    try:
        # pick the scene that has the key at the beginning of its name
        # (discard any other scenes that also begin with the same character
        # that happens to be the key)
        scenes = await obs.request('GetSceneList')
        scenes = scenes['scenes']
        chosen_scene, *_ = [
            scene['sceneName'] for scene in scenes
            if scene['sceneName'].startswith(chosen_scene_key)
        ]
    except ValueError as _:
        exit(1)

    await obs.request('SetCurrentProgramScene', {
        'sceneName': chosen_scene
    })


obs.execute(program)
