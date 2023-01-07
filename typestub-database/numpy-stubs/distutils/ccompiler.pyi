from numpy.distutils import log as log
from numpy.distutils.exec_command import filepath_from_subprocess_output as filepath_from_subprocess_output, forward_bytes_to_stdout as forward_bytes_to_stdout
from numpy.distutils.misc_util import cyg2win32 as cyg2win32, get_num_build_jobs as get_num_build_jobs, is_sequence as is_sequence, mingw32 as mingw32
from typing import Any

def replace_method(klass, method_name, func): ...
def CCompiler_find_executables(self) -> None: ...
def CCompiler_spawn(self, cmd, display: Any | None = ...) -> None: ...
def CCompiler_object_filenames(self, source_filenames, strip_dir: int = ..., output_dir: str = ...): ...
def CCompiler_compile(self, sources, output_dir: Any | None = ..., macros: Any | None = ..., include_dirs: Any | None = ..., debug: int = ..., extra_preargs: Any | None = ..., extra_postargs: Any | None = ..., depends: Any | None = ...): ...
def CCompiler_customize_cmd(self, cmd, ignore=...): ...
def CCompiler_show_customization(self) -> None: ...
def CCompiler_customize(self, dist, need_cxx: int = ...) -> None: ...
def simple_version_match(pat: str = ..., ignore: str = ..., start: str = ...): ...
def CCompiler_get_version(self, force: bool = ..., ok_status=...): ...
def CCompiler_cxx_compiler(self): ...