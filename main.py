from mean_var_std import calculate
import demographic_data_analyzer
import medical_data_visualizer
import time_series_visualizer

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

demographic_data_analyzer.calculate_demographic_data()

medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()


time_series_visualizer.draw_line_plot()
time_series_visualizer.draw_bar_plot()
time_series_visualizer.draw_box_plot()