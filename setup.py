from setuptools import find_packages, setup
from typing import List # to identify the list data type

H='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    using this function to access the requirements.txt and return the list of requirements
    '''
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[i.replace('\n','') for i in requirement]
        if H in requirement:
            requirement.remove(H)

setup(
    
    version='0.0.1',
    name='Project_1',
    author='kirthna',
    author_email='kirthnak7@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)