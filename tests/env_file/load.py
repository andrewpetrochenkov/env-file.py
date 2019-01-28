#!/usr/bin/env python
import env_file
import os

os.chdir(os.path.dirname(__file__))

data = env_file.load()
print(data)

data = env_file.load([".env", "dev.env"])
print(data)
