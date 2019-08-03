import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='res-facenet',
    version='0.0.3',
    author='Khairul Imam',
    author_email='ki65559@gmail.com',
    description='This model has been trained on VGGv2 and tested on LFW with 92% accuracy. The pretrained model can be accessed on res_facenet.model_921 or res_facenet.model_920',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/khrlimam/res-facenet",
    packages=setuptools.find_packages(),
    install_requires=['torch', 'torchvision'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
