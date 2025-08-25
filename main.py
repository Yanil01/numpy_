from mean_var_std import calculate
import demographic_data_analyzer
import medical_data_visualizer

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

demographic_data_analyzer.calculate_demographic_data()

medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()
