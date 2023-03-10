from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

def as_string(input, precision: int = ..., scientific: bool = ..., shortest: bool = ..., width: int = ..., fill: str = ..., name: Any | None = ...): ...

AsString: Any

def as_string_eager_fallback(input, precision, scientific, shortest, width, fill, name, ctx): ...
def decode_base64(input, name: Any | None = ...): ...

DecodeBase64: Any

def decode_base64_eager_fallback(input, name, ctx): ...
def encode_base64(input, pad: bool = ..., name: Any | None = ...): ...

EncodeBase64: Any

def encode_base64_eager_fallback(input, pad, name, ctx): ...
def reduce_join(inputs, reduction_indices, keep_dims: bool = ..., separator: str = ..., name: Any | None = ...): ...

ReduceJoin: Any

def reduce_join_eager_fallback(inputs, reduction_indices, keep_dims, separator, name, ctx): ...
def regex_full_match(input, pattern, name: Any | None = ...): ...

RegexFullMatch: Any

def regex_full_match_eager_fallback(input, pattern, name, ctx): ...
def regex_replace(input, pattern, rewrite, replace_global: bool = ..., name: Any | None = ...): ...

RegexReplace: Any

def regex_replace_eager_fallback(input, pattern, rewrite, replace_global, name, ctx): ...
def static_regex_full_match(input, pattern, name: Any | None = ...): ...

StaticRegexFullMatch: Any

def static_regex_full_match_eager_fallback(input, pattern, name, ctx): ...
def static_regex_replace(input, pattern, rewrite, replace_global: bool = ..., name: Any | None = ...): ...

StaticRegexReplace: Any

def static_regex_replace_eager_fallback(input, pattern, rewrite, replace_global, name, ctx): ...
def string_format(inputs, template: str = ..., placeholder: str = ..., summarize: int = ..., name: Any | None = ...): ...

StringFormat: Any

def string_format_eager_fallback(inputs, template, placeholder, summarize, name, ctx): ...
def string_join(inputs, separator: str = ..., name: Any | None = ...): ...

StringJoin: Any

def string_join_eager_fallback(inputs, separator, name, ctx): ...
def string_length(input, unit: str = ..., name: Any | None = ...): ...

StringLength: Any

def string_length_eager_fallback(input, unit, name, ctx): ...
def string_lower(input, encoding: str = ..., name: Any | None = ...): ...

StringLower: Any

def string_lower_eager_fallback(input, encoding, name, ctx): ...

class _StringNGramsOutput(NamedTuple):
    ngrams: Any
    ngrams_splits: Any

def string_n_grams(data, data_splits, separator, ngram_widths, left_pad, right_pad, pad_width, preserve_short_sequences, name: Any | None = ...): ...

StringNGrams: Any

def string_n_grams_eager_fallback(data, data_splits, separator, ngram_widths, left_pad, right_pad, pad_width, preserve_short_sequences, name, ctx): ...

class _StringSplitOutput(NamedTuple):
    indices: Any
    values: Any
    shape: Any

def string_split(input, delimiter, skip_empty: bool = ..., name: Any | None = ...): ...

StringSplit: Any

def string_split_eager_fallback(input, delimiter, skip_empty, name, ctx): ...

class _StringSplitV2Output(NamedTuple):
    indices: Any
    values: Any
    shape: Any

def string_split_v2(input, sep, maxsplit: int = ..., name: Any | None = ...): ...

StringSplitV2: Any

def string_split_v2_eager_fallback(input, sep, maxsplit, name, ctx): ...
def string_strip(input, name: Any | None = ...): ...

StringStrip: Any

def string_strip_eager_fallback(input, name, ctx): ...
def string_to_hash_bucket(string_tensor, num_buckets, name: Any | None = ...): ...

StringToHashBucket: Any

def string_to_hash_bucket_eager_fallback(string_tensor, num_buckets, name, ctx): ...
def string_to_hash_bucket_fast(input, num_buckets, name: Any | None = ...): ...

StringToHashBucketFast: Any

def string_to_hash_bucket_fast_eager_fallback(input, num_buckets, name, ctx): ...
def string_to_hash_bucket_strong(input, num_buckets, key, name: Any | None = ...): ...

StringToHashBucketStrong: Any

def string_to_hash_bucket_strong_eager_fallback(input, num_buckets, key, name, ctx): ...
def string_upper(input, encoding: str = ..., name: Any | None = ...): ...

StringUpper: Any

def string_upper_eager_fallback(input, encoding, name, ctx): ...
def substr(input, pos, len, unit: str = ..., name: Any | None = ...): ...

Substr: Any

def substr_eager_fallback(input, pos, len, unit, name, ctx): ...

class _UnicodeDecodeOutput(NamedTuple):
    row_splits: Any
    char_values: Any

def unicode_decode(input, input_encoding, errors: str = ..., replacement_char: int = ..., replace_control_characters: bool = ..., Tsplits=..., name: Any | None = ...): ...

UnicodeDecode: Any

def unicode_decode_eager_fallback(input, input_encoding, errors, replacement_char, replace_control_characters, Tsplits, name, ctx): ...

class _UnicodeDecodeWithOffsetsOutput(NamedTuple):
    row_splits: Any
    char_values: Any
    char_to_byte_starts: Any

def unicode_decode_with_offsets(input, input_encoding, errors: str = ..., replacement_char: int = ..., replace_control_characters: bool = ..., Tsplits=..., name: Any | None = ...): ...

UnicodeDecodeWithOffsets: Any

def unicode_decode_with_offsets_eager_fallback(input, input_encoding, errors, replacement_char, replace_control_characters, Tsplits, name, ctx): ...
def unicode_encode(input_values, input_splits, output_encoding, errors: str = ..., replacement_char: int = ..., name: Any | None = ...): ...

UnicodeEncode: Any

def unicode_encode_eager_fallback(input_values, input_splits, output_encoding, errors, replacement_char, name, ctx): ...
def unicode_script(input, name: Any | None = ...): ...

UnicodeScript: Any

def unicode_script_eager_fallback(input, name, ctx): ...
def unicode_transcode(input, input_encoding, output_encoding, errors: str = ..., replacement_char: int = ..., replace_control_characters: bool = ..., name: Any | None = ...): ...

UnicodeTranscode: Any

def unicode_transcode_eager_fallback(input, input_encoding, output_encoding, errors, replacement_char, replace_control_characters, name, ctx): ...
def unsorted_segment_join(inputs, segment_ids, num_segments, separator: str = ..., name: Any | None = ...): ...

UnsortedSegmentJoin: Any

def unsorted_segment_join_eager_fallback(inputs, segment_ids, num_segments, separator, name, ctx): ...
