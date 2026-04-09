from setuptools import find_packages, setup

package_name = 'study_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ilya3',
    maintainer_email='ilya3@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
		    'first_node = study_pkg.first_node:main',
		    'time_printer = study_pkg.time_printer:main',
		    'talker = study_pkg.talker:main',
            'listener = study_pkg.listener:main',
        ],
    },
)
