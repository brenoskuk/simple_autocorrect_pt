import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_autocorrect_pt",
    version="0.0.1",
    author="Breno Skuk",
    author_email="breno.skuk@gmail.com",
    description="Autocorrect to be used in the pipeline of rasa that corrects PT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brenoskuk/simple_autocorrect_pt",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved ::  License",
        "Operating System :: OS Independent",
    ]
)