import pandas as pd
import statistics
import csv
df = pd.read_csv("StudentsPerformance 3.csv")
math_Score = df["math score"].to_list()

math_mean = statistics.mean(math_Score)
math_median = statistics.median(math_Score)
math_mode = statistics.mode(math_Score)

print("Mean, Median and Mode of height is {}, {} and {} ".format(math_mean, math_median,math_mode))

math_std_deviation = statistics.stdev(math_Score)

math_first_std_deviation_start, math_first_std_deviation_end = math_mean-math_std_deviation,math_mean+math_std_deviation
math_second_std_deviation_start, math_second_std_deviation_end = math_mean-(2*math_std_deviation), math_mean+(2*math_std_deviation)
math_third_std_deviation_start, math_third_std_deviation_end = math_mean-(3*math_std_deviation), math_mean+(3*math_std_deviation)

height_list_of_data_within_1_std_deviation = [result for result in math_Score if result > math_first_std_deviation_start and result < math_first_std_deviation_end]
height_list_of_data_within_2_std_deviation = [result for result in math_Score if result > math_second_std_deviation_start and result < math_second_std_deviation_end]
height_list_of_data_within_3_std_deviation = [result for result in math_Score if result > math_third_std_deviation_start and result < math_third_std_deviation_end]

print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(math_Score)))
print("{}% of data for height lies within 2 standard deviations".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(math_Score)))
print("{}% of data for height lies within 3 standard deviations".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(math_Score)))
