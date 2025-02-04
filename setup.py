from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''This function returns the list of requirements.'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
    # Return the requirements without modifying -e .
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
        
    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='Paarya',
    author_email='prashantaarya005@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),  # Handle the requirements list
    include_package_data=True,  # Ensure that any other necessary files are included
)
