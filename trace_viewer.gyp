# Copyright (c) 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'tracing_css_files': [
      'trace_viewer/base/ui/common.css',
      'trace_viewer/base/ui/drag_handle.css',
      'trace_viewer/base/ui/info_bar.css',
      'trace_viewer/base/ui/line_chart.css',
      'trace_viewer/base/ui/list_view.css',
      'trace_viewer/base/ui/mouse_mode_selector.css',
      'trace_viewer/base/ui/pie_chart.css',
      'trace_viewer/base/ui/sortable_table.css',
      'trace_viewer/base/ui/sunburst_chart.css',
      'trace_viewer/base/ui/tool_button.css',
      'trace_viewer/core/analysis/analysis_results.css',
      'trace_viewer/core/side_panel/side_panel_container.css',
      'trace_viewer/core/timeline_track_view.css',
      'trace_viewer/core/timeline_view.css',
      'trace_viewer/core/tracks/counter_track.css',
      'trace_viewer/core/tracks/drawing_container.css',
      'trace_viewer/core/tracks/heading_track.css',
      'trace_viewer/core/tracks/object_instance_track.css',
      'trace_viewer/core/tracks/process_track_base.css',
      'trace_viewer/core/tracks/rect_track.css',
      'trace_viewer/core/tracks/ruler_track.css',
      'trace_viewer/core/tracks/spacing_track.css',
      'trace_viewer/core/tracks/thread_track.css',
      'trace_viewer/core/tracks/track.css',
      'trace_viewer/extras/about_tracing/common.css',
      'trace_viewer/extras/cc/display_item_view.css',
      'trace_viewer/extras/cc/layer_picker.css',
      'trace_viewer/extras/cc/layer_tree_host_impl_view.css',
      'trace_viewer/extras/cc/layer_view.css',
      'trace_viewer/extras/cc/picture_ops_chart_summary_view.css',
      'trace_viewer/extras/cc/picture_ops_chart_view.css',
      'trace_viewer/extras/cc/picture_ops_list_view.css',
      'trace_viewer/extras/cc/picture_view.css',
      'trace_viewer/extras/gpu/state_view.css',
      'trace_viewer/extras/system_stats/system_stats_instance_track.css',
      'trace_viewer/extras/system_stats/system_stats_snapshot_view.css',
      'trace_viewer/extras/tcmalloc/heap_instance_track.css',
      'trace_viewer/extras/tcmalloc/tcmalloc_instance_view.css',
      'trace_viewer/extras/tcmalloc/tcmalloc_snapshot_view.css',
    ],
    'tracing_js_html_files': [
      'trace_viewer/base/base.html',
      'trace_viewer/base/base64.html',
      'trace_viewer/base/bbox2.html',
      'trace_viewer/base/category_util.html',
      'trace_viewer/base/color.html',
      'trace_viewer/base/event_target.html',
      'trace_viewer/base/events.html',
      'trace_viewer/base/extension_registry.html',
      'trace_viewer/base/extension_registry_base.html',
      'trace_viewer/base/extension_registry_basic.html',
      'trace_viewer/base/extension_registry_type_based.html',
      'trace_viewer/base/gl_matrix.html',
      'trace_viewer/base/guid.html',
      'trace_viewer/base/interval_tree.html',
      'trace_viewer/base/iteration_helpers.html',
      'trace_viewer/base/key_event_manager.html',
      'trace_viewer/base/polymer_utils.html',
      'trace_viewer/base/properties.html',
      'trace_viewer/base/quad.html',
      'trace_viewer/base/raf.html',
      'trace_viewer/base/range.html',
      'trace_viewer/base/rect.html',
      'trace_viewer/base/settings.html',
      'trace_viewer/base/sorted_array_utils.html',
      'trace_viewer/base/statistics.html',
      'trace_viewer/base/task.html',
      'trace_viewer/base/ui.html',
      'trace_viewer/base/ui/animation.html',
      'trace_viewer/base/ui/animation_controller.html',
      'trace_viewer/base/ui/camera.html',
      'trace_viewer/base/ui/chart_base.html',
      'trace_viewer/base/ui/color_scheme.html',
      'trace_viewer/base/ui/color_utils.html',
      'trace_viewer/base/ui/container_that_decorates_its_children.html',
      'trace_viewer/base/ui/d3.html',
      'trace_viewer/base/ui/dom_helpers.html',
      'trace_viewer/base/ui/drag_handle.html',
      'trace_viewer/base/ui/info_bar.html',
      'trace_viewer/base/ui/line_chart.html',
      'trace_viewer/base/ui/list_view.html',
      'trace_viewer/base/ui/mouse_mode_selector.html',
      'trace_viewer/base/ui/mouse_tracker.html',
      'trace_viewer/base/ui/overlay.html',
      'trace_viewer/base/ui/pie_chart.html',
      'trace_viewer/base/ui/quad_stack_view.html',
      'trace_viewer/base/ui/sortable_table.html',
      'trace_viewer/base/ui/sunburst_chart.html',
      'trace_viewer/base/utils.html',
      'trace_viewer/core/analysis/analysis_link.html',
      'trace_viewer/core/analysis/analysis_results.html',
      'trace_viewer/core/analysis/analysis_sub_view.html',
      'trace_viewer/core/analysis/analysis_view.html',
      'trace_viewer/core/analysis/counter_sample_sub_view.html',
      'trace_viewer/core/analysis/generic_object_view.html',
      'trace_viewer/core/analysis/multi_alert_sub_view.html',
      'trace_viewer/core/analysis/multi_flow_event_sub_view.html',
      'trace_viewer/core/analysis/multi_global_memory_dump_sub_view.html',
      'trace_viewer/core/analysis/multi_instant_event_sub_view.html',
      'trace_viewer/core/analysis/multi_interaction_record_sub_view.html',
      'trace_viewer/core/analysis/multi_object_sub_view.html',
      'trace_viewer/core/analysis/multi_sample_sub_view.html',
      'trace_viewer/core/analysis/multi_slice_sub_view.html',
      'trace_viewer/core/analysis/object_instance_view.html',
      'trace_viewer/core/analysis/object_snapshot_view.html',
      'trace_viewer/core/analysis/single_alert_sub_view.html',
      'trace_viewer/core/analysis/single_cpu_slice_sub_view.html',
      'trace_viewer/core/analysis/single_flow_event_sub_view.html',
      'trace_viewer/core/analysis/single_global_memory_dump_sub_view.html',
      'trace_viewer/core/analysis/single_instant_event_sub_view.html',
      'trace_viewer/core/analysis/single_interaction_record_sub_view.html',
      'trace_viewer/core/analysis/single_object_instance_sub_view.html',
      'trace_viewer/core/analysis/single_object_snapshot_sub_view.html',
      'trace_viewer/core/analysis/single_sample_sub_view.html',
      'trace_viewer/core/analysis/single_slice_sub_view.html',
      'trace_viewer/core/analysis/single_thread_time_slice_sub_view.html',
      'trace_viewer/core/analysis/stack_frame.html',
      'trace_viewer/core/analysis/tab_view.html',
      'trace_viewer/core/analysis/table_builder.html',
      'trace_viewer/core/analysis/time_element.html',
      'trace_viewer/core/analysis/time_span.html',
      'trace_viewer/core/analysis/time_stamp.html',
      'trace_viewer/core/analysis/toggle_container.html',
      'trace_viewer/core/analysis/util.html',
      'trace_viewer/core/auditor.html',
      'trace_viewer/core/constants.html',
      'trace_viewer/core/draw_helpers.html',
      'trace_viewer/core/elided_cache.html',
      'trace_viewer/core/event_presenter.html',
      'trace_viewer/core/fast_rect_renderer.html',
      'trace_viewer/core/filter.html',
      'trace_viewer/core/find_control.html',
      'trace_viewer/core/find_controller.html',
      'trace_viewer/core/importer/empty_importer.html',
      'trace_viewer/core/importer/importer.html',
      'trace_viewer/core/importer/simple_line_reader.html',
      'trace_viewer/core/location.html',
      'trace_viewer/core/scripting_control.html',
      'trace_viewer/core/selection.html',
      'trace_viewer/core/side_panel/side_panel.html',
      'trace_viewer/core/side_panel/side_panel_container.html',
      'trace_viewer/core/timeline_display_transform.html',
      'trace_viewer/core/timeline_display_transform_animations.html',
      'trace_viewer/core/timeline_interest_range.html',
      'trace_viewer/core/timeline_track_view.html',
      'trace_viewer/core/timeline_view.html',
      'trace_viewer/core/timeline_viewport.html',
      'trace_viewer/core/timing_tool.html',
      'trace_viewer/core/trace_model/alert.html',
      'trace_viewer/core/trace_model/annotation.html',
      'trace_viewer/core/trace_model/async_slice.html',
      'trace_viewer/core/trace_model/async_slice_group.html',
      'trace_viewer/core/trace_model/counter.html',
      'trace_viewer/core/trace_model/counter_sample.html',
      'trace_viewer/core/trace_model/counter_series.html',
      'trace_viewer/core/trace_model/cpu.html',
      'trace_viewer/core/trace_model/cpu_slice.html',
      'trace_viewer/core/trace_model/event.html',
      'trace_viewer/core/trace_model/event_container.html',
      'trace_viewer/core/trace_model/flow_event.html',
      'trace_viewer/core/trace_model/global_memory_dump.html',
      'trace_viewer/core/trace_model/instant_event.html',
      'trace_viewer/core/trace_model/interaction_record.html',
      'trace_viewer/core/trace_model/kernel.html',
      'trace_viewer/core/trace_model/object_collection.html',
      'trace_viewer/core/trace_model/object_instance.html',
      'trace_viewer/core/trace_model/object_snapshot.html',
      'trace_viewer/core/trace_model/process.html',
      'trace_viewer/core/trace_model/process_base.html',
      'trace_viewer/core/trace_model/process_memory_dump.html',
      'trace_viewer/core/trace_model/rect_annotation.html',
      'trace_viewer/core/trace_model/sample.html',
      'trace_viewer/core/trace_model/slice.html',
      'trace_viewer/core/trace_model/slice_group.html',
      'trace_viewer/core/trace_model/stack_frame.html',
      'trace_viewer/core/trace_model/thread.html',
      'trace_viewer/core/trace_model/thread_slice.html',
      'trace_viewer/core/trace_model/thread_time_slice.html',
      'trace_viewer/core/trace_model/time_to_object_instance_map.html',
      'trace_viewer/core/trace_model/timed_event.html',
      'trace_viewer/core/trace_model/trace_model.html',
      'trace_viewer/core/trace_model/trace_model_settings.html',
      'trace_viewer/core/trace_model/x_marker_annotation.html',
      'trace_viewer/core/tracks/alert_track.html',
      'trace_viewer/core/tracks/annotation_view.html',
      'trace_viewer/core/tracks/async_slice_group_track.html',
      'trace_viewer/core/tracks/container_track.html',
      'trace_viewer/core/tracks/counter_track.html',
      'trace_viewer/core/tracks/cpu_track.html',
      'trace_viewer/core/tracks/drawing_container.html',
      'trace_viewer/core/tracks/heading_track.html',
      'trace_viewer/core/tracks/highlighter.html',
      'trace_viewer/core/tracks/kernel_track.html',
      'trace_viewer/core/tracks/letter_dot_track.html',
      'trace_viewer/core/tracks/memory_dump_track.html',
      'trace_viewer/core/tracks/multi_row_track.html',
      'trace_viewer/core/tracks/object_instance_group_track.html',
      'trace_viewer/core/tracks/object_instance_track.html',
      'trace_viewer/core/tracks/process_track.html',
      'trace_viewer/core/tracks/process_track_base.html',
      'trace_viewer/core/tracks/rect_annotation_view.html',
      'trace_viewer/core/tracks/rect_track.html',
      'trace_viewer/core/tracks/ruler_track.html',
      'trace_viewer/core/tracks/sample_track.html',
      'trace_viewer/core/tracks/slice_group_track.html',
      'trace_viewer/core/tracks/slice_track.html',
      'trace_viewer/core/tracks/spacing_track.html',
      'trace_viewer/core/tracks/stacked_bars_track.html',
      'trace_viewer/core/tracks/thread_track.html',
      'trace_viewer/core/tracks/trace_model_track.html',
      'trace_viewer/core/tracks/track.html',
      'trace_viewer/core/tracks/x_marker_annotation_view.html',
      'trace_viewer/core/ui_state.html',
      'trace_viewer/extras/about_tracing/about_tracing.html',
      'trace_viewer/extras/about_tracing/inspector_connection.html',
      'trace_viewer/extras/about_tracing/inspector_tracing_controller_client.html',
      'trace_viewer/extras/about_tracing/profiling_view.html',
      'trace_viewer/extras/about_tracing/record_and_capture_controller.html',
      'trace_viewer/extras/about_tracing/record_selection_dialog.html',
      'trace_viewer/extras/about_tracing/tracing_controller_client.html',
      'trace_viewer/extras/about_tracing/xhr_based_tracing_controller_client.html',
      'trace_viewer/extras/analysis/sampling_summary.html',
      'trace_viewer/extras/audits/android_app.html',
      'trace_viewer/extras/audits/android_auditor.html',
      'trace_viewer/extras/audits/android_frame.html',
      'trace_viewer/extras/audits/android_model_helper.html',
      'trace_viewer/extras/audits/chrome_auditor.html',
      'trace_viewer/extras/audits/chrome_browser_helper.html',
      'trace_viewer/extras/audits/chrome_model_helper.html',
      'trace_viewer/extras/audits/chrome_process_helper.html',
      'trace_viewer/extras/audits/chrome_renderer_helper.html',
      'trace_viewer/extras/audits/utils.html',
      'trace_viewer/extras/cc/cc.html',
      'trace_viewer/extras/cc/constants.html',
      'trace_viewer/extras/cc/debug_colors.html',
      'trace_viewer/extras/cc/display_item_debugger.html',
      'trace_viewer/extras/cc/display_item_list.html',
      'trace_viewer/extras/cc/display_item_view.html',
      'trace_viewer/extras/cc/layer_impl.html',
      'trace_viewer/extras/cc/layer_picker.html',
      'trace_viewer/extras/cc/layer_tree_host_impl.html',
      'trace_viewer/extras/cc/layer_tree_host_impl_view.html',
      'trace_viewer/extras/cc/layer_tree_impl.html',
      'trace_viewer/extras/cc/layer_tree_quad_stack_view.html',
      'trace_viewer/extras/cc/layer_view.html',
      'trace_viewer/extras/cc/picture.html',
      'trace_viewer/extras/cc/picture_as_image_data.html',
      'trace_viewer/extras/cc/picture_debugger.html',
      'trace_viewer/extras/cc/picture_ops_chart_summary_view.html',
      'trace_viewer/extras/cc/picture_ops_chart_view.html',
      'trace_viewer/extras/cc/picture_ops_list_view.html',
      'trace_viewer/extras/cc/picture_view.html',
      'trace_viewer/extras/cc/raster_task.html',
      'trace_viewer/extras/cc/raster_task_selection.html',
      'trace_viewer/extras/cc/raster_task_view.html',
      'trace_viewer/extras/cc/region.html',
      'trace_viewer/extras/cc/render_pass.html',
      'trace_viewer/extras/cc/selection.html',
      'trace_viewer/extras/cc/tile.html',
      'trace_viewer/extras/cc/tile_coverage_rect.html',
      'trace_viewer/extras/cc/tile_view.html',
      'trace_viewer/extras/cc/util.html',
      'trace_viewer/extras/chrome_config.html',
      'trace_viewer/extras/full_config.html',
      'trace_viewer/extras/gpu/gpu.html',
      'trace_viewer/extras/gpu/state.html',
      'trace_viewer/extras/gpu/state_view.html',
      'trace_viewer/extras/highlighter/vsync_highlighter.html',
      'trace_viewer/extras/importer/ddms_importer.html',
      'trace_viewer/extras/importer/etw/etw_importer.html',
      'trace_viewer/extras/importer/etw/eventtrace_parser.html',
      'trace_viewer/extras/importer/etw/parser.html',
      'trace_viewer/extras/importer/etw/process_parser.html',
      'trace_viewer/extras/importer/etw/thread_parser.html',
      'trace_viewer/extras/importer/gzip_importer.html',
      'trace_viewer/extras/importer/jszip.html',
      'trace_viewer/extras/importer/linux_perf/android_parser.html',
      'trace_viewer/extras/importer/linux_perf/bus_parser.html',
      'trace_viewer/extras/importer/linux_perf/clock_parser.html',
      'trace_viewer/extras/importer/linux_perf/cpufreq_parser.html',
      'trace_viewer/extras/importer/linux_perf/disk_parser.html',
      'trace_viewer/extras/importer/linux_perf/drm_parser.html',
      'trace_viewer/extras/importer/linux_perf/exynos_parser.html',
      'trace_viewer/extras/importer/linux_perf/gesture_parser.html',
      'trace_viewer/extras/importer/linux_perf/i915_parser.html',
      'trace_viewer/extras/importer/linux_perf/irq_parser.html',
      'trace_viewer/extras/importer/linux_perf/kfunc_parser.html',
      'trace_viewer/extras/importer/linux_perf/linux_perf_importer.html',
      'trace_viewer/extras/importer/linux_perf/mali_parser.html',
      'trace_viewer/extras/importer/linux_perf/memreclaim_parser.html',
      'trace_viewer/extras/importer/linux_perf/parser.html',
      'trace_viewer/extras/importer/linux_perf/power_parser.html',
      'trace_viewer/extras/importer/linux_perf/regulator_parser.html',
      'trace_viewer/extras/importer/linux_perf/sched_parser.html',
      'trace_viewer/extras/importer/linux_perf/sync_parser.html',
      'trace_viewer/extras/importer/linux_perf/workqueue_parser.html',
      'trace_viewer/extras/importer/trace2html_importer.html',
      'trace_viewer/extras/importer/trace_event_importer.html',
      'trace_viewer/extras/importer/v8/codemap.html',
      'trace_viewer/extras/importer/v8/log_reader.html',
      'trace_viewer/extras/importer/v8/splaytree.html',
      'trace_viewer/extras/importer/v8/v8_log_importer.html',
      'trace_viewer/extras/importer/zip_importer.html',
      'trace_viewer/extras/lean_config.html',
      'trace_viewer/extras/net/net.html',
      'trace_viewer/extras/net/net_async_slice.html',
      'trace_viewer/extras/side_panel/alerts_side_panel.html',
      'trace_viewer/extras/side_panel/input_latency.html',
      'trace_viewer/extras/side_panel/time_summary.html',
      'trace_viewer/extras/system_stats/system_stats.html',
      'trace_viewer/extras/system_stats/system_stats_instance_track.html',
      'trace_viewer/extras/system_stats/system_stats_snapshot.html',
      'trace_viewer/extras/system_stats/system_stats_snapshot_view.html',
      'trace_viewer/extras/systrace_config.html',
      'trace_viewer/extras/tcmalloc/heap.html',
      'trace_viewer/extras/tcmalloc/heap_instance_track.html',
      'trace_viewer/extras/tcmalloc/tcmalloc.html',
      'trace_viewer/extras/tcmalloc/tcmalloc_instance_view.html',
      'trace_viewer/extras/tcmalloc/tcmalloc_snapshot_view.html',
      'trace_viewer/trace_viewer.html',
    ],
    'tracing_img_files': [
      'trace_viewer/base/images/chrome-left.png',
      'trace_viewer/base/images/chrome-mid.png',
      'trace_viewer/base/images/chrome-right.png',
      'trace_viewer/base/images/ui-states.png',
      'trace_viewer/extras/cc/images/input-event.png',
      'trace_viewer/extras/gpu/images/checkerboard.png',
      'trace_viewer/extras/tcmalloc/images/collapse.png',
      'trace_viewer/extras/tcmalloc/images/expand.png',
    ],
    'tracing_files': [
      '<@(tracing_css_files)',
      '<@(tracing_js_html_files)',
      '<@(tracing_img_files)',
    ],
  },
  'targets': [
    {
      'target_name': 'generate_about_tracing',
      'type': 'none',
      'actions': [
        {
          'action_name': 'generate_about_tracing',
          'script_name': 'trace_viewer/build/generate_about_tracing_contents',
          'inputs': [
            '<@(tracing_files)',
          ],
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/content/browser/tracing/about_tracing.js',
            '<(SHARED_INTERMEDIATE_DIR)/content/browser/tracing/about_tracing.html'
          ],
          'action': ['python', '<@(_script_name)',
                     '--outdir', '<(SHARED_INTERMEDIATE_DIR)/content/browser/tracing']
        }
      ]
    }
  ]
}
