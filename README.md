# iris-stubs
Type annotations for the SciTools Iris library.

This is currently *work-in-progress* to add type information to the iris 3 public API.

## Installation

Install as a development dependency:
```cd iris-stubs
pip install -e . --no-deps
```

Once installed, IDE language servers such as PyLance used in VS Code should respect both the type stub, recognising the return types from functions, as well as the documentation and type information included in the underlying source file as well.

![image](https://user-images.githubusercontent.com/22805/114051634-2abc7c00-9885-11eb-862b-8574125b1014.png)

![image](https://user-images.githubusercontent.com/22805/114051876-66574600-9885-11eb-8390-d5d503555b61.png)
