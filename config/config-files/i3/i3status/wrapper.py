#!/usr/bin/env python3

# Adopted from https://github.com/i3/i3status/blob/master/contrib/wrapper.py
# and modified by jerry-sky.
#
# This script is a simple wrapper which prefixes each i3status line with custom
# information. It is a python reimplementation of:
# http://code.stapelberg.de/git/i3status/tree/contrib/wrapper.pl
#
# To use it, ensure your ~/.i3status.conf contains this line:
#     output_format = "i3bar"
# in the 'general' section.
# Then, in your ~/.i3/config, use:
#     status_command i3status | ~/i3status/contrib/wrapper.py
# In the 'bar' section.
#
# In its current version it will display the cpu frequency governor, but you
# are free to change it to display whatever you like, see the comment in the
# source code below.
#
# © 2012 Valentin Haenel <valentin.haenel@gmx.de>
#
# This program is free software. It comes without any warranty, to the extent
# permitted by applicable law. You can redistribute it and/or modify it under
# the terms of the Do What The Fuck You Want To Public License (WTFPL), Version
# 2, as published by Sam Hocevar. See http://sam.zoy.org/wtfpl/COPYING for more
# details.

import sys
import subprocess
import json
from typing import List
import re


def is_mic_muted():
    """
    Returns `True` when microphone (default source) is muted.
    """
    output: str = subprocess.check_output(
        # find default source
        # display next 20 lines containing information about this default source
        # grab the ‘muted’ parameter
        # extract its value
        "pacmd list-sources | grep '*' -A 20 | grep muted: | awk '{print $2}'",
        shell=True
    )
    # the output of the above command can be either `yes` or `no`
    # in rudimentary ASCII (hence binary string)
    return output.strip() == b'yes'


def print_line(message):
    """
    Non-buffered printing to stdout.
    """
    sys.stdout.write(message + '\n')
    sys.stdout.flush()


def read_line():
    """
    Interrupted respecting reader for stdin.
    """
    # try reading a line, removing any extra whitespace
    try:
        line = sys.stdin.readline().strip()
        # i3status sends EOF, or an empty line
        if not line:
            sys.exit(3)
        return line
    # exit on ctrl-c
    except KeyboardInterrupt:
        sys.exit()


def parse_space_units(item):
    '''
    Finds all -ibi values and convert them to decimal
    '''
    expression = r'([0-9]+(,|\.)[0-9])+\s?(.)iB'
    match = re.findall(expression, item['full_text'])
    if match:
        # extract the numerical value
        value = float(match[0][0].replace(',', '.'))
        # extract the separator (the comma or the dot)
        separator = match[0][1]
        # extract the order of magnitude
        order = match[0][2]
        # convert to decimal
        decimal = value * 1.074
        # update the visible text
        item['full_text'] = re.sub(
            expression,
            format(decimal, '.2f').replace('.', separator) + ' ' + order + 'B',
            item['full_text'],
        )


def pad_decimal_values(item, width=3):
    '''
    Adds visual padding to number values.
    '''
    if width < 2:
        raise Exception('pad width has to be at least `2`')
    # match a number prefixed by a blank or a parenthesis
    expression = r'(\s|\(+)([0-9]{1,' + str(width-1) + r'})([^0-9:])'
    match = re.findall(expression, item['full_text'])
    while match:
        m = match[0]
        number: str = m[1]
        value = m[0] + number.rjust(width, '•') + m[2]
        item['full_text'] = re.sub(
            expression,
            value,
            item['full_text'],
            count=1,
        )
        match = re.findall(expression, item['full_text'])


if __name__ == '__main__':
    # Skip the first line which contains the version header.
    print_line(read_line())

    # The second line contains the start of the infinite array.
    print_line(read_line())

    while True:
        line, prefix = read_line(), ''
        # ignore comma at start of lines
        if line.startswith(','):
            line, prefix = line[1:], ','

        data: List = json.loads(line)
        # insert information into the start of the json, but could be anywhere
        if is_mic_muted():
            data.insert(0, {
                'full_text': '%s' % '  aus ',
                'color': '#efefef',
                'name': 'mic'
            })
        else:
            data.insert(0, {
                'full_text': '%s' % '   ein ',
                # 'color': '#efefef',
                'name': 'mic'
            })

        for item in data:
            parse_space_units(item)
            if item['name'] != 'tztime':
                pad_decimal_values(item)

        # and echo back new encoded json
        print_line(prefix+json.dumps(data))
