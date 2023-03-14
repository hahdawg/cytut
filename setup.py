from os.path import join
from pathlib import Path
from setuptools import Extension, setup
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy as np

root = Path(__file__).parent.resolve()
src = join(root, "src", "cytut")

ext_data = {
    "cytut.lib": {
        "sources": [join(src, "lib.pyx")],
        "include_dirs": [np.get_include()]
    }
}

extensions = []
cmdclass = {}
for name, data in ext_data.items():
    obj = Extension(
        name,
        sources=data["sources"],
        include=data.get("include", []),
        include_dirs=data.get("include_dirs", [])
    )
    extensions.append(obj)
    cmdclass.update({"build_ext": build_ext})


setup(
    ext_modules=cythonize(extensions, compiler_directives={"language_level": "3"}),
    cmdclass=cmdclass
)
