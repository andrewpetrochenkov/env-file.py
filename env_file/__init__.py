#!/usr/bin/env python
import os
import public
import values


def parse(line):
    """parse line and return a dictionary with variable value"""
    if line.lstrip().startswith('#'):
        return {}
    if not line.lstrip():
        return {}
    """find the second occurence of a quote mark:"""
    quote_delimit = max(line.find('\'', line.find('\'') + 1),
                        line.find('"', line.rfind('"')) + 1)
    """find first comment mark after second quote mark"""
    comment_delimit = line.find('#', quote_delimit)
    line = line[:comment_delimit]
    key, value = map(lambda x: x.strip().strip('\'').strip('"'),
                     line.split('=', 1))
    return {key: value}


@public.add
class EnvFile(dict):
    """.env file class"""
    path = None

    def __init__(self, path, **kwargs):
        self.path = os.path.abspath(os.path.expanduser(path))
        if os.path.exists(self.path):
            self.load()
        for k, v in kwargs.items():
            self[k] = v

    def load(self):
        """load env variables from a file"""
        variables = {}
        with open(self.path, 'r') as dotenv:
            for line in dotenv.readlines():
                variables.update(parse(line))
        dict.__init__(self, **variables)
        return self

    def save(self):
        """save a dictionary to a file"""
        lines = []
        for key, value in self.items():
            lines.append("%s=%s" % (key, value))
        lines.append("")
        open(self.path, 'w').write("\n".join(lines))

    def __setitem__(self, key, value):
        super(EnvFile, self).__setitem__(key, value)

    def __delitem__(self, key):
        super(EnvFile, self).__delitem__(key)


@public.add
def load(path=".env"):
    """load .env file variables and return a dictionary"""
    if not path:
        path = ".env"
    data = dict()
    for path in values.get(path):
        data.update(EnvFile(path))
    return data


@public.add
def setup(path=".env"):
    """load .env file variables and set environment variables"""
    if not path:
        path = ".env"
    for path in values.get(path):
        os.environ.update(load(path))


@public.add
def get(variable, default=None):
    """return the value for variable if variable is in the file, else default"""
    data = load()
    if default is None:
        return data.get(variable)
    return data.get(variable, default)


@public.add
def update(**kwargs):
    """update .env file"""
    env = EnvFile(".env")
    for k, v in kwargs.items():
        env[k] = v
    env.save()
