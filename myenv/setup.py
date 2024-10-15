from setuptools import find_packages, setup

package_name = 'myenv'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	('share/' + package_name + '/launch', ['launch/webots_launch.py']),
	('share/' + package_name + '/worlds', ['worlds/my_world.wbt']),    
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='liam',
    maintainer_email='ljkelly4213@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
