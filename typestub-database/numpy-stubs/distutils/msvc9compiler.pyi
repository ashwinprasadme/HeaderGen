from .system_info import platform_bits as platform_bits
from distutils.msvc9compiler import MSVCCompiler as _MSVCCompiler
from typing import Any

class MSVCCompiler(_MSVCCompiler):
    def __init__(self, verbose: int = ..., dry_run: int = ..., force: int = ...) -> None: ...
    def initialize(self, plat_name: Any | None = ...) -> None: ...
    def manifest_setup_ldargs(self, output_filename, build_temp, ld_args) -> None: ...
