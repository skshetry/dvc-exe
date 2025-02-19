import git
import os
import pathlib
import posixpath
import shutil


VERSION = "3.48.4"
URL = "https://github.com/iterative/dvc"

path = pathlib.Path(__file__).parent.absolute()
dvc = path / "dvc"

try:
    shutil.rmtree(dvc)
except FileNotFoundError:
    pass

# NOTE: need full git clone for version detection
# by setuptools-scm
repo = git.Repo.clone_from(URL, dvc)
repo.git.checkout(VERSION)


