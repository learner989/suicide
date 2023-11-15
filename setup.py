from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        lines = [line.strip() for line in file_obj.readlines() if not line.startswith('-e')]
        requirements = [line for line in lines if line]  # Remove empty lines
    return requirements

setup(
    name='mental_health',
    version='3.9.12',
    author='Meher',
    author_email='meher09@gmail.com',
    description='Your project description here',
    packages=find_packages(exclude=['tests']),
    install_requires=get_requirements('requirements.txt')
)
