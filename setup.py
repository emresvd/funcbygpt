from setuptools import setup, find_packages
import codecs

with codecs.open("README.md", "r", "utf-8") as f:
    long_description = f.read()

setup(
    name='funcbygpt',
    version='0.0.2',
    description='tell the function what to do and gpt will write the code',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='emresvd',
    license='MIT',
    url='https://github.com/emresvd/funcbygpt',
    packages=find_packages(),
    install_requires=[
        'openai==0.27.2',
        'python-dotenv==0.21.1',
    ],
    keywords=[
        "gpt",
        "openai",
        "wrapper",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Operating System :: OS Independent",
    ],
)
