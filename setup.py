from setuptools import setup
from setuptools import find_packages

#with open('README.md') asf:
#readme = f.read()

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
  name='decbinconverter',
  version='1.0.0',
  #long_description=readme,
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='hamid',
  author_email='fadilajouaou34@gmail.com',
  url='https://github.com/hamidajouaou/M1-2022-git-workflow',
  packages=find_packages(),
  entry_points={
    'console_script':[
      'hello-world-cli = M1_2022_git_workflow.main:say_hello',
    ],
  },
)
