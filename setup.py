from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='funniest_bw',
    version='0.2',
    description='a simple python project',
    long_description=long_description,
    url='http://www.xxx.com',
    author='wb',
    author_email='biaowang_88@163.com',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='sample setuptools development',
    packages=['funniest_bw'],
    install_requires=[],
    extras_require={},
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [
            'funniest_bw=funniest_bw:main',
        ]
    }
)
