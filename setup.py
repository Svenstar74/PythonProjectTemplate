from setuptools import setup, find_packages


with open("README.md", "r") as readme:
    long_description = readme.read()


setup(
    # Metadata
    name="project_template",
    version="0.0.1",
    author="Sven Firmbach",
    author_email="sven.firmbach@outlook.de",
    description="A template for new python projects.",
    long_description="",
    long_description_content_type='text/markdown',

    # Setup and install definitions
    setup_requires=[
        "wheel"
    ],
    install_requires=[
        "setuptools>=42.0",
        "wheel"
    ],
    package_dir={"": "src"},
    packages=[
        "count_symbols",
        "roman_numerals"
    ],

    # Development extras
    extras_require={
        'dev': [
            'pytest'
        ]
    }
)
