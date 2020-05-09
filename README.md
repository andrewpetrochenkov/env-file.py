<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/env-file.svg?longCache=True)](https://pypi.org/project/env-file/)
[![](https://img.shields.io/pypi/v/env-file.svg?maxAge=3600)](https://pypi.org/project/env-file/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/env-file.py.svg?branch=master)](https://travis-ci.org/andrewp-as-is/env-file.py/)

#### Installation
```bash
$ [sudo] pip install env-file
```

#### Classes
class|`__doc__`
-|-
`env_file.EnvFile` |.env file class

#### Functions
function|`__doc__`
-|-
`env_file.get(path='.env')` |return a dictionary wit .env file variables
`env_file.load(path='.env')` |set environment variables from .env file

#### Examples

`.env`
```bash
DJANGO_SETTINGS_MODULE=project.settings
DB_NAME=dbname
DB_PASS=secret
```

```python
import env_file
env_file.load('.env')
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>