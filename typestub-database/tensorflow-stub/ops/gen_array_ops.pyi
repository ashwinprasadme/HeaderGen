from tensorflow.python.util.deprecation import deprecated_endpoints as deprecated_endpoints
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any, NamedTuple

def batch_matrix_band_part(input, num_lower, num_upper, name: Any | None = ...): ...

BatchMatrixBandPart: Any

def batch_matrix_band_part_eager_fallback(input, num_lower, num_upper, name, ctx): ...
def batch_matrix_diag(diagonal, name: Any | None = ...): ...

BatchMatrixDiag: Any

def batch_matrix_diag_eager_fallback(diagonal, name, ctx): ...
def batch_matrix_diag_part(input, name: Any | None = ...): ...

BatchMatrixDiagPart: Any

def batch_matrix_diag_part_eager_fallback(input, name, ctx): ...
def batch_matrix_set_diag(input, diagonal, name: Any | None = ...): ...

BatchMatrixSetDiag: Any

def batch_matrix_set_diag_eager_fallback(input, diagonal, name, ctx): ...
def batch_to_space(input, crops, block_size, name: Any | None = ...): ...

BatchToSpace: Any

def batch_to_space_eager_fallback(input, crops, block_size, name, ctx): ...
def batch_to_space_nd(input, block_shape, crops, name: Any | None = ...): ...

BatchToSpaceND: Any

def batch_to_space_nd_eager_fallback(input, block_shape, crops, name, ctx): ...
def bitcast(input, type, name: Any | None = ...): ...

Bitcast: Any

def bitcast_eager_fallback(input, type, name, ctx): ...
def broadcast_args(s0, s1, name: Any | None = ...): ...

BroadcastArgs: Any

def broadcast_args_eager_fallback(s0, s1, name, ctx): ...

class _BroadcastGradientArgsOutput(NamedTuple):
    r0: Any
    r1: Any

def broadcast_gradient_args(s0, s1, name: Any | None = ...): ...

BroadcastGradientArgs: Any

def broadcast_gradient_args_eager_fallback(s0, s1, name, ctx): ...
def broadcast_to(input, shape, name: Any | None = ...): ...

BroadcastTo: Any

def broadcast_to_eager_fallback(input, shape, name, ctx): ...
def check_numerics(tensor, message, name: Any | None = ...): ...

CheckNumerics: Any

def check_numerics_eager_fallback(tensor, message, name, ctx): ...
def check_numerics_v2(tensor, message, name: Any | None = ...): ...

CheckNumericsV2: Any

def check_numerics_v2_eager_fallback(tensor, message, name, ctx): ...
def concat(concat_dim, values, name: Any | None = ...): ...

Concat: Any

def concat_eager_fallback(concat_dim, values, name, ctx): ...
def concat_offset(concat_dim, shape, name: Any | None = ...): ...

ConcatOffset: Any

def concat_offset_eager_fallback(concat_dim, shape, name, ctx): ...
def concat_v2(values, axis, name: Any | None = ...): ...

ConcatV2: Any

def concat_v2_eager_fallback(values, axis, name, ctx): ...
def conjugate_transpose(x, perm, name: Any | None = ...): ...

ConjugateTranspose: Any

def conjugate_transpose_eager_fallback(x, perm, name, ctx): ...
def const(value, dtype, name: Any | None = ...): ...

Const: Any

def const_eager_fallback(value, dtype, name, ctx): ...
def debug_gradient_identity(input, name: Any | None = ...): ...

DebugGradientIdentity: Any

def debug_gradient_identity_eager_fallback(input, name, ctx): ...
def debug_gradient_ref_identity(input, name: Any | None = ...): ...

DebugGradientRefIdentity: Any

def debug_gradient_ref_identity_eager_fallback(input, name, ctx) -> None: ...
def deep_copy(x, name: Any | None = ...): ...

DeepCopy: Any

def deep_copy_eager_fallback(x, name, ctx): ...
def depth_to_space(input, block_size, data_format: str = ..., name: Any | None = ...): ...

DepthToSpace: Any

