from setuptools import find_packages, setup
import os
from glob import glob

package_name = "ros2_course"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        ("share/" + package_name + "/launch", glob("launch/*.py")),  # <- HOZZÁADVA
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="cillard",
    maintainer_email="cillard@todo.todo",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "turtlesim_controller = ros2_course.turtlesim_controller:main",
        ],
    },
)
