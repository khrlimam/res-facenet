import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='facenet-khairulimam',
    version='0.0.1',
    author='Khairul Imam',
    author_email='ki65559@gmail.com',
    description='This model has been trained on VGGv2 and tested on LFW with 92% accuracy.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/khrlimam/res-facenet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
