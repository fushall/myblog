from warnings import warn
from flask import Blueprint

__blueprints = {}
__libcdns = {}


def fetch_blueprints() -> dict:
    return __blueprints


def fetch_libcdns() -> dict:
    return __libcdns


class MetaClass(type):
    def __new__(mcs, name, bases, attrs):
        if len(bases) == 1 and bases[0] is Library:
            mcs.register(name, attrs)
        return super().__new__(mcs, name, bases, attrs)

    @classmethod
    def register(mcs, clsname, attrs):
        module = attrs.get('__module__')
        libname = attrs.get('name')
        libfolder = attrs.get('folder')
        libcdn = attrs.get('cdn')

        if libname and libfolder and libcdn and module:
            blueprint = Blueprint(
                f'library_{libname}',
                module,
                static_folder=libfolder,
                url_prefix=f'/library/{libname}'
            )
            blueprints = fetch_blueprints()
            blueprints[libname] = blueprint

            libcdns = fetch_libcdns()
            libcdns[libname] = libcdn

        else:
            warn(f'{clsname}不符合要求')


class Library(metaclass=MetaClass):
    pass
