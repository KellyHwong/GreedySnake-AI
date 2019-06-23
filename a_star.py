#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-13 23:16:24
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from TreeNode import TreeNode


class GridData(object):
    def __init__(self, coord=None, f=float("inf"), g=float("inf"), h=float("inf")):
        self.coord = coord
        self.f = f
        self.g = g
        self.h = h


def around(coord):  # 不考虑边界
    return [(coord[0], coord[1]), (coord[0], coord[-1]), (coord[-1], coord[0]), (coord[1], coord[0])]


def a_star(start: tuple, target: tuple):
    """A star algorithm

    Args:
        start (tuple): ( , ) start's coord
        target (tuple): ( , ) target's coord

    Returns:
        path (TreeNode): Head node of the path

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
    start_node = TreeNode(data=GridData(coord=start))  # 首先树状图化
    open_list = [start_node]
    close_list = []
    ptr = open_list[0]
    for node in open_list:
        if node.data.f < ptr.data.f:
            ptr = node
        close_list.append(node)
        for coord in around(ptr.data.coord):  # ptr arounds 下一步的节点，4点，或者8点
            if coord not in [_.data.coord for _ in open_list]:
                _ = TreeNode()
                _.father = ptr
                _.data = GridData(coord=coord)  # TODO f, g, h
                open_list.append(_)
            else:
                pass

        # open_list.append(_)

    close_list = []

    # target
    return None


def main():
    grids = [(1, 1), (2, 2), (3, 3)]
    start = grids[0]
    target = (10, 10)
    ret = a_star(start, target)


if __name__ == "__main__":
    main()
