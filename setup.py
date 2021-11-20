from setuptools import setup

setup(
    name='tracevec',
    version='1.0',
    description='Learning word embedding models based on the electrical consumption of various home appliances.',
    author='Matic Pintarič, Sašo Karakatič',
    author_email='matic.pintaric@outlook.com',
    url='https://github.com/mpinta/tracevec',
    license='MIT',
    install_requires=[
        'numpy',
        'scipy',
        'torch',
        'pandas',
        'seaborn',
        'matplotlib',
        'scikit_learn',
        'gensim==3.8.3',
        'matplotlib_venn==0.11.6'
    ]
)
