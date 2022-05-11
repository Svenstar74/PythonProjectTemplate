from setuptools import setup


setup(
    name="roman_numerals",
    description="Kata challenge for 'To Roman Numerals'",
    author="Sven Firmbach",
    install_requires=[
        "setuptools>=42.0",
        "wheel"
    ],
    packages=[
        "roman_numerals"
    ],
    package_dir={"": "src"},
    extras_require={
        'dev': [
            'pytest'
        ]
    }
)
