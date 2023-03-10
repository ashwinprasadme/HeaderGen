from typing import Any

class _Config:
    conf_nocache: bool
    conf_noopt: bool
    conf_cache_factors: Any
    conf_tmp_path: Any
    conf_check_path: Any
    conf_target_groups: Any
    conf_c_prefix: str
    conf_c_prefix_: str
    conf_cc_flags: Any
    conf_min_features: Any
    conf_features: Any
    def conf_features_partial(self): ...
    def __init__(self) -> None: ...

class _Distutils:
    def __init__(self, ccompiler) -> None: ...
    def dist_compile(self, sources, flags, ccompiler: Any | None = ..., **kwargs): ...
    def dist_test(self, source, flags, macros=...): ...
    def dist_info(self): ...
    @staticmethod
    def dist_error(*args) -> None: ...
    @staticmethod
    def dist_fatal(*args) -> None: ...
    @staticmethod
    def dist_log(*args, stderr: bool = ...) -> None: ...
    @staticmethod
    def dist_load_module(name, path): ...

class _Cache:
    cache_me: Any
    cache_private: Any
    cache_infile: bool
    def __init__(self, cache_path: Any | None = ..., *factors) -> None: ...
    def __del__(self) -> None: ...
    def cache_flush(self) -> None: ...
    def cache_hash(self, *factors): ...
    @staticmethod
    def me(cb): ...

class _CCompiler:
    cc_noopt: bool
    cc_is_gcc: bool
    cc_march: str
    cc_name: str
    cc_flags: Any
    cc_is_cached: bool
    def __init__(self) -> None: ...
    def cc_test_flags(self, flags): ...
    def cc_normalize_flags(self, flags): ...

class _Feature:
    feature_supported: Any
    feature_min: Any
    feature_is_cached: bool
    def __init__(self) -> None: ...
    def feature_names(self, names: Any | None = ..., force_flags: Any | None = ..., macros=...): ...
    def feature_is_exist(self, name): ...
    def feature_sorted(self, names, reverse: bool = ...): ...
    def feature_implies(self, names, keep_origins: bool = ...): ...
    def feature_implies_c(self, names): ...
    def feature_ahead(self, names): ...
    def feature_untied(self, names): ...
    def feature_get_til(self, names, keyisfalse): ...
    def feature_detect(self, names): ...
    def feature_flags(self, names): ...
    def feature_test(self, name, force_flags: Any | None = ..., macros=...): ...
    def feature_is_supported(self, name, force_flags: Any | None = ..., macros=...): ...
    def feature_can_autovec(self, name): ...
    def feature_extra_checks(self, name): ...
    def feature_c_preprocessor(self, feature_name, tabs: int = ...): ...

class _Parse:
    parse_baseline_names: Any
    parse_baseline_flags: Any
    parse_dispatch_names: Any
    parse_target_groups: Any
    parse_is_cached: bool
    def __init__(self, cpu_baseline, cpu_dispatch) -> None: ...
    def parse_targets(self, source): ...

class CCompilerOpt(_Config, _Distutils, _Cache, _CCompiler, _Feature, _Parse):
    sources_status: Any
    hit_cache: Any
    def __init__(self, ccompiler, cpu_baseline: str = ..., cpu_dispatch: str = ..., cache_path: Any | None = ...) -> None: ...
    def is_cached(self): ...
    def cpu_baseline_flags(self): ...
    def cpu_baseline_names(self): ...
    def cpu_dispatch_names(self): ...
    def try_dispatch(self, sources, src_dir: Any | None = ..., ccompiler: Any | None = ..., **kwargs): ...
    def generate_dispatch_header(self, header_path) -> None: ...
    def report(self, full: bool = ...): ...

def new_ccompiler_opt(compiler, dispatch_hpath, **kwargs): ...
