# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import divider

DEBUG = True if __name__ == '__main__' else False

"""Protected variation sounds a lot like indirection and information hiding,
but it is tied to the idea of consolidating disparate objects/resources.

In this sense, it acts more like the general idea of abstraction,
because A. it does not necessarily (though often may, tangentially) provide
mechanisms for pluggable behavior, and B. it does not necessarily
hide all access to information. What it does do, is group disparate systems
into one single entity, to protect the variation and thus remove coupling
to specific implementations.

In this sense, it feels a lot like an adapter, but it's more like a
multi-adapter in that sense, so it's not quite the same.

My ultimate conclusion is that these other similar design patterns are
effectively subclasses of this idea, which is the most abstract version."""


class PostgresSQLAdapter:

    def conn(self):
        print('Getting conn')
        return self

    def cursor(self):
        print('Getting cursor')
        return self

    def execute(self, sql):
        print('Executing SQL: `{}`'.format(sql))
        return self

    def commit(self):
        pass


class MongoAdapter:

    def collections(self):
        def get(pk):
            print('Getting collection: pk {}'.format(pk))
        return {'get': get}


class ConnectionMixin:
    """Abstracts the notion of a document across all database types.
    This ones' is a weird experimentation."""

    def __init__(self):
        self.db = {'name': None, 'adapter': None}

    def set_adapter(self, name):
        self.db['name'] = name
        if self.db['name'] == 'mongo':
            self.db['adapter'] = MongoAdapter()
        elif self.db['name'] == 'postgres':
            self.db['adapter'] = PostgresSQLAdapter()

    def get(self, pk):
        if self.db['name'] == 'mongo':
            collections = self.db['adapter'].collections()
            return collections['get'](pk)
        elif self.db['name'] == 'postgres':
            sql = """SELECT * FROM documents doc
                  WHERE doc.id == {} LIMIT;""".format(pk)
            self.db['adapter'].conn().cursor().execute(sql).commit()


class Document(ConnectionMixin):
    pass


if DEBUG:
    with Section('GRASP protected variation pattern'):
        doc = Document()
        doc.set_adapter('mongo')
        doc.get(991)
        divider(newline=False)
        doc.set_adapter('postgres')
        doc.get(991)