def depth_to_space_eager_fallback(input, block_size, data_format, name, ctx): ...
def dequantize(input, min_range, max_range, mode: str = ..., narrow_range: bool = ..., axis: int = ..., dtype=..., name: Any | None = ...): ...

Dequantize: Any

def dequantize_eager_fallback(input, min_range, max_range, mode, narrow_range, axis, dtype, name, ctx): ...
def diag(diagonal, name: Any | None = ...): ...

Diag: Any

def diag_eager_fallback(diagonal, name, ctx): ...
def diag_part(input, name: Any | None = ...): ...

DiagPart: Any

def diag_part_eager_fallback(input, name, ctx): ...
def edit_distance(hypothesis_indices, hypothesis_values, hypothesis_shape, truth_indices, truth_values, truth_shape, normalize: bool = ..., name: Any | None = ...): ...

EditDistance: Any

def edit_distance_eager_fallback(hypothesis_indices, hypothesis_values, hypothesis_shape, truth_indices, truth_values, truth_shape, normalize, name, ctx): ...
def empty(shape, dtype, init: bool = ..., name: Any | None = ...): ...

Empty: Any

def empty_eager_fallback(shape, dtype, init, name, ctx): ...
def ensure_shape(input, shape, name: Any | None = ...): ...

EnsureShape: Any

def ensure_shape_eager_fallback(input, shape, name, ctx): ...
def expand_dims(input, axis, name: Any | None = ...): ...

ExpandDims: Any

def expand_dims_eager_fallback(input, axis, name, ctx): ...
def extract_image_patches(images, ksizes, strides, rates, padding, name: Any | None = ...): ...

ExtractImagePatches: Any

def extract_image_patches_eager_fallback(images, ksizes, strides, rates, padding, name, ctx): ...
def extract_volume_patches(input, ksizes, strides, padding, name: Any | None = ...): ...

ExtractVolumePatches: Any

def extract_volume_patches_eager_fallback(input, ksizes, strides, padding, name, ctx): ...
def fake_quant_with_min_max_args(inputs, min: int = ..., max: int = ..., num_bits: int = ..., narrow_range: bool = ..., name: Any | None = ...): ...

FakeQuantWithMinMaxArgs: Any

def fake_quant_with_min_max_args_eager_fallback(inputs, min, max, num_bits, narrow_range, name, ctx): ...
def fake_quant_with_min_max_args_gradient(gradients, inputs, min: int = ..., max: int = ..., num_bits: int = ..., narrow_range: bool = ..., name: Any | None = ...): ...

FakeQuantWithMinMaxArgsGradient: Any

def fake_quant_with_min_max_args_gradient_eager_fallback(gradients, inputs, min, max, num_bits, narrow_range, name, ctx): ...
def fake_quant_with_min_max_vars(inputs, min, max, num_bits: int = ..., narrow_range: bool = ..., name: Any | None = ...): ...

FakeQuantWithMinMaxVars: Any

def fake_quant_with_min_max_vars_eager_fallback(inputs, min, max, num_bits, narrow_range, name, ctx): ...

class _FakeQuantWithMinMaxVarsGradientOutput(NamedTuple):
    backprops_wrt_input: Any
    backprop_wrt_min: Any
    backprop_wrt_max: Any

def fake_quant_with_min_max_vars_gradient(gradients, inputs, min, max, num_bits: int = ..., narrow_range: bool = ..., name: Any | None = ...): ...

FakeQuantWithMinMaxVarsGradient: Any

def fake_quant_with_min_max_vars_gradient_eager_fallback(gradients, inputs, min, max, num_bits, narrow_range, name, ctx): ...
def fake_quant_with_min_max_vars_per_channel(inputs, min, max, num_bits: int = ..., narrow_range: bool = ..., name: Any | None = ...): ...

FakeQuantWithMinMaxVarsPerChannel: Any

def fake_quant_with_min_max_vars_per_channel_eager_fallback(inputs, min, max, num_bits, narrow_range, name, ctx): ...

class _FakeQuantWithMinMaxVarsPerChannelGradientOutput(NamedTuple):
    backprops_wrt_input: Any
    backprop_wrt_min: Any
    backprop_wrt_max: Any

