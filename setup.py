"""Install arXiv-base as an importable package."""

from setuptools import setup, find_packages


setup(
    name='arxiv-base',
    version='0.14.3rc3',
    packages=[f'arxiv.{package}' for package
              in find_packages('arxiv', exclude=['*test*'])],
    zip_safe=False,
    install_requires=[
        'flask',
        'jsonschema',
        'pytz',
        'uwsgi',
        'boto3',
        'bleach==3.1.0'
    ],
    include_package_data=True
)
