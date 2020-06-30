import setuptools

setuptools.setup(
    name='env-file',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
