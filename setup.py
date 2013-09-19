import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name="rasterstats",
    version="0.1",
    author="Matthew Perry",
    author_email="perrygeo@gmail.com",
    description=("Summarize geospatial raster datasets based on vector geometries"),
    license="BSD",
    keywords="gis geospatial geographic raster vector zonal statistics",
    url="https://github.com/perrygeo/python-raster-stats",
    package_dir={'': 'src'},
    packages=['rasterstats'],
    long_description=read('README.rst'),
    install_requires=[
        'shapely',
        'numpy',
        'GDAL',
        # pandas, pyproj?
    ],
    scripts=['scripts/rasterstats'],
    tests_require=['pytest', 'pyshp', 'coverage'],
    cmdclass = {'test': PyTest},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: GIS',
    ],
)
