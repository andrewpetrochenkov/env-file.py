<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/env-file.svg?maxAge=3600)](https://pypi.org/project/env-file/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/env-file.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/env-file.py/actions)

### Installation
```bash
$ [sudo] pip install env-file
```

#### Examples
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
    <a href="https://readme42.com/">readme42.com</a>
</p>
