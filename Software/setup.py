"""
This is a setup.py script

Usage:
    python setup.py py2app
"""

from setuptools import setup
import buildtools

buildtools.convert_ui()
print "Converted .ui files."

setup(
    app=['main.py'],
    setup_requires=['pyserial', 'py2app'],
)
