import setuptools

with open("README.org", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sample_hello",
    version="0.0.1",
    author="sugayu",
    author_email="author@example.com",
    description="Say hello to the world.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sugayu/sample_hello",
    project_urls={
        "Bug Tracker": "https://github.com/sugayu/sample_hello/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "sample_hello"},
    packages=['sample_hello'],
    # setuptools.find_packages(where="sample_hello"),
    entry_points={
        'console_scripts': ['pysample_hello = sample_hello.sample_hello:main']
    },
    python_requires=">=3.6",
)
