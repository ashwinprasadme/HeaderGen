from tensorflow.python.distribute import distribution_strategy_context as distribution_strategy_context
from tensorflow.python.lib.io import file_io as file_io

def write_dirpath(dirpath, strategy): ...
def remove_temp_dirpath(dirpath, strategy) -> None: ...
def write_filepath(filepath, strategy): ...
def remove_temp_dir_with_filepath(filepath, strategy) -> None: ...
