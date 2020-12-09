import setuptools
import re
import io

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with io.open("version.py", encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

setuptools.setup(
    name="pydilha", # Replace with your own username
    version=version,
    author="Rafael Padilha",
    author_email="rafaelpadilha@hotmail.com.br",
    description="A simple bot for fun with friends on discord servers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)