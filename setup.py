import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="trello_client-domrachr",
    version="0.0.1",
    author="Ruslan",
    author_email="domrachr@gmail.com",
    description="D1 - Homework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/domrachr/D1-HW",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", ],
    python_requires='>=3.6',
)
