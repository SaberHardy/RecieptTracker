# filters.py
import logging


class ExcludePatternFilter(logging.Filter):
    def __init__(self, patterns):
        super().__init__()
        self.patterns = patterns

    def filter(self, record):
        msg = record.getMessage()
        return all(pattern not in msg for pattern in self.patterns)
