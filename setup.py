from setuptools import find_packages
from setuptools import setup


setup(
    name='sll.policy',
    version='0.8.1',
    description="Turns plone site into SLL site.",
    long_description=open("README.rst").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
    ],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@inicie.net',
    url='',
    license='None-free',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['sll'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Products.PloneFormGen',
        'collective.contentleadimage',
        'five.grok',
        'hexagonit.testing',
        'inicie.cropimage',
        'setuptools',
        'sll.theme',
        'z3c.jbot',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
)
