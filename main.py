#!/usr/bin/env python3

import serial
import keyboard
from enum import Enum
import sys

Key = Enum('Key', 'next prev play pause stop')

keymap = {
    '538526F': Key.next,
    '53892AF': Key.prev,
    '5446021': Key.pause,
    '5440041': Key.stop,
    '5445011': Key.play,
}

actionmap = {
    Key.next: 'next track',
    Key.prev: 'previous track',
    Key.play: 'play/pause media',
    Key.pause: 'play/pause media',
    Key.stop: 'stop media',
}

def act(bytes):
    str = bytes.decode('utf-8')
    print(str)
    if not str in keymap:
        return
    
    key = keymap[str]
    if not key in actionmap:
        return

    action = actionmap[key]
    print(action)
    keyboard.send(action)


port = sys.argv[1]
baud = 9600
with serial.Serial(port, baud, timeout=1) as ser:
    while True:
        line = ser.readline()
        if line:
            act(line.rstrip())