from .. import rcmod as rcmod
from .._core import categorical_order as categorical_order
from .._testing import assert_colors_equal as assert_colors_equal, assert_plots_equal as assert_plots_equal
from ..categorical import pointplot as pointplot
from ..distributions import distplot as distplot, histplot as histplot, kdeplot as kdeplot
from ..palettes import color_palette as color_palette
from ..relational import scatterplot as scatterplot
from typing import Any

rs: Any

class TestFacetGrid:
    df: Any
    def test_self_data(self) -> None: ...
    def test_self_figure(self) -> None: ...
    def test_self_axes(self) -> None: ...
    def test_axes_array_size(self) -> None: ...
    def test_single_axes(self) -> None: ...
    def test_col_wrap(self) -> None: ...
    def test_normal_axes(self) -> None: ...
    def test_wrapped_axes(self) -> None: ...
    def test_axes_dict(self) -> None: ...
    def test_figure_size(self) -> None: ...
    def test_figure_size_with_legend(self) -> None: ...
    def test_legend_data(self) -> None: ...
    def test_legend_data_missing_level(self) -> None: ...
    def test_get_boolean_legend_data(self) -> None: ...
    def test_legend_tuples(self) -> None: ...
    def test_legend_options(self) -> None: ...
    def test_legendout_with_colwrap(self) -> None: ...
    def test_legend_tight_layout(self) -> None: ...
    def test_subplot_kws(self) -> None: ...
    def test_gridspec_kws(self) -> None: ...
    def test_gridspec_kws_col_wrap(self) -> None: ...
    def test_data_generator(self) -> None: ...
    def test_map(self) -> None: ...
    def test_map_dataframe(self) -> None: ...
    def test_set(self) -> None: ...
    def test_set_titles(self) -> None: ...
    def test_set_titles_margin_titles(self) -> None: ...
    def test_set_ticklabels(self) -> None: ...
    def test_set_axis_labels(self) -> None: ...
    def test_axis_lims(self) -> None: ...
    def test_data_orders(self) -> None: ...
    def test_palette(self) -> None: ...
    def test_hue_kws(self) -> None: ...
    def test_dropna(self) -> None: ...
    def test_categorical_column_missing_categories(self) -> None: ...
    def test_categorical_warning(self) -> None: ...
    def test_refline(self) -> None: ...

class TestPairGrid:
    rs: Any
    df: Any
    def test_self_data(self) -> None: ...
    def test_ignore_datelike_data(self) -> None: ...
    def test_self_figure(self) -> None: ...
    def test_self_axes(self) -> None: ...
    def test_default_axes(self) -> None: ...
    def test_specific_square_axes(self, vars) -> None: ...
    def test_remove_hue_from_default(self) -> None: ...
    def test_specific_nonsquare_axes(self, x_vars, y_vars) -> None: ...
    def test_corner(self) -> None: ...
    def test_size(self) -> None: ...
    def test_empty_grid(self) -> None: ...
    def test_map(self) -> None: ...
    def test_map_nonsquare(self) -> None: ...
    def test_map_lower(self) -> None: ...
    def test_map_upper(self) -> None: ...
    def test_map_mixed_funcsig(self) -> None: ...
    def test_map_diag(self) -> None: ...
    def test_map_diag_rectangular(self) -> None: ...
    def test_map_diag_color(self) -> None: ...
    def test_map_diag_palette(self) -> None: ...
    def test_map_diag_and_offdiag(self) -> None: ...
    def test_diag_sharey(self) -> None: ...
    def test_map_diag_matplotlib(self) -> None: ...
    def test_palette(self) -> None: ...
    def test_hue_kws(self) -> None: ...
    def test_hue_order(self) -> None: ...
    def test_hue_order_missing_level(self) -> None: ...
    def test_nondefault_index(self) -> None: ...
    def test_dropna(self, func) -> None: ...
    def test_histplot_legend(self) -> None: ...
    def test_pairplot(self) -> None: ...
    def test_pairplot_reg(self) -> None: ...
    def test_pairplot_reg_hue(self) -> None: ...
    def test_pairplot_diag_kde(self) -> None: ...
    def test_pairplot_kde(self) -> None: ...
    def test_pairplot_hist(self) -> None: ...
    def test_pairplot_markers(self) -> None: ...
    def test_corner_despine(self) -> None: ...
    def test_corner_set(self) -> None: ...
    def test_legend(self) -> None: ...

class TestJointGrid:
    rs: Any
    x: Any
    y: Any
    x_na: Any
    data: Any
    def test_margin_grid_from_lists(self) -> None: ...
    def test_margin_grid_from_arrays(self) -> None: ...
    def test_margin_grid_from_series(self) -> None: ...
    def test_margin_grid_from_dataframe(self) -> None: ...
    def test_margin_grid_from_dataframe_bad_variable(self) -> None: ...
    def test_margin_grid_axis_labels(self) -> None: ...
    def test_dropna(self) -> None: ...
    def test_axlims(self) -> None: ...
    def test_marginal_ticks(self) -> None: ...
    def test_bivariate_plot(self) -> None: ...
    def test_univariate_plot(self) -> None: ...
    def test_univariate_plot_distplot(self) -> None: ...
    def test_univariate_plot_matplotlib(self) -> None: ...
    def test_plot(self) -> None: ...
    def test_space(self) -> None: ...
    def test_hue(self, long_df, as_vector) -> None: ...
    def test_refline(self) -> None: ...

class TestJointPlot:
    rs: Any
    x: Any
    y: Any
    data: Any
    def test_scatter(self) -> None: ...
    def test_scatter_hue(self, long_df) -> None: ...
    def test_reg(self) -> None: ...
    def test_resid(self) -> None: ...
    def test_hist(self, long_df) -> None: ...
    def test_hex(self) -> None: ...
    def test_kde(self, long_df) -> None: ...
    def test_kde_hue(self, long_df) -> None: ...
    def test_color(self) -> None: ...
    def test_palette(self, long_df) -> None: ...
    def test_hex_customise(self) -> None: ...
    def test_bad_kind(self) -> None: ...
    def test_unsupported_hue_kind(self) -> None: ...
    def test_leaky_dict(self) -> None: ...
    def test_distplot_kwarg_warning(self, long_df) -> None: ...