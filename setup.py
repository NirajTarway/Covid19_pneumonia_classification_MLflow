from setuptools import setup

with open('README.md', 'r', encoding='utf-8')as f:
    long_description = f.read()

REPO_NAME='Mlflow_project_template'
AUTHOR_USER_NAME='NirajTarway'
SRC_REPO='src'
LIST_OF_REQUIREMENTS=[]

setup(
    name=REPO_NAME,
    version='0.0.1',
    author=AUTHOR_USER_NAME,
    description='a small package for MLflow app',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.dev/{AUTHOR_USER_NAME}/{REPO_NAME}',
    author_email='nirajntr@gmail.com',
    packages=[SRC_REPO],
    license='MIT',
    python_requires='>=3.6',
    install_requires=LIST_OF_REQUIREMENTS
)