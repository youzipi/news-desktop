from distutils.core import setup
import py2exe
import sys

#this allows to run it with a simple double click.
sys.argv.append('py2exe')

py2exe_options = {
        "includes": ["sip"],
        "dll_excludes": ["MSVCP90.dll",],
        "compressed": 1,
        "optimize": 2,
        "ascii": 0,
        #"bundle_files": 3,
        }

setup(
      name = 'Teemo News for Desktop',
      version = '1.0',
      windows = ['news1.py','Ui_news1.py','spider.py'], 
      #console = ['news1.py','Ui_news1.py','spider.py'], 
      #windows = ['news1.py'], 
      zipfile = None,
      options = {'py2exe': py2exe_options}
      )
