# -*- coding: utf-8 -*-
import os.path
import pysideuic

def _naming_convetion_ui(pydir, pyfile):
    name = os.path.splitext(pyfile)[0]
    return pydir, name + '_ui.py'

def convert_ui():
    pysideuic.compileUiDir('.', recurse=True, map=_naming_convetion_ui)

def convert_rcc():
    pass


if __name__ == '__main__':
    convert_ui()
    convert_rcc()
