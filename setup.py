from setuptools import find_packages
from setuptools import setup


setup(
    name='sll.policy',
    version='0.10',
    description="Turns plone site into SLL site.",
    long_description=open("README.rst").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
    ],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@abita.fi',
    url='http://sll.fi/',
    license='None-free',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['sll'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Products.NewSllSkin',
        'Products.PFGExtendedMailAdapter',
        'Products.PFGSelectionStringField',
        'Products.PloneFormGen',
        # 'collective.cart.core',
        # 'collective.cart.shipping',
        'collective.folderlogo',
        'collective.pfg.payment',
        'collective.pfg.showrequest',
        'collective.portlet.fblikebox',
        # 'collective.searchevent',
        'collective.sharerizer',
        'five.grok',
        'hexagonit.testing',
        # 'plone.app.theming',
        'plone.browserlayer',
        'setuptools',
        'sll.portlet',
        'sll.templates',
        'sll.theme',
        'z3c.autoinclude',
        'z3c.jbot',
    ],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
)
