## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
mean_group_b =  np.mean(weight_lost_b)

print(mean_group_a)
print(mean_group_b)

## 4. Test statistic ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
mean_group_b = np.mean(weight_lost_b)

mean_difference = mean_group_b - mean_group_a
print(mean_difference)

## 5. Permutation test ##

mean_difference = 2.52
print(all_values)
import numpy as np

mean_differences = []
for i in range(1000):
    group_a =[]
    group_b =[]
    for value in all_values:
        assignment_chance =  np.random.rand()
        if assignment_chance >= 0.5:
            group_a.append(value)
        else:
            group_b.append(value)
          
    iteration_mean_difference = np.mean(group_b) - np.mean(group_a)
    mean_differences.append(iteration_mean_difference)
    
plt.hist(mean_differences)
plt.show()
            

## 7. Dictionary representation of a distribution ##

sampling_distribution = {}

for df in mean_differences:
    if sampling_distribution.get(df, False):
        sampling_distribution[df] = sampling_distribution[df] +1
    else:
        sampling_distribution[df] = 1
        

## 8. P value ##

frequencies = []
for keys in sampling_distribution:
    if keys >= 2.52 :
        frequencies.append(keys)
        
sum_value = np.sum(frequencies)

p_value =sum_value/1000
print(p_value)