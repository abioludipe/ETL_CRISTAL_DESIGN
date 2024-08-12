from setuptools import setup

setup(name='etl',
      version='0.0.1',
      description='Data ETL tool',
      author='Abimbola Oludipe',
      author_email='ao.oludipe@gmail.com',
      packages=['etl'],
      install_requires=['pandas==2.2.2',
'numpy==1.26.0',
'logging==0.4.9.6',
'setuptools==72.1.0'])