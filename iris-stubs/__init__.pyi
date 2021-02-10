from iris.cube import Cube, CubeList
import iris.io
import threading
from iris._deprecation import IrisDeprecation as IrisDeprecation
from typing import Any, Iterable, Optional, TYPE_CHECKING, Union

from iris._constraints import Constraint, AttributeConstraint, NameConstraint

class Future(threading.local):
    def __init__(self) -> None: ...
    deprecated_options: Any = ...
    def __setattr__(self, name: Any, value: Any) -> None: ...
    def context(self, **kwargs: Any) -> None: ...

FUTURE: Any
site_configuration: Any

def load(uris: Iterable[str], 
    constraints: Optional[Iterable[Constraint]] = ..., 
    callback: Optional[Any] = ...) -> CubeList: ...
def load_cube(
    uris: Union[str, Iterable[str]], 
    constraint: Optional[Iterable[Constraint]] = ..., 
    callback: Optional[Any] = ...) -> Cube: ...
def load_cubes(
    uris: Iterable[str], 
    constraints: Optional[Iterable[Constraint]] = ..., 
    callback: Optional[Any] = ...) -> CubeList: ...
def load_raw(
    uris: Iterable[str], 
    constraints: Optional[Iterable[Constraint]] = ..., 
    callback: Optional[Any] = ...) -> CubeList: ...

save = iris.io.save

def sample_data_path(*path_to_join: str) -> str: ...
