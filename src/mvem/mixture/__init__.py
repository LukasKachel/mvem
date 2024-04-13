import pkgutil
import importlib.util

__all__ = []
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    __all__.append(module_name)
    _module_spec = loader.find_spec(module_name)
    _module = importlib.util.module_from_spec(_module_spec)
    _module_spec.loader.exec_module(_module)
    globals()[module_name] = _module