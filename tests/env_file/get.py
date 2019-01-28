#!/usr/bin/env python
import env_file
import os

os.chdir(os.path.dirname(__file__))

value = env_file.get("POSTGRES_PASSWORD")
print(value)

value = env_file.get("no-existing")
print(value)
