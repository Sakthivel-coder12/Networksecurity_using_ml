'''
The setup.py file is an essential part of packaging and
distributing python projects. It is used by setup tools 
(or distutils in older python versions) to define the 
configuration of your project, such as its metadata,
dependencies , and more 
'''


from setuptools import find_packages,setup

from typing import List

def get_requirements():
    '''
    This function will return list of requirements 

    '''
    requirement_list:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requiremnts.txt file not found")
    
    return requirement_list

setup(
    name = "Networksecurity",
    version = "0.0.1",
    auhor = "sakthivel",
    author_email= "sakthivel790460@gmail.com",
    packages= find_packages(),
    install_requires  = get_requirements()
)

