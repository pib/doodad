from setuptools import setup, find_packages

dependency_links = [l.strip()
                    for l in open('test_requirements.txt').readlines()]

setup(
    name='doodad',
    version='0.1',
    packages=find_packages(),

    dependency_links=dependency_links,

    tests_require=['nose==1.3.0', 'nose-machineout==0.4-rc1'],
    test_suite='nose.collector',
)
