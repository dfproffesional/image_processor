from setuptools import setup, find_packages

setup(
    name='imagecv2-processor',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'imagecv2-processor=project.cli:main',
        ],
    },
    install_requires=[
        'numpy==2.0.1',
        'opencv-python-headless==4.10.0.84',
        'argparse==1.4.0',
        'Pillow==8.3.2',
    ],
)