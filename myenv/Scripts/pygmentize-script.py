#!c:\users\bruno.azevedo\documents\projetos\myenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Pigments==1.6','console_scripts','pygmentize'
__requires__ = 'Pigments==1.6'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('Pigments==1.6', 'console_scripts', 'pygmentize')()
    )