def fake_quant_with_min_max_vars_per_channel_gradient(gradients, inputs, min, max, num_bits: int = ..., narrow_range: bool = ..., name: Any | None = ...): ...

FakeQuantWithMinMaxVarsPerChannelGradient: Any

def fake_quant_with_min_max_vars_per_channel_gradient_eager_fallback(gradients, inputs, min, max, num_bits, narrow_range, name, ctx): ...
def fill(dims, value, name: Any | None = ...): ...

Fill: Any

def fill_eager_fallback(dims, value, name, ctx): ...
def fingerprint(data, method, name: Any | None = ...): ...

Fingerprint: Any

def fingerprint_eager_fallback(data, method, name, ctx): ...
def gather(params, indices, validate_indices: bool = ..., name: Any | None = ...): ...

Gather: Any

def gather_eager_fallback(params, indices, validate_indices, name, ctx): ...
def gather_nd(params, indices, name: Any | None = ...): ...

GatherNd: Any

def gather_nd_eager_fallback(params, indices, name, ctx): ...
def gather_v2(params, indices, axis, batch_dims: int = ..., name: Any | None = ...): ...

GatherV2: Any

def gather_v2_eager_fallback(params, indices, axis, batch_dims, name, ctx): ...
def guarantee_const(input, name: Any | None = ...): ...

GuaranteeConst: Any

def guarantee_const_eager_fallback(input, name, ctx): ...
def identity(input, name: Any | None = ...): ...

Identity: Any

def identity_eager_fallback(input, name, ctx): ...
def identity_n(input, name: Any | None = ...): ...

IdentityN: Any

def identity_n_eager_fallback(input, name, ctx): ...
def immutable_const(dtype, shape, memory_region_name, name: Any | None = ...): ...

ImmutableConst: Any

def immutable_const_eager_fallback(dtype, shape, memory_region_name, name, ctx): ...
def inplace_add(x, i, v, name: Any | None = ...): ...

InplaceAdd: Any

def inplace_add_eager_fallback(x, i, v, name, ctx): ...
def inplace_sub(x, i, v, name: Any | None = ...): ...

InplaceSub: Any

def inplace_sub_eager_fallback(x, i, v, name, ctx): ...
def inplace_update(x, i, v, name: Any | None = ...): ...

InplaceUpdate: Any

def inplace_update_eager_fallback(x, i, v, name, ctx): ...
def invert_permutation(x, name: Any | None = ...): ...

InvertPermutation: Any

def invert_permutation_eager_fallback(x, name, ctx): ...

class _ListDiffOutput(NamedTuple):
    out: Any
    idx: Any

def list_diff(x, y, out_idx=..., name: Any | None = ...): ...

ListDiff: Any

def list_diff_eager_fallback(x, y, out_idx, name, ctx): ...
def lower_bound(sorted_inputs, values, out_type=..., name: Any | None = ...): ...

LowerBound: Any

def lower_bound_eager_fallback(sorted_inputs, values, out_type, name, ctx): ...
def matrix_band_part(input, num_lower, num_upper, name: Any | None = ...): ...

MatrixBandPart: Any

def matrix_band_part_eager_fallback(input, num_lower, num_upper, name, ctx): ...
def matrix_diag(diagonal, name: Any | None = ...): ...

MatrixDiag: Any

def matrix_diag_eager_fallback(diagonal, name, ctx): ...
def matrix_diag_part(input, name: Any | None = ...): ...

MatrixDiagPart: Any

def matrix_diag_part_eager_fallback(input, name, ctx): ...
def matrix_diag_part_v2(input, k, padding_value, name: Any | None = ...): ...

MatrixDiagPartV2: Any

def matrix_diag_part_v2_eager_fallback(input, k, padding_value, name, ctx): ...
def matrix_diag_part_v3(input, k, padding_value, align: str = ..., name: Any | None = ...): ...

MatrixDiagPartV3: Any

def matrix_diag_part_v3_eager_fallback(input, k, padding_value, align, name, ctx): ...
def matrix_diag_v2(diagonal, k, num_rows, num_cols, padding_value, name: Any | None = ...): ...

