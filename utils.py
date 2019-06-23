#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-13 12:56:57
# @Author  : Kelly Hwong (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import json


def read_config(file="./config.json"):
    with open(file, "r") as f:
        config = json.load(f)
        print(config)


def main():
    read_config()


if __name__ == "__main__":
    main()
