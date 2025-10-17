from setuptools import setup, find_packages

setup(
    name="lokseva_prepper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pydantic",
        "python-dotenv",
        "google-adk>=0.1.0"
    ],
)