MatrixDiagV2: Any

def matrix_diag_v2_eager_fallback(diagonal, k, num_rows, num_cols, padding_value, name, ctx): ...
def matrix_diag_v3(diagonal, k, num_rows, num_cols, padding_value, align: str = ..., name: Any | None = ...): ...

MatrixDiagV3: Any

def matrix_diag_v3_eager_fallback(diagonal, k, num_rows, num_cols, padding_value, align, name, ctx): ...
def matrix_set_diag(input, diagonal, name: Any | None = ...): ...

MatrixSetDiag: Any

def matrix_set_diag_eager_fallback(input, diagonal, name, ctx): ...
def matrix_set_diag_v2(input, diagonal, k, name: Any | None = ...): ...

MatrixSetDiagV2: Any

def matrix_set_diag_v2_eager_fallback(input, diagonal, k, name, ctx): ...
def matrix_set_diag_v3(input, diagonal, k, align: str = ..., name: Any | None = ...): ...

MatrixSetDiagV3: Any

def matrix_set_diag_v3_eager_fallback(input, diagonal, k, align, name, ctx): ...
def mirror_pad(input, paddings, mode, name: Any | None = ...): ...

MirrorPad: Any

def mirror_pad_eager_fallback(input, paddings, mode, name, ctx): ...
def mirror_pad_grad(input, paddings, mode, name: Any | None = ...): ...

MirrorPadGrad: Any

def mirror_pad_grad_eager_fallback(input, paddings, mode, name, ctx): ...
def one_hot(indices, depth, on_value, off_value, axis: int = ..., name: Any | None = ...): ...

OneHot: Any

def one_hot_eager_fallback(indices, depth, on_value, off_value, axis, name, ctx): ...
def ones_like(x, name: Any | None = ...): ...

OnesLike: Any

def ones_like_eager_fallback(x, name, ctx): ...
def pack(values, axis: int = ..., name: Any | None = ...): ...

Pack: Any

def pack_eager_fallback(values, axis, name, ctx): ...
def pad(input, paddings, name: Any | None = ...): ...

Pad: Any

def pad_eager_fallback(input, paddings, name, ctx): ...
def pad_v2(input, paddings, constant_values, name: Any | None = ...): ...

PadV2: Any

def pad_v2_eager_fallback(input, paddings, constant_values, name, ctx): ...
def parallel_concat(values, shape, name: Any | None = ...): ...

ParallelConcat: Any

def parallel_concat_eager_fallback(values, shape, name, ctx): ...
def placeholder(dtype, shape: Any | None = ..., name: Any | None = ...): ...

Placeholder: Any

def placeholder_eager_fallback(dtype, shape, name, ctx): ...
def placeholder_v2(dtype, shape, name: Any | None = ...): ...

PlaceholderV2: Any

def placeholder_v2_eager_fallback(dtype, shape, name, ctx): ...
def placeholder_with_default(input, shape, name: Any | None = ...): ...

PlaceholderWithDefault: Any

def placeholder_with_default_eager_fallback(input, shape, name, ctx): ...
def prevent_gradient(input, message: str = ..., name: Any | None = ...): ...

PreventGradient: Any

def prevent_gradient_eager_fallback(input, message, name, ctx): ...
def quantize_and_dequantize(input, signed_input: bool = ..., num_bits: int = ..., range_given: bool = ..., input_min: int = ..., input_max: int = ..., name: Any | None = ...): ...

QuantizeAndDequantize: Any

def quantize_and_dequantize_eager_fallback(input, signed_input, num_bits, range_given, input_min, input_max, name, ctx): ...
def quantize_and_dequantize_v2(input, input_min, input_max, signed_input: bool = ..., num_bits: int = ..., range_given: bool = ..., round_mode: str = ..., narrow_range: bool = ..., axis: int = ..., name: Any | None = ...): ...

QuantizeAndDequantizeV2: Any

