#!/usr/bin/python3
"""
module for determining if dataset is a valid utf-8 encording
"""


def validUTF8(data):
    """
    function that checks if a dataset is a valid utf-8 encorded
    """
    try:
        for num in data:
            if num < 0 or num > 255:
                return False
        byte_data = bytes(data)
        byte_data.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
