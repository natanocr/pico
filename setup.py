from setuptools import setup

version = '2.0.0-dev'

setup(
    name='pico',
    version=version,
    description='Pico Web Application Framework',
    author='Fergal Walsh',
    url='http://github.com/fergalwalsh/pico',
    download_url='https://github.com/fergalwalsh/pico/tarball/%s' % version,
    packages=['pico'],
    test_suite='nose2.collector.collector',
    install_requires=['wrapt >= 1.8.0', 'Werkzeug >= 0.11.4', 'requests >= 2.9.1'],
)