def quantize_and_dequantize_v2_eager_fallback(input, input_min, input_max, signed_input, num_bits, range_given, round_mode, narrow_range, axis, name, ctx): ...
def quantize_and_dequantize_v3(input, input_min, input_max, num_bits, signed_input: bool = ..., range_given: bool = ..., narrow_range: bool = ..., axis: int = ..., name: Any | None = ...): ...

QuantizeAndDequantizeV3: Any

def quantize_and_dequantize_v3_eager_fallback(input, input_min, input_max, num_bits, signed_input, range_given, narrow_range, axis, name, ctx): ...
def quantize_and_dequantize_v4(input, input_min, input_max, signed_input: bool = ..., num_bits: int = ..., range_given: bool = ..., round_mode: str = ..., narrow_range: bool = ..., axis: int = ..., name: Any | None = ...): ...

QuantizeAndDequantizeV4: Any

def quantize_and_dequantize_v4_eager_fallback(input, input_min, input_max, signed_input, num_bits, range_given, round_mode, narrow_range, axis, name, ctx): ...

class _QuantizeAndDequantizeV4GradOutput(NamedTuple):
    input_backprop: Any
    input_min_backprop: Any
    input_max_backprop: Any

def quantize_and_dequantize_v4_grad(gradients, input, input_min, input_max, axis: int = ..., name: Any | None = ...): ...

QuantizeAndDequantizeV4Grad: Any

def quantize_and_dequantize_v4_grad_eager_fallback(gradients, input, input_min, input_max, axis, name, ctx): ...

class _QuantizeV2Output(NamedTuple):
    output: Any
    output_min: Any
    output_max: Any

def quantize_v2(input, min_range, max_range, T, mode: str = ..., round_mode: str = ..., narrow_range: bool = ..., axis: int = ..., ensure_minimum_range: float = ..., name: Any | None = ...): ...

QuantizeV2: Any

def quantize_v2_eager_fallback(input, min_range, max_range, T, mode, round_mode, narrow_range, axis, ensure_minimum_range, name, ctx): ...

class _QuantizedConcatOutput(NamedTuple):
    output: Any
    output_min: Any
    output_max: Any

def quantized_concat(concat_dim, values, input_mins, input_maxes, name: Any | None = ...): ...

QuantizedConcat: Any

def quantized_concat_eager_fallback(concat_dim, values, input_mins, input_maxes, name, ctx): ...

class _QuantizedInstanceNormOutput(NamedTuple):
    y: Any
    y_min: Any
    y_max: Any

def quantized_instance_norm(x, x_min, x_max, output_range_given: bool = ..., given_y_min: int = ..., given_y_max: int = ..., variance_epsilon: float = ..., min_separation: float = ..., name: Any | None = ...): ...

QuantizedInstanceNorm: Any

def quantized_instance_norm_eager_fallback(x, x_min, x_max, output_range_given, given_y_min, given_y_max, variance_epsilon, min_separation, name, ctx): ...

class _QuantizedReshapeOutput(NamedTuple):
    output: Any
    output_min: Any
    output_max: Any

def quantized_reshape(tensor, shape, input_min, input_max, name: Any | None = ...): ...

QuantizedReshape: Any

def quantized_reshape_eager_fallback(tensor, shape, input_min, input_max, name, ctx): ...
def rank(input, name: Any | None = ...): ...

Rank: Any

def rank_eager_fallback(input, name, ctx): ...
def ref_identity(input, name: Any | None = ...): ...

RefIdentity: Any

def ref_identity_eager_fallback(input, name, ctx) -> None: ...
def reshape(tensor, shape, name: Any | None = ...): ...

Reshape: Any

def reshape_eager_fallback(tensor, shape, name, ctx): ...
def resource_strided_slice_assign(ref, begin, end, strides, value, begin_mask: int = ..., end_mask: int = ..., ellipsis_mask: int = ..., new_axis_mask: int = ..., shrink_axis_mask: int = ..., name: Any | None = ...): ...

ResourceStridedSliceAssign: Any

def resource_strided_slice_assign_eager_fallback(ref, begin, end, strides, value, begin_mask, end_mask, ellipsis_mask, new_axis_mask, shrink_axis_mask, name, ctx): ...
def reverse(tensor, dims, name: Any | None = ...): ...

