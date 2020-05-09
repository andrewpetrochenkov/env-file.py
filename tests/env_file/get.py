#!/usr/bin/env python
import env_file
import os

os.chdir(os.path.dirname(__file__))

data = env_file.get()
print(data)

assert data["PGDATA"] == "/var/lib/postgresql/data"
assert data["POSTGRES_USER"] == "postgres"

assert 'COMMENT' not in data
assert data["SINGLE_QUOTED"] == "value"
assert data["DOUBLE_QUOTED"] == "value"
assert data["EXPORTED"] == "value"
assert data["CONTAINS_EXPORT"] == "key=value; export more"
