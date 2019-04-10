from setuptools import setup

with open('README.md') as file:
    long_description = file.read()

setup(
    name='inequality_coefficients',
    packages=['inequality_coefficients'],
    version='1.0.1',
    description='Coefficients to measure inequality.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Abel 'Akronix' Serrano Juste",
    author_email='akronix5@gmail.com',
    url='https://github.com/Akronix/inequality_coefficients',
    python_requires='>=3',
    install_requires=['numpy'],
    license='GPLv3+',
    keywords='inequality coefficient index gini ratio top',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research'
    ]
)
