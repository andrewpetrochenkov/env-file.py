#!/usr/bin/env python
import env_file
import os

os.chdir(os.path.dirname(__file__))

env_file.load()
env_file.load(".env")
env_file.load([".env", "dev.env"])
for var, value in os.environ.items():
    print("%s=%s" % (var, value))
