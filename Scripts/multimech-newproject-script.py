#!c:\python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'multi-mechanize==1.2.0.1','console_scripts','multimech-newproject'
__requires__ = 'multi-mechanize==1.2.0.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('multi-mechanize==1.2.0.1', 'console_scripts', 'multimech-newproject')()
    )
