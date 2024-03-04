import setuptools 

with open("README.md", "r",encoding='utf-8') as f:
    long_description = f.read()

__version__="0.0.0"
REPO_NAME="Text-summarization-"
AUTHOR_USER_NAME="tallojarshith"
SRC_REPO="textsummarizartion"
AUTHOR_EMAIL="tallojarshith123@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/tallojarshith/Text-summarization",
    project_urls=
    {
        "Bug Tracker": "https://github.com/tallojarshith/Text-summarization/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
)
