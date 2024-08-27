#!/usr/bin/env python

import json
import sys
import struct

binary_stdin = sys.stdin if sys.version_info < (3, 0) else sys.stdin.buffer
binary_stderr = sys.stderr if sys.version_info < (3, 0) else sys.stderr.buffer
binary_stdout = sys.stdout if sys.version_info < (3, 0) else sys.stdout.buffer

def input_stream():
    while True:
        byte_len = binary_stdin.read(8)
        if len(byte_len) == 8:
            byte_len = struct.unpack("L", byte_len)[0]
            result = binary_stdin.read(byte_len)
            yield result
        else:
            assert len(byte_len) == 0, byte_len
            return

def log(message):
    binary_stderr.write(message + b"\n")

def emit(message):
    binary_stdout.write(message + b"\n")

log(b"Begin transform")

for data in input_stream():
    try:
        json_data = json.loads(data.decode('utf-8'))
        transformed_data = json.dumps(json_data)
        emit(transformed_data.encode('utf-8'))
    except json.JSONDecodeError as e:
        log(f"JSON decode error: {str(e)}".encode('utf-8'))
        emit(data)

log(b"End transform")