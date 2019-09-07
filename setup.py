import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="bootcamp-sneh-sneh.koul",
    version="0.0.1",
    author="Sneh Koul",
    author_email="sneh.koul@agilicus.com",
    description="bootcamp_project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.agilicus.com/sneh.koul/bootcamp-sneh",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
