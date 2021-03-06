from setuptools import setup, find_packages

setup(
    name='jmbo-superhero',
    version='0.1',
    description='Jmbo superhero application.  A content type that represents a bundle of HTML, JS and CSS on the filesystem.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/jmbo-superhero',
    packages = find_packages(),
    install_requires = [
        'jmbo>=1.1.1',
    ],
    tests_require=[
        'django-setuptest>=0.1.4',
    ],
    test_suite='setuptest.setuptest.SetupTestSuite',
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
