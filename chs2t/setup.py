try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'Convert chs to cht',
        'author': 'TCT',
        'url': 'htts://www.github.com/dTCTb/chs2t.git',
        'author_email': 'tctdonaldtang@gmail.com',
        'version': '0.1',
        'install_requires': [''],
        'packages': ['chs2t'],
        'scripts': [],
        'name': 'chs2t'
        }

setup(**config)
