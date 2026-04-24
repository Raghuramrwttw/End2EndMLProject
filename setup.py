from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function return list of requirements
    '''
    HYPEN_E_DOT = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            req = line.strip()

            if not req or req.startswith("#"):
                continue

            if req != HYPEN_E_DOT:
                requirements.append(req)
    
    return requirements


setup(
    name="MLproject",
    version="0.0.1",
    author="Raghuram Varma",
    author_email="raghuramvarmav05@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)





