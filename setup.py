from setuptools import setup, find_packages

setup(
  name='tor_tools',
  version='0.0.1',
  description="",
  long_description="",
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    ],
  keywords='',
  author='Brian Abelson',
  author_email='brian@enigma.io',
  url='http://github.com/bibliotech/tor-tools',
  license='MIT',
  packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
  namespace_packages=[],
  include_package_data=False,
  zip_safe=False,
  install_requires=[
    'requests',
    'pyvirtualdisplay',
    'stem',
    'selenium'
  ],
  tests_require=[],
  entry_points={
    }
)
