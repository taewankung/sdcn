import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.md')).read()

requires = [
    'kivy',
    ]

SCRIPT_NAME = 'sdcn'
setup(name='sdcn',
      version='0.0.1',
      description='',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: kivy",
        ],
      author='Phutthewan Yangyuenyong, Aran Khunaree, Chalermchon Saekoo',
      author_email='taewankung@gmail.com, alunnice2537@gmail.com, greanmer.tm@gmail.com',
      scripts = ['bin/%s' % SCRIPT_NAME],
      license = 'License',
      packages = find_packages(),
      url='https://github.com/taewankung/sdcn',
      keywords='sdcn',
#      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
#      tests_require=requires,
#      test_suite="nokkhum-controller",
      )

