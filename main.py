import sys
import shutil
import os

if sys.argv[-1] == "clean":
    for i in ["build", "dist", "funcbygpt.egg-info"]:
        try:
            shutil.rmtree(i)
        except FileNotFoundError:
            pass

if sys.argv[-1] == "build":
    os.system("python setup.py sdist bdist_wheel")

if sys.argv[-1] == "upload":
    os.system("twine upload dist/*")
