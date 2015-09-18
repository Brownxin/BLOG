__author__ = 'Brown'
'''
    Database Operation Module
'''
import time
import uuid
import functools
import threading
import logging


class Dict(dict):
    '''
        Dict object
        Deal with input and catch exception
    '''

    def __init__(self, name=(), value=(), **kw):
        super(Dict, self).__init__(**kw)
        for i, j in zip(name, value):
            self[i] = j

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


def next_id(t=None):
    '''
    Return next id 50-char string
    t is unix timestamp, default to None using time().time
    :param t:
    :return:
    '''
    if t == None:
        t = time.time()
    return "%015d%s000" % (int(t * 1000), uuid.uuid4().hex)


def _profiling(start, sql=''):
    '''
    for sql executing period
    :param start:
    :param sql:
    :return:
    '''
    t = time.time() - start
    if t > 0.1:
        logging.warning('[PROFILING] [DB] %s: %s' % (t, sql))
    else:
        logging.info('[PROFILING] [DB] %s: %s' % (t, sql))

def DBError(Exception):
    pass
def MultiColumnsError(DBError):
    pass