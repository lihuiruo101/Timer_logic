from setuptools import setup, find_packages

setup(
    name="timerapp",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'timer = timerapp.__main__:main',
        ]
    },
)
