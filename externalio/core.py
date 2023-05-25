"""
IO support for fictitious externalio format.
"""
from dascore.io.core import FiberIO


class ExternalIOV1(FiberIO):
    """
    An IO class supporting version 1 of the jingle format.
    """

    # you must specify the format name using the name attribute
    name = "externalio"
    # you can also define which file extensions are expected like so.
    # this will speed up determining the formats of files if not specified.
    preferred_extensions = ("eio",)
    # also specifying a version is good practice so when version 2 is
    # released you can just make another class in the same module named
    # ExternalIOV2.
    version = "1"

    def read(self, path, jingle_param=1, **kwargs):
        """
        Read should take a path and return a patch or sequence of patches.

        It can also define its own optional parameters, and should always
        accept kwargs. If the format supports partial reads, these should
        be implemented as well.
        """

    def get_format(self, path):
        """
        Used to determine if path is a supported jingle file.

        Returns a tuple of (format_name, file_version) if the file is a
        supported externalio file, else return False or raise a
        dascore.exceptions.UnknownFiberFormat exception.
        """

    def scan(self, path):
        """
        Used to get metadata about a file without reading the whole file.

        This should return a list of `PatchFileSummary` objects from the
        dascore.core.schema module.
        """

    def write(self, patch, path, **kwargs):
        """
        Write a patch or spool back to disk in the externalio format.
        """
