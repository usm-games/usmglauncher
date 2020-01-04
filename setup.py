from setuptools import setup

setup(
    name="usmgames-launcher",
    version="0.0.1",
    description="Launcher for USM Games projects. Made for Nerdonomicon 2019, Valparaíso, Chile",
    author="USM Games",
    author_email="usmgames@gmail.com",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    include_package_data=True,
    install_requires=[
        "flask==1.1.1",
    ],
    entry_points={"console_scripts": ["usmglauncher=usmglauncher.__main__:main"]},
)