from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='Backtvt',
    version='1.0.0',
    python_requires='>=3.8, <4',
    install_requires=[
        'django',
        'djangorestframework',
        'markdown',
        'django-filter',
        'django-cors-headers',
        'dbf',
        'djangorestframework-simplejwt',
        'apscheduler',
        'psycopg2'
        ]
    
)
