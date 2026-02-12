from setuptools import setup, find_packages

def get_requirements(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


setup(
    name="wine_ml",
    version="0.0.1",
    description="ML project",
    author="ermias",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements("requirements.txt")
    
)