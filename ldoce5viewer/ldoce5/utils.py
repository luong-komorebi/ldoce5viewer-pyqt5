from __future__ import absolute_import

def shorten_id(_id):
    ids = _id.split('.')
    return '.'.join(ids[2:4]) if len(ids) == 4 else _id

