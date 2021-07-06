from setuptools import setup
release_version = '<PLACE_HOLDER_RELEASE_VERSION>'

setup(
    name='perfecto-py3',
    packages=['perfecto-py3','perfecto-py3/client', 'perfecto-py3/Exceptions', 'perfecto-py3/model', 'perfecto-py3/test'],  # this must be the same as the name above
    package_data = {'': ['*.txt']},
	version=release_version,
    description='Perfecto Reporting SDK for Python\nPerfecto Reporting is a multiple execution digital report, Add personalized logical steps and tags according to your team and organization.\n For release notes see: https://github.com/PerfectoCode/Samples/blob/master/Reporting/README.md',
    author='Perfecto',
    author_email='perfecto@perfectomobile.com',
    url='https://github.com/PerfectoCode',  # use the URL to the GitHub repo
    download_url='https://github.com/PerfectoCode',
    keywords=['Perfecto', 'PerfectoMobile', 'Reporting', 'Selenium', 'Appium', 'Automation testing'],
    classifiers=[ 'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent']
        
)