Reverse: Any

def reverse_eager_fallback(tensor, dims, name, ctx): ...
def reverse_sequence(input, seq_lengths, seq_dim, batch_dim: int = ..., name: Any | None = ...): ...

ReverseSequence: Any

def reverse_sequence_eager_fallback(input, seq_lengths, seq_dim, batch_dim, name, ctx): ...
def reverse_v2(tensor, axis, name: Any | None = ...): ...

ReverseV2: Any

def reverse_v2_eager_fallback(tensor, axis, name, ctx): ...
def scatter_nd(indices, updates, shape, name: Any | None = ...): ...

ScatterNd: Any

def scatter_nd_eager_fallback(indices, updates, shape, name, ctx): ...
def scatter_nd_non_aliasing_add(input, indices, updates, name: Any | None = ...): ...

ScatterNdNonAliasingAdd: Any

def scatter_nd_non_aliasing_add_eager_fallback(input, indices, updates, name, ctx): ...
def shape(input, out_type=..., name: Any | None = ...): ...

Shape: Any

def shape_eager_fallback(input, out_type, name, ctx): ...
def shape_n(input, out_type=..., name: Any | None = ...): ...

ShapeN: Any

def shape_n_eager_fallback(input, out_type, name, ctx): ...
def size(input, out_type=..., name: Any | None = ...): ...

Size: Any

def size_eager_fallback(input, out_type, name, ctx): ...

Slice: Any

def snapshot(input, name: Any | None = ...): ...

Snapshot: Any

def snapshot_eager_fallback(input, name, ctx): ...
def space_to_batch(input, paddings, block_size, name: Any | None = ...): ...

SpaceToBatch: Any

def space_to_batch_eager_fallback(input, paddings, block_size, name, ctx): ...
def space_to_batch_nd(input, block_shape, paddings, name: Any | None = ...): ...

SpaceToBatchND: Any

def space_to_batch_nd_eager_fallback(input, block_shape, paddings, name, ctx): ...
def space_to_depth(input, block_size, data_format: str = ..., name: Any | None = ...): ...

SpaceToDepth: Any

def space_to_depth_eager_fallback(input, block_size, data_format, name, ctx): ...
def split(axis, value, num_split, name: Any | None = ...): ...

Split: Any

def split_eager_fallback(axis, value, num_split, name, ctx): ...
def split_v(value, size_splits, axis, num_split, name: Any | None = ...): ...

SplitV: Any

def split_v_eager_fallback(value, size_splits, axis, num_split, name, ctx): ...
def squeeze(input, axis=..., name: Any | None = ...): ...

Squeeze: Any

def squeeze_eager_fallback(input, axis, name, ctx): ...
def stop_gradient(input, name: Any | None = ...): ...

StopGradient: Any

def stop_gradient_eager_fallback(input, name, ctx): ...
def strided_slice(input, begin, end, strides, begin_mask: int = ..., end_mask: int = ..., ellipsis_mask: int = ..., new_axis_mask: int = ..., shrink_axis_mask: int = ..., name: Any | None = ...): ...

StridedSlice: Any

def strided_slice_eager_fallback(input, begin, end, strides, begin_mask, end_mask, ellipsis_mask, new_axis_mask, shrink_axis_mask, name, ctx): ...
def strided_slice_assign(ref, begin, end, strides, value, begin_mask: int = ..., end_mask: int = ..., ellipsis_mask: int = ..., new_axis_mask: int = ..., shrink_axis_mask: int = ..., name: Any | None = ...): ...

StridedSliceAssign: Any

def strided_slice_assign_eager_fallback(ref, begin, end, strides, value, begin_mask, end_mask, ellipsis_mask, new_axis_mask, shrink_axis_mask, name, ctx) -> None: ...
def strided_slice_grad(shape, begin, end, strides, dy, begin_mask: int = ..., end_mask: int = ..., ellipsis_mask: int = ..., new_axis_mask: int = ..., shrink_axis_mask: int = ..., name: Any | None = ...): ...

StridedSliceGrad: Any

