from tensorflow.python.eager import def_function as def_function
from tensorflow.python.framework import constant_op as constant_op, dtypes as dtypes, ops as ops, random_seed as random_seed, tensor_shape as tensor_shape, tensor_util as tensor_util
from tensorflow.python.ops import array_ops as array_ops, check_ops as check_ops, control_flow_ops as control_flow_ops, gen_image_ops as gen_image_ops, math_ops as math_ops, nn as nn, nn_ops as nn_ops, random_ops as random_ops, sort_ops as sort_ops, stateless_random_ops as stateless_random_ops, string_ops as string_ops, variables as variables
from tensorflow.python.util import deprecation as deprecation, dispatch as dispatch
from tensorflow.python.util.tf_export import tf_export as tf_export
from typing import Any

def fix_image_flip_shape(image, result): ...
def random_flip_up_down(image, seed: Any | None = ...): ...
def random_flip_left_right(image, seed: Any | None = ...): ...
def stateless_random_flip_left_right(image, seed): ...
def stateless_random_flip_up_down(image, seed): ...
def flip_left_right(image): ...
def flip_up_down(image): ...
def rot90(image, k: int = ..., name: Any | None = ...): ...
def transpose(image, name: Any | None = ...): ...
def central_crop(image, central_fraction): ...
def pad_to_bounding_box(image, offset_height, offset_width, target_height, target_width): ...
def crop_to_bounding_box(image, offset_height, offset_width, target_height, target_width): ...
def resize_image_with_crop_or_pad(image, target_height, target_width): ...

class ResizeMethodV1:
    BILINEAR: int
    NEAREST_NEIGHBOR: int
    BICUBIC: int
    AREA: int

class ResizeMethod:
    BILINEAR: str
    NEAREST_NEIGHBOR: str
    BICUBIC: str
    AREA: str
    LANCZOS3: str
    LANCZOS5: str
    GAUSSIAN: str
    MITCHELLCUBIC: str

def resize_images(images, size, method=..., align_corners: bool = ..., preserve_aspect_ratio: bool = ..., name: Any | None = ...): ...
def resize_images_v2(images, size, method=..., preserve_aspect_ratio: bool = ..., antialias: bool = ..., name: Any | None = ...): ...
def resize_image_with_pad_v1(image, target_height, target_width, method=..., align_corners: bool = ...): ...
def resize_image_with_pad_v2(image, target_height, target_width, method=..., antialias: bool = ...): ...
def per_image_standardization(image): ...
def random_brightness(image, max_delta, seed: Any | None = ...): ...
def stateless_random_brightness(image, max_delta, seed): ...
def random_contrast(image, lower, upper, seed: Any | None = ...): ...
def stateless_random_contrast(image, lower, upper, seed): ...
def adjust_brightness(image, delta): ...
def adjust_contrast(images, contrast_factor): ...
def adjust_gamma(image, gamma: int = ..., gain: int = ...): ...
def convert_image_dtype(image, dtype, saturate: bool = ..., name: Any | None = ...): ...
def rgb_to_grayscale(images, name: Any | None = ...): ...
def grayscale_to_rgb(images, name: Any | None = ...): ...
def random_hue(image, max_delta, seed: Any | None = ...): ...
def stateless_random_hue(image, max_delta, seed): ...
def adjust_hue(image, delta, name: Any | None = ...): ...
def random_jpeg_quality(image, min_jpeg_quality, max_jpeg_quality, seed: Any | None = ...): ...
def stateless_random_jpeg_quality(image, min_jpeg_quality, max_jpeg_quality, seed): ...
def adjust_jpeg_quality(image, jpeg_quality, name: Any | None = ...): ...
def random_saturation(image, lower, upper, seed: Any | None = ...): ...
def stateless_random_saturation(image, lower, upper, seed: Any | None = ...): ...
def adjust_saturation(image, saturation_factor, name: Any | None = ...): ...
def is_jpeg(contents, name: Any | None = ...): ...
def encode_png(image, compression: int = ..., name: Any | None = ...): ...
def decode_image(contents, channels: Any | None = ..., dtype=..., name: Any | None = ..., expand_animations: bool = ...): ...
def total_variation(images, name: Any | None = ...): ...
def sample_distorted_bounding_box_v2(image_size, bounding_boxes, seed: int = ..., min_object_covered: float = ..., aspect_ratio_range: Any | None = ..., area_range: Any | None = ..., max_attempts: Any | None = ..., use_image_if_no_bounding_boxes: Any | None = ..., name: Any | None = ...): ...
def stateless_sample_distorted_bounding_box(image_size, bounding_boxes, seed, min_object_covered: float = ..., aspect_ratio_range: Any | None = ..., area_range: Any | None = ..., max_attempts: Any | None = ..., use_image_if_no_bounding_boxes: Any | None = ..., name: Any | None = ...): ...
def sample_distorted_bounding_box(image_size, bounding_boxes, seed: Any | None = ..., seed2: Any | None = ..., min_object_covered: float = ..., aspect_ratio_range: Any | None = ..., area_range: Any | None = ..., max_attempts: Any | None = ..., use_image_if_no_bounding_boxes: Any | None = ..., name: Any | None = ...): ...
def non_max_suppression(boxes, scores, max_output_size, iou_threshold: float = ..., score_threshold=..., name: Any | None = ...): ...
def non_max_suppression_with_scores(boxes, scores, max_output_size, iou_threshold: float = ..., score_threshold=..., soft_nms_sigma: float = ..., name: Any | None = ...): ...
def non_max_suppression_with_overlaps(overlaps, scores, max_output_size, overlap_threshold: float = ..., score_threshold=..., name: Any | None = ...): ...
def rgb_to_yiq(images): ...
def yiq_to_rgb(images): ...
def rgb_to_yuv(images): ...
def yuv_to_rgb(images): ...
def psnr(a, b, max_val, name: Any | None = ...): ...
def ssim(img1, img2, max_val, filter_size: int = ..., filter_sigma: float = ..., k1: float = ..., k2: float = ...): ...
def ssim_multiscale(img1, img2, max_val, power_factors=..., filter_size: int = ..., filter_sigma: float = ..., k1: float = ..., k2: float = ...): ...
def image_gradients(image): ...
def sobel_edges(image): ...
def resize_bicubic(images, size, align_corners: bool = ..., name: Any | None = ..., half_pixel_centers: bool = ...): ...
def resize_bilinear(images, size, align_corners: bool = ..., name: Any | None = ..., half_pixel_centers: bool = ...): ...
def resize_nearest_neighbor(images, size, align_corners: bool = ..., name: Any | None = ..., half_pixel_centers: bool = ...): ...

resize_area_deprecation: Any
resize_bicubic_deprecation: Any
resize_bilinear_deprecation: Any
resize_nearest_neighbor_deprecation: Any

def crop_and_resize_v2(image, boxes, box_indices, crop_size, method: str = ..., extrapolation_value: float = ..., name: Any | None = ...): ...
def crop_and_resize_v1(image, boxes, box_ind: Any | None = ..., crop_size: Any | None = ..., method: str = ..., extrapolation_value: int = ..., name: Any | None = ..., box_indices: Any | None = ...): ...
def extract_glimpse(input, size, offsets, centered: bool = ..., normalized: bool = ..., uniform_noise: bool = ..., name: Any | None = ...): ...
def extract_glimpse_v2(input, size, offsets, centered: bool = ..., normalized: bool = ..., noise: str = ..., name: Any | None = ...): ...
def combined_non_max_suppression(boxes, scores, max_output_size_per_class, max_total_size, iou_threshold: float = ..., score_threshold=..., pad_per_class: bool = ..., clip_boxes: bool = ..., name: Any | None = ...): ...
def non_max_suppression_padded(boxes, scores, max_output_size, iou_threshold: float = ..., score_threshold=..., pad_to_max_output_size: bool = ..., name: Any | None = ..., sorted_input: bool = ..., canonicalized_coordinates: bool = ..., tile_size: int = ...): ...
def non_max_suppression_padded_v2(boxes, scores, max_output_size, iou_threshold: float = ..., score_threshold=..., sorted_input: bool = ..., canonicalized_coordinates: bool = ..., tile_size: int = ...): ...
def non_max_suppression_padded_v1(boxes, scores, max_output_size, iou_threshold: float = ..., score_threshold=..., pad_to_max_output_size: bool = ..., name: Any | None = ...): ...
def draw_bounding_boxes_v2(images, boxes, colors, name: Any | None = ...): ...
def draw_bounding_boxes(images, boxes, name: Any | None = ..., colors: Any | None = ...): ...
def generate_bounding_box_proposals(scores, bbox_deltas, image_info, anchors, nms_threshold: float = ..., pre_nms_topn: int = ..., min_size: int = ..., post_nms_topn: int = ..., name: Any | None = ...): ...