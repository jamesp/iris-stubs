import threading
from typing import Any

class Lenient(threading.local):
    def __init__(self, **kwargs: Any) -> None: ...
    def __contains__(self, key: Any): ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def context(self, **kwargs: Any) -> None: ...

class _Lenient(threading.local):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, func: Any): ...
    def __contains__(self, name: Any): ...
    def __getattr__(self, name: Any): ...
    def __getitem__(self, name: Any): ...
    def __setitem__(self, name: Any, value: Any) -> None: ...
    def context(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def enable(self): ...
    @enable.setter
    def enable(self, state: Any) -> None: ...
    def register_client(self, func: Any, services: Any, append: bool = ...) -> None: ...
    def register_service(self, func: Any) -> None: ...
    def unregister_client(self, func: Any) -> None: ...
    def unregister_service(self, func: Any) -> None: ...

LENIENT: Any
