# -*- coding: utf-8 -*-
import os
import pysideuic

def _naming_convetion_ui(pydir, pyfile):
    name = os.path.splitext(pyfile)[0]
    return pydir, name + '_ui.py'

def _naming_convetion_rcc(pydir, pyfile):
    name = os.path.splitext(pyfile)[0]
    return pydir, name + '_rcc.py'

def convert_ui():
    pysideuic.compileUiDir('.', recurse=True, map=_naming_convetion_ui)
    print "Converting ui files done."

def convert_rcc():
    print "Converting resource files:"
    assets = [f for f in os.listdir('./') if f.endswith('.qrc')]
    for asset in assets:
        asset_path = os.path.abspath(asset)
        converted_path = asset_path[:-4] + "_rc.py"
        os.system("pyside-rcc " + asset_path + " > " + converted_path)
        print asset


if __name__ == '__main__':
    convert_ui()
    convert_rcc()
