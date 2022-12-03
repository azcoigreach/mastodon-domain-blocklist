from setuptools import setup

setup(
    name="tools",
    version="0.1.0",
    py_modules=["tools"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        tools=tools:cli
    """,
)