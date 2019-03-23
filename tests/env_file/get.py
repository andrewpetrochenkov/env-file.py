#!/usr/bin/env python
import env_file
import os

os.chdir(os.path.dirname(__file__))

data = env_file.get()
print(data)

assert data["PGDATA"] == "/var/lib/postgresql/data"
assert data["POSTGRES_USER"] == "postgres"
