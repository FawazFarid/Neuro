from setuptools import setup

setup(
    name="Neuro",
    version="1.0.0",
    py_modules=['app.py'],
    install_requires=['Click'],

    entry_points="""
        [console_scripts]
        neuro=cli:cli
    """
)
