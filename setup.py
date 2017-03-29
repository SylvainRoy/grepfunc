from distutils.core import setup
setup(
  name = 'grepfunc',
  packages = ['grepfunc'],
  package_data = {'grepfunc' : ["*.py", "README.md"], },
  version = '1.0.0',
  description = 'Unix\'s grep, as a Python function.',
  author = 'Ronen Ness',
  author_email = 'ronenness@gmail.com',
  url = 'https://github.com/RonenNess/grepfunc',
  download_url = 'https://github.com/RonenNess/grepfunc/tarball/1.0.0',
  keywords = ['grep', 'regex', 'filter', 'search'],
  classifiers = [],
)