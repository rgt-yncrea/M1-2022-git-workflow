from setuptools import setup 
from setuptools import find_packages
#with open('README.md') asf:
#readme = f.read() 
from pathlib import Path 
this_directory = Path(__file__).parent 
long_description = (this_directory / "README.md").read_text()
setup(
name='BIN_Converter',
version='1.0.0',
#long_description=readme,
long_description=long_description, 
long_description_content_type='text/markdown',
author='salma temsamani',
author_email='salma.temsamani@isen.yncrea.fr',
url='https://github.com/Salmatemsamani/M1-2022-git-workflow', 
packages=find_packages(),
entry_points={ 
  'console_script':[ 
    'hello-world-cli = M1-2022-git-workflow.main:say_hello',
  ], 
}, 
)
