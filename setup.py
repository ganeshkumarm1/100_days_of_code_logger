from setuptools import setup

setup(
    name = "100-days-of-code-logger",
    version = 1.0,
    description = "Python logger to commit log to 100 days of code repo",
    author = "Ganesh Kumar M",
    author_email = "ganeshkumarm.1996@gmail.com",
    license = "MIT",
    url = "https://github.com/GaneshmKumar/100_days_of_code_logger",
    packages = ["logger"],
    entry_points={
        'console_scripts':[
            'logger = logger.logger:main'
            ]
        }
)