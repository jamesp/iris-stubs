from distutils.core import setup
import os

name = "scitools-iris-stubs"

def find_stub_files(name):
    result = []
    for root, dirs, files in os.walk(name):
        for file in files:
            if file.endswith('.pyi'):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
    return result

setup(
    name=name,
    version="0.0.1.dev1",
    author="SciTools",
    #package_data={"": find_stub_files(name)},
    packages=['iris-stubs'],
    install_requires=['scitools-iris>3']
)