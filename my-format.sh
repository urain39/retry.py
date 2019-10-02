#!/usr/bin/env bash

isort -rc retry.py
yapf -i -r retry.py
exit $?

