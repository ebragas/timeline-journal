"""Timeline API exceptions"""

class EntryNotFoundException(Exception):
    """Raised when selecting an entry by ID and none is found with a matching
    identifier."""
    pass