def strided_slice_grad_eager_fallback(shape, begin, end, strides, dy, begin_mask, end_mask, ellipsis_mask, new_axis_mask, shrink_axis_mask, name, ctx): ...
def tensor_scatter_add(tensor, indices, updates, name: Any | None = ...): ...

TensorScatterAdd: Any

def tensor_scatter_add_eager_fallback(tensor, indices, updates, name, ctx): ...
def tensor_scatter_max(tensor, indices, updates, name: Any | None = ...): ...

TensorScatterMax: Any

def tensor_scatter_max_eager_fallback(tensor, indices, updates, name, ctx): ...
def tensor_scatter_min(tensor, indices, updates, name: Any | None = ...): ...

TensorScatterMin: Any

def tensor_scatter_min_eager_fallback(tensor, indices, updates, name, ctx): ...
def tensor_scatter_sub(tensor, indices, updates, name: Any | None = ...): ...

TensorScatterSub: Any

def tensor_scatter_sub_eager_fallback(tensor, indices, updates, name, ctx): ...
def tensor_scatter_update(tensor, indices, updates, name: Any | None = ...): ...

TensorScatterUpdate: Any

def tensor_scatter_update_eager_fallback(tensor, indices, updates, name, ctx): ...
def tensor_strided_slice_update(input, begin, end, strides, value, begin_mask: int = ..., end_mask: int = ..., ellipsis_mask: int = ..., new_axis_mask: int = ..., shrink_axis_mask: int = ..., name: Any | None = ...): ...

TensorStridedSliceUpdate: Any

def tensor_strided_slice_update_eager_fallback(input, begin, end, strides, value, begin_mask, end_mask, ellipsis_mask, new_axis_mask, shrink_axis_mask, name, ctx): ...
def tile(input, multiples, name: Any | None = ...): ...

Tile: Any

def tile_eager_fallback(input, multiples, name, ctx): ...
def tile_grad(input, multiples, name: Any | None = ...): ...

TileGrad: Any

def tile_grad_eager_fallback(input, multiples, name, ctx): ...
def transpose(x, perm, name: Any | None = ...): ...

Transpose: Any

def transpose_eager_fallback(x, perm, name, ctx): ...

class _UniqueOutput(NamedTuple):
    y: Any
    idx: Any

def unique(x, out_idx=..., name: Any | None = ...): ...

Unique: Any

def unique_eager_fallback(x, out_idx, name, ctx): ...

class _UniqueV2Output(NamedTuple):
    y: Any
    idx: Any

def unique_v2(x, axis, out_idx=..., name: Any | None = ...): ...

UniqueV2: Any

def unique_v2_eager_fallback(x, axis, out_idx, name, ctx): ...

class _UniqueWithCountsOutput(NamedTuple):
    y: Any
    idx: Any
    count: Any

def unique_with_counts(x, out_idx=..., name: Any | None = ...): ...

UniqueWithCounts: Any

def unique_with_counts_eager_fallback(x, out_idx, name, ctx): ...

class _UniqueWithCountsV2Output(NamedTuple):
    y: Any
    idx: Any
    count: Any

def unique_with_counts_v2(x, axis, out_idx=..., name: Any | None = ...): ...

UniqueWithCountsV2: Any

def unique_with_counts_v2_eager_fallback(x, axis, out_idx, name, ctx): ...
def unpack(value, num, axis: int = ..., name: Any | None = ...): ...

Unpack: Any

def unpack_eager_fallback(value, num, axis, name, ctx): ...
def unravel_index(indices, dims, name: Any | None = ...): ...

UnravelIndex: Any

def unravel_index_eager_fallback(indices, dims, name, ctx): ...
def upper_bound(sorted_inputs, values, out_type=..., name: Any | None = ...): ...

UpperBound: Any

def upper_bound_eager_fallback(sorted_inputs, values, out_type, name, ctx): ...
def where(condition, name: Any | None = ...): ...

Where: Any

def where_eager_fallback(condition, name, ctx): ...
def zeros_like(x, name: Any | None = ...): ...

ZerosLike: Any

def zeros_like_eager_fallback(x, name, ctx): ...
