from setuptools import find_packages, setup

version = '1.3.0'

setup(name='safe_logger',
      version=version,
      description="Safe TimedRotatingFileHandler for concurrent writers",
      long_description="""Safe TimedRotatingFileHandler for concurrent writers""",
      classifiers=[],
      keywords='logging handler concurrent',
      author='cybergrind',
      author_email='cybergrind@gmail.com',
      url='https://github.com/cybergrind/safe_logger',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests', 'old*']),
      zip_safe=False,
      install_requires=[]
      )
