from setuptools import setup

setup(
    name="list-builder",
    version="0.1.0",
    py_modules=["list-builder"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        list-builder=list-builder:cli
    """,
)