import os
from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->list[str]:
   '''
   This function will return the list of requirements
   ''' 
   requirements=[]
   Hypen_E_dot='-e.'
   with open(file_path) as file_Obj:
        requirements=file_Obj.readlines()  
        [req.replace('\n',"") for req in requirements]
        if Hypen_E_dot in requirements:
           requirements.remove(Hypen_E_dot)
           os.close()
   return requirements
          




setup( 
      name='ml_project',
      version='0.0.1',
      author='Chanchal_Narang',
      author_email='narangchanchal4@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements('requirement.txt'),
      
)