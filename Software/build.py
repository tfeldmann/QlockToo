# -*- coding: utf-8 -*-
"""
Use this script to convert the given Qt .ui and .rc files into python files.
This currently only works in Linux or Mac OS X with pyside-tools installed.
"""
import os
import pysideuic


def _naming_convetion_ui(pydir, pyfile):
    name = os.path.splitext(pyfile)[0]
    return pydir, name + '_ui.py'


def convert_ui(path):
    pysideuic.compileUiDir(path, recurse=True,
                           map=_naming_convetion_ui, from_imports=True)


def convert_rcc(args, dirname, filenames):
    for filename in filenames:
        if '.qrc' in filename:
            old_path = os.path.join(dirname, filename)
            new_filename = os.path.splitext(filename)[0] + "_rc.py"
            new_path = os.path.join(dirname, new_filename)
            os.system("pyside-rcc " + old_path + " > " + new_path)


def run(ui=True, qrc=True):
    path = './'
    if qrc:
        print("Converting .qrc files.")
        os.path.walk(path, convert_rcc, None)
    if ui:
        print("Converting .ui-files.")
        convert_ui(path)
    print('Done.')

if __name__ == '__main__':
    run()
