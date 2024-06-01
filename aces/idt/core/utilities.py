"""
Common IDT Utilities
====================
"""

import contextlib
import logging
import os
import re
import shutil
import tempfile
import unicodedata
from functools import partial
from pathlib import Path
from typing import Optional

import matplotlib as mpl
import numpy as np
import scipy.stats
import xxhash

mpl.use("Agg")
logger = logging.getLogger(__name__)

__author__ = "Alex Forsythe, Joshua Pines, Thomas Mansencal"
__copyright__ = "Copyright 2022 Academy of Motion Picture Arts and Sciences"
__license__ = "Academy of Motion Picture Arts and Sciences License Terms"
__maintainer__ = "Academy of Motion Picture Arts and Sciences"
__email__ = "acessupport@oscars.org"
__status__ = "Production"

__all__ = [
    "slugify",
    "list_sub_directories",
    "mask_outliers",
    "working_directory",
]


def slugify(object_, allow_unicode=False):
    """
    Generate a *SEO* friendly and human-readable slug from given object.

    Convert to ASCII if ``allow_unicode`` is *False*. Convert spaces or
    repeated dashes to single dashes. Remove characters that aren't
    alphanumerics, underscores, or hyphens. Convert to lowercase. Also strip
    leading and trailing whitespace, dashes, and underscores.

    Parameters
    ----------
    object_ : object
        Object to convert to a slug.
    allow_unicode : bool
        Whether to allow unicode characters in the generated slug.

    Returns
    -------
    :class:`str`
        Generated slug.

    References
    ----------
    -   https://github.com/django/django/blob/\
0dd29209091280ccf34e07c9468746c396b7778e/django/utils/text.py#L400

    Examples
    --------
    >>> slugify(
    ...     " Jack & Jill like numbers 1,2,3 and 4 and silly characters ?%.$!/"
    ... )
    'jack-jill-like-numbers-123-and-4-and-silly-characters'
    """

    value = str(object_)

    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )

    value = re.sub(r"[^\w\s-]", "", value.lower())

    return re.sub(r"[-\s]+", "-", value).strip("-_")


def list_sub_directories(
    directory,
    filterers=(
        lambda path: "__MACOSX" not in path.name,
        lambda path: path.is_dir(),
    ),
):
    """
    List the sub-directories in given directory.

    Parameters
    ----------
    directory : str
        Directory to list the sub-directories from.
    filterers : array_like, optional
        List of callables used to filter the sub-directories, each callable
        takes a :class:`Path` class instance as argument and returns whether to
        include or exclude the sub-directory as a bool.

    Returns
    -------
    list
        Sub-directories in given directory.
    """

    sub_directories = [
        path
        for path in Path(directory).iterdir()
        if all(filterer(path) for filterer in filterers)
    ]

    return sub_directories


def mask_outliers(a, axis=None, z_score=3):
    """
    Return the mask for the outliers of given array :math:`a` using the
    z-score.

    Parameters
    ----------
    a : array_like
        Array :math:`a` to return the outliers mask of.
    axis : int or None, optional
        Axis along which to operate. Default is 0. If None, compute over
        the whole array `a`.
    z_score : numeric
        z-score threshold to mask the outliers.

    Returns
    -------
    NDArray
        Mask for the outliers of given array :math:`a`.
    """

    return np.abs(scipy.stats.zscore(a, axis=axis)) > z_score


@contextlib.contextmanager
def working_directory(directory):
    """
    Define a context manager that temporarily sets the current working
    directory.

    Parameters
    ----------
    directory : str
        Current working directory to set.
    """

    current_working_directory = os.getcwd()
    try:
        os.chdir(directory)
        yield
    finally:
        os.chdir(current_working_directory)


def hash_file(path):
    """
    Hash the file a given path.

    Parameters
    ----------
    path : str
        Path to the file to hash.

    Returns
    -------
    :class:`str`
        File hash.
    """

    with open(path, "rb") as input_file:
        x = xxhash.xxh3_64()
        for chunk in iter(partial(input_file.read, 2**32), b""):
            x.update(chunk)

        return x.hexdigest()


def extract_archive(archive: str, directory: Optional[str] = None):
    """
    Extract the archive to the given directory or a temporary directory.

    Parameters
    ----------
    archive : str
        Archive to extract.
    directory : str, optional known directory

    Returns
    -------
    str
        Extracted directory.
    """
    if not directory:
        directory = (
            tempfile.TemporaryDirectory().name if directory is None else directory
        )

    logger.info(
        'Extracting "%s" archive to "%s"...',
        archive,
        directory,
    )

    shutil.unpack_archive(archive, directory)
    return directory


def sort_exposure_key(key):
    """
    Sort the data keys based on the +/- exposure.

    Parameters
    ----------
    key
        The key value for the exposure

    Returns
    -------
    float
        The sorted exposure key

    """
    # Allow for the removal of non-numeric characters while
    # keeping negative sign and decimal point
    return float(re.sub(r"[^\d.-]+", "", key))


def format_key(key):
    """Format the exposure keys for serialization so they encompass the + symbol.

    Parameters
    ----------
    key
        The key value for the exposure

    Returns
    -------
    str
        The key value with or without the + symbol

    """
    # Format keys to add '+' prefix for positive keys
    key_float = float(re.sub(r"[^\d.-]+", "", key))
    if key_float > 0:
        return f"+{key_float:g}"
    else:
        return f"{key_float:g}"
