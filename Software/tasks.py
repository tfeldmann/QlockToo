import os
import sys
import logging
import subprocess
from concurrent.futures import ProcessPoolExecutor
from invoke import task


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
logger = logging.getLogger('task')


@task
def gui(top='qlocktoo'):
    """Convert PySide QRC and UI files to python files

    This script recurses through all subdirectories.
    """
    file_list = []
    for root, _, files in os.walk(top=top, topdown=False):
        # exclude the .git directory
        if '.git' in root:
            continue

        for f in files:
            if f.endswith('.qrc') or f.endswith('.ui'):
                file_list.append(os.path.join(root, f))

    with ProcessPoolExecutor() as executor:
        executor.map(_pythonize_pyside_file, file_list)


def _pythonize_pyside_file(filepath):
    logger.info('File: %s', filepath)
    path, ext = os.path.splitext(filepath)
    try:
        if ext == '.qrc':
            new_path = '%s_rc.py' % path
            subprocess.check_output(
                ['pyside-rcc', '-py3', filepath, '-o', new_path])
        elif ext == '.ui':
            new_path = '%s_ui.py' % path
            subprocess.check_output(
                ['pyside-uic', '--from-imports', filepath, '-o', new_path])
        else:
            logger.warning('Unknown extension')
    except Exception as e:
        logger.critical(str(e))


@task
def win_exe():
    """Build an windows executable"""
    os.system('python freeze.py build_exe')


@task(pre=[win_exe])
def win_installer():
    """Create a windows application installer"""
    print('Make sure the Innosetup program folder is in your PATH!')
    os.system('iscc InnoSetup.iss')


@task
def test():
    """Run unittests"""
    python = 'python' if sys.platform.startswith('win') else 'python3'
    os.system(python + ' -m unittest discover')
