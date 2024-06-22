import inspect

import requests
from pprint import pprint


def introspection_info(obj):
    return ({"type": type(obj),
             "attributes": dir(obj),
             "methods": inspect.getmembers(obj),
             "module": inspect.getmodule(obj),
             "isinstance": isinstance(obj, list),
             "id": id(obj)})


number_info = introspection_info(42)
print(number_info)
