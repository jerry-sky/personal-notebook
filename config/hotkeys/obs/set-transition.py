#!/usr/bin/env python3
from sys import argv
from obs import OBS


obs = OBS()


t = argv[1]
transition = 'Stinger'
if t == 'm':
    transition = 'Schnitt'
elif t == 'comma':
    transition = 'Überblende'
elif t == 'period':
    transition = 'Luma Wipe'

duration = 200 if transition == 'Fade' else 300


async def program():
    await obs.request('SetCurrentSceneTransition', {
        'transitionName': transition
    })
    await obs.request('SetCurrentSceneTransitionDuration', {
        'transitionDuration': duration
    })


obs.execute(program)
