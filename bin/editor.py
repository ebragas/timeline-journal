"""Test opening working with a users editor"""
import sys
import tempfile
import os
from subprocess import call

EDITOR = os.environ.get("EDITOR", "vim")

initial_message = b"Initial message: "  # file setup

with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
    tf.write(initial_message)
    tf.flush()
    call([EDITOR, tf.name])

    tf.seek(0)
    edited_message = open(tf.name, 'r').read()

print(edited_message)
