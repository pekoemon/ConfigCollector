from setuptools import setup

setup(
    name='ConfigCollector',
    version='0.1.0',
    description='The tool collects configuration file of multiple routers',
    author='Taiji Tsuchiya',
    author_email='tuty0630@gmail.com',
    license='MIT',
    packages=[
        'configcollector',
    ],
    keywords='network router cisco juniper junos ios ios-xr ios-xe',
    include_package_data=True,
    install_requires=[
        'Exscript',
    ],
    entry_points="""
        [console_scripts]
        configcollector = configcollector:main
        """,
)