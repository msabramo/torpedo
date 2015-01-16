from setuptools import setup, find_packages

long_description = open(
    path.join(
        path.dirname(__file__),
        'README.rst'
    )
).read()

setup(
  name='torpedo',
  version='0.0.2',
  description="A simplified interface for creating session and browser objects on top of Tor",
  long_description=long_description,
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    ],
  keywords='Tor, Scraping, Crawling',
  author='Brian Abelson',
  author_email='brian@enigma.io',
  url='http://github.com/abelsonlive/torpedo',
  license='MIT',
  packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
  namespace_packages=[],
  include_package_data=False,
  zip_safe=False,
  install_requires=[
    'requesocks',
    'selenium'
  ],
  tests_require=[],
  entry_points={
    }
)
