#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-13 23:44:30
# @Author  : Kelly Hwong (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os


class TreeNode(object):
    def __init__(self, data=None, parent=None, childs=None):
        # childs: list of TreeNode
        self.data = data
        self.parent = parent  # 父亲节点
        self.childs = childs  # 多个子节点

    def print(self):
        _ = self
        while _ is not None:
            print(_.data)
            _ = _.childs[0]
