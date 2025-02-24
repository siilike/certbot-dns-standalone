from setuptools import setup
from setuptools import find_packages

with open('README.rst') as file:
    long_description = file.read()

version = '1.2.1'

# Remember to update local-oldest-requirements.txt when changing the minimum
# acme/certbot version.
install_requires = [
    'acme>=0.21.1',
    'certbot>=3.0.0',
    'dnslib>=0.9.0',
    'mock',
    'setuptools',
]

docs_extras = [
    'Sphinx>=1.0',  # autodoc_member_order = 'bysource', autodoc_default_flags
    'sphinx_rtd_theme',
]

setup(
    name='certbot-dns-standalone',
    version=version,
    description="Standalone DNS Authenticator plugin for Certbot",
    url='https://github.com/siilike/certbot-dns-standalone',
    author="Lauri Keel",
    license='Apache License 2.0',
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    long_description=long_description,
    long_description_content_type='text/x-rst',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'docs': docs_extras,
    },
    entry_points={
        'certbot.plugins': [
            'dns-standalone = certbot_dns_standalone.dns_standalone:Authenticator',
        ],
    },
    test_suite='certbot_dns_standalone',
)
