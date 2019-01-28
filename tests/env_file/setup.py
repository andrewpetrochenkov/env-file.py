#!/usr/bin/env python
import env_file
import os

os.chdir(os.path.dirname(__file__))


env_file.setup()
for variable in ["POSTGRES_DB", "POSTGRES_USER", "POSTGRES_PASSWORD"]:
    print(os.environ[variable])
