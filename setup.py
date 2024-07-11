from setuptools import setup,find_packages
from typing import List

Hyphen_e_dot="-e ."
def get_requirements(file_path:str)->List[str]:
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace('\n','') for req in requirments]

        if Hyphen_e_dot in requirments:
            requirments.remove(Hyphen_e_dot)

    return requirments



setup(
    name='ML_2',
    version='0.0.1',
    author='irfan',
    author_emial='007irf@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') #['numpy','pandas','sklearn'],

)