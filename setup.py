from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)-> List[str]:
    # This function will return all list of requirement
    # Moreover the -e . will help in invoking the setup.py file 
    # wihile running pip install -r requiremnts.txt

    requirements = []
    with open(file_path) as file_obj:
        requirments = file_obj.readline()
        requirements = [req.replace('\n','') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements

# setup the package

setup(
    name="Student performance Index",
    version='0.0.1',
    author="Adithya",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)
    

