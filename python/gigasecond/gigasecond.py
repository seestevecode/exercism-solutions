"""Calculate the moment 1 gigasecond after a specified moment"""

from datetime import timedelta

def add(moment):
    return moment + timedelta(seconds=1e9)
