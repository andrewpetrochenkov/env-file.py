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
`env_file.get(variable, default=None)`|return the value for variable if variable is in the file, else default
`env_file.load(path='.env')`|load .env file variables and return a dictionary
`env_file.setup(path='.env')`|load .env file variables and set environment variables
`env_file.update(**kwargs)`|update .env file

#### CLI
usage|`__doc__`
-|-
`python -m env_file variable [value]`|get/set .env variable

```bash
usage: env-file variable [value]
```

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
    env_file.setup()

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
```

##### library example
```python
>>> import env_file
>>> env_file.get('DB_NAME')
'DB_NAME'
>>> env_file.load(['.env','dev.env'])
```

##### cli example
```bash
$ env-file DB_NAME
dbname
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>