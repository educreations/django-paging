try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('django-paging').version
except Exception, e:
    VERSION = 'unknown'