from .bzipped import opener as bzip2_opener
from .gzipped import opener as gzip_opener

__all__ = ['bzip2_opener', 'gzip_opener']