import setuptools

setuptools.setup(
    version='1.0.0',
    name='mbse',
    packages=['mbse'],
    entry_points={
        'console_scripts': [
            'mbse-pwfix = mbse.cmd.pwfix:main',
        ],
    }
)
