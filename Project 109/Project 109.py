import statistics
import pandas as pd
import plotly.express as py

df = pd.read_csv('StudentsPerformance.csv')
score_list = df["math score"].tolist()

mean_s = statistics.mean(score_list)
median_s = statistics.mode(score_list)
mode_s =statistics.mode(score_list)
print("mean of students' scores: ", mean_s)
print("median of students' scores: ", median_s)
print("mode of students' scores: ", mode_s)

stdev_s =statistics.stdev(score_list)
print("Standard Daviation of score: ", stdev_s)

stdev_s1_start,  stdev_s1_end = mean_s - stdev_s, mean_s + stdev_s
percentage_stdev_s1 = [result for result in score_list if result > stdev_s1_start and result < stdev_s1_end]

stdev_s2_start,  stdev_s2_end = mean_s - (2*stdev_s), mean_s + (2*stdev_s)
percentage_stdev_s2 = [result for result in score_list if result > stdev_s2_start and result < stdev_s2_end]

stdev_s3_start,  stdev_s3_end = mean_s - (3*stdev_s), mean_s + (3*stdev_s)
percentage_stdev_s3 = [result for result in score_list if result > stdev_s3_start and result < stdev_s3_end]

print("{}% of data lies within 1 standard daviations".format(len(percentage_stdev_s1)*100/len(score_list)))
print("{}% of data lies within 2 standard daviations".format(len(percentage_stdev_s2)*100/len(score_list)))
print("{}% of data lies within 3 standard daviations".format(len(percentage_stdev_s3)*100/len(score_list)))