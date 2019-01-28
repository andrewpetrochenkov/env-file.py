#!/usr/bin/env python
"""get/set .env variable"""
# -*- coding: utf-8 -*-
import click
import env_file


MODULE_NAME = "env_file"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s variable [value]' % MODULE_NAME


@click.command()
@click.argument('variable', required=True)
@click.argument('value', required=False)
def _cli(variable, value=None):
    path = ".env"
    env = env_file.EnvFile(path)
    if value is None:
        if variable in env:
            print(env[variable])
    else:
        env[variable] = value
        env.save()


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
