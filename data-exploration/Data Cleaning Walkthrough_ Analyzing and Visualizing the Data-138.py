## 3. Finding Correlations With the r Value ##

correlations = combined.corr()


correlations = correlations['sat_score']
print(correlations)

## 5. Plotting Enrollment With the Plot() Accessor ##

import matplotlib.pyplot as plt

plt.scatter(x= combined['total_enrollment'], y= combined['sat_score'])
plt.xlabel('total_enrollment')
plt.ylabel('sat_score')
plt.show()

## 6. Exploring Schools With Low SAT Scores and Enrollment ##

low_enrollment = combined[combined['total_enrollment']<1000]

low_enrollment = low_enrollment[combined['sat_score'] <1000]

print(low_enrollment['School Name'])


## 7. Plotting Language Learning Percentage ##

plt.scatter(x= combined['ell_percent'] , y=combined['sat_score'])
plt.xlabel('ell_percent')
plt.ylabel('sat_score')
plt.show()

## 8. Calculating District-Level Statistics ##

import numpy as np

districts = combined.groupby('school_dist').agg(np.mean).reset_index()

print(districts)

