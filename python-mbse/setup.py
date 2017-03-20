import setuptools

setuptools.setup(
    version='1.0.0',
    name='mbse',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'mbse-pwfix = mbse.cmd.pwfix:main',
        ],
    }
)
