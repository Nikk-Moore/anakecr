import os, platform

class CreateKernel():
    def __init__(self, name : str, display: str, condaexec: str, r = False, python_version="3.8",requirement_file=".requirements.txt"):
        self.name = name.lower().replace(" ", "_")
        self.display = display.title()
        self.condabin = os.path.join(condaexec, 'conda')
        self.conda_base = condaexec
        self.python_version = f"python={python_version}"
        self.operating_system = platform.system()

        self.activation = self._create_activation_conda()

    def create(self):
        os.system(f"""{self.activation}
conda create --name {self.name} {self.python_version} ipykernel
conda activate {self.name}
{os.path.join(self.conda_base, 'python')} -m ipykernel install --user --name={self.name} --display-name '{self.display}' "
""")
        print(f"Created\nkernel: {self.name}\nDisplay Name: {self.display}")
    
    def _create_activation_conda(self):
        if self.operating_system == "Linux":
            return '/bin/bash -c "source activate {self.condabin}'
    
    def install_packages(self):
        "conda install -n myenv pip"