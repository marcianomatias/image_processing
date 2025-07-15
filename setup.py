from setuptools import setup, find_packages

setup(
    name='image_processing',
    version='0.1.0',
    description='Pacote simples para processamento de imagens',
    author='Marciano Matias',
    author_email='marcianomatias1@hotmail.com',
    packages=find_packages(),
    install_requires=['Pillow'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
