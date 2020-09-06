from setuptools import setup,find_packages

setup(
    name = "tools",
    description = "this is tools packer",
    author = "melody",
    author_email = "melody.0108@qq.com",
    version = "1.2.3",
    url = 'http://www.melodyspace.cn',
    packages = find_packages(),
    install_requires = [
        'requests>=2.23.0',
        'pymmh3>=0.0.4',
        
    ],
    py_modules = ['tools.faviconhash']

)