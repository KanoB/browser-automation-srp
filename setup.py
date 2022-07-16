from setuptools import setup
from setuptools import find_packages

setup(
    name='webtester',
    version='0.0.1',
    description='Sample package that performs browser automation with Selenium + Python',
    author='Claudio Canseco',
    author_email='claudio.canseco@gmail.com',
    url='https://github.com/KanoB/webtester',
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=[
        'selenium',
    ],
    setup_requires=['pytest-runner', 'flake8'],
    tests_require=['pytest'],
    # entry_points={
    #     'console_scripts': ['my-command=exampleproject.example:main']
    # },
)