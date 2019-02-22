[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/env-file.svg?longCache=True)](https://pypi.org/project/env-file/)
[![](https://img.shields.io/pypi/v/env-file.svg?maxAge=3600)](https://pypi.org/project/env-file/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/env-file.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/env-file.py/)

#### Install
```bash
$ [sudo] pip install env-file
```

#### Classes
`env_file.EnvFile` - .env file class

#### Functions
function|`__doc__`
-|-
`env_file.get(path='.env')`|return a dictionary wit .env file variables
`env_file.load(path='.env')`|set environment variables from .env file

#### Examples
##### Django example

`.env`
```bash
DJANGO_SETTINGS_MODULE = project.settings
DJANGO_SECRETKEY = somerandomkey
DB_NAME=dbname
DB_PASS=secret
```

`manage.py`
```python
import env_file
import sys

if __name__ == "__main__":
    #  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    env_file.load()

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>