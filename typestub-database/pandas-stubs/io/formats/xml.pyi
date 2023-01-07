from pandas._typing import CompressionOptions as CompressionOptions, FilePath as FilePath, ReadBuffer as ReadBuffer, StorageOptions as StorageOptions, WriteBuffer as WriteBuffer
from pandas.core.dtypes.common import is_list_like as is_list_like
from pandas.core.dtypes.missing import isna as isna
from pandas.core.frame import DataFrame as DataFrame
from pandas.errors import AbstractMethodError as AbstractMethodError
from pandas.io.common import get_handle as get_handle
from pandas.io.xml import get_data_from_filepath as get_data_from_filepath, preprocess_data as preprocess_data
from pandas.util._decorators import doc as doc
from typing import Union, Any

class BaseXMLFormatter:
    frame: Any
    path_or_buffer: Any
    index: Any
    root_name: Any
    row_name: Any
    na_rep: Any
    attr_cols: Any
    elem_cols: Any
    namespaces: Any
    prefix: Any
    encoding: Any
    xml_declaration: Any
    pretty_print: Any
    stylesheet: Any
    compression: Any
    storage_options: Any
    orig_cols: Any
    frame_dicts: Any
    prefix_uri: Any
    def __init__(self, frame: DataFrame, path_or_buffer: Union[FilePath, WriteBuffer[bytes], WriteBuffer[str], None] = ..., index: bool = ..., root_name: Union[str, None] = ..., row_name: Union[str, None] = ..., na_rep: Union[str, None] = ..., attr_cols: Union[list[str], None] = ..., elem_cols: Union[list[str], None] = ..., namespaces: Union[dict[Union[str, None], str], None] = ..., prefix: Union[str, None] = ..., encoding: str = ..., xml_declaration: Union[bool, None] = ..., pretty_print: Union[bool, None] = ..., stylesheet: Union[FilePath, ReadBuffer[str], ReadBuffer[bytes], None] = ..., compression: CompressionOptions = ..., storage_options: StorageOptions = ...) -> None: ...
    def build_tree(self) -> bytes: ...
    def validate_columns(self) -> None: ...
    def validate_encoding(self) -> None: ...
    def process_dataframe(self) -> dict[Union[int, str], dict[str, Any]]: ...
    def handle_indexes(self) -> None: ...
    def get_prefix_uri(self) -> str: ...
    def other_namespaces(self) -> dict: ...
    def build_attribs(self, d: dict[str, Any], elem_row: Any) -> Any: ...
    def build_elems(self, d: dict[str, Any], elem_row: Any) -> None: ...
    def write_output(self) -> Union[str, None]: ...

class EtreeXMLFormatter(BaseXMLFormatter):
    root: Any
    elem_cols: Any
    out_xml: Any
    def build_tree(self) -> bytes: ...
    def get_prefix_uri(self) -> str: ...
    def build_elems(self, d: dict[str, Any], elem_row: Any) -> None: ...
    def prettify_tree(self) -> bytes: ...
    def add_declaration(self) -> bytes: ...
    def remove_declaration(self) -> bytes: ...

class LxmlXMLFormatter(BaseXMLFormatter):
    def __init__(self, *args, **kwargs) -> None: ...
    root: Any
    elem_cols: Any
    out_xml: Any
    def build_tree(self) -> bytes: ...
    def convert_empty_str_key(self) -> None: ...
    def get_prefix_uri(self) -> str: ...
    def build_elems(self, d: dict[str, Any], elem_row: Any) -> None: ...
    def transform_doc(self) -> bytes: ...