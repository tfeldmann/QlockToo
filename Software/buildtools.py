# -*- coding: utf-8 -*-
import os
import pysideuic


def _naming_convetion_ui(pydir, pyfile):
    name = os.path.splitext(pyfile)[0]
    return pydir, name + '_ui.py'

def convert_ui(path):
    pysideuic.compileUiDir(path, recurse=True, map=_naming_convetion_ui)

def convert_rcc(args, dirname, filenames):
    for filename in filenames:
        path = os.path.join(dirname, filename)
        if '.qrc' in filename:
            converted = os.path.splitext(filename)[0] + "_rc.py"
            os.system("pyside-rcc " + filename + " > " + converted)


if __name__ == '__main__':
    path = './'
    print("Converting .qrc files.")
    os.path.walk(path, convert_rcc, None)
    print("Converting .ui-files.")
    convert_ui(path)
    print('Done.')
