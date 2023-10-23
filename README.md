# project-1
# Overview

This aim of this project is to clean and format a dataset containing information about shark attacks, to find information about the more vulnerable profile, the more dangerous place, month and day of the week and what are the more common injuries provoked by sharks on surfers. 
<br>

# Requirements/Libraries Used:
This code was written in Python/Jupyter Notebook, using the following libraries:
<br>
- Numpy
- Pandas
- matplotlib.pyplot
- Seaborn
- re
<br>
 

# Questions:
<br>

## 1- What profile do sharks find more attractive?
## 2- Where and when are there more shark attacks?
## 3- What is the most common injury among surfers attacked by sharks?

<br>

# Most attractive profile:

For this question we have a clear conclusion: the most vulnerable group when we talk about being attacked by a shark are men between 10 and 20 years old followed by men between 20 and 30 years old. 

An interesting thing to note is that in all group ages male receive more attacks than female. This might be due to more man practicing water sports, specially in the earlier years reported in the dataset.


![age_sex_plot](https://github.com/patriciazapatab/project-1/blob/main/images/age_sex.png?raw=true)

When we compare age distributions by gender using boxplots, we can observe that as more attacks are reported data gets more concentrated around the 25 years old. 

![age_M](https://github.com/patriciazapatab/project-1/blob/main/images/age_M.png?raw=true)

We also find more outliers on the male group than in the female group. Since we have less records results are not as conclusive.

![age_F](https://github.com/patriciazapatab/project-1/blob/main/images/age_F.png?raw=true)

# Where are there more shark attacks? 

Florida in the USA is by far the area with more shark attacks. Australia and South Africa follow 2nd and 3rd position. However, adding their attacks together they are still under USA.

<br>

![countries_plot](https://github.com/patriciazapatab/project-1/blob/main/images/countries.png?raw=true)

In the case of Florida the attacks are almost equal to the ones in Hawaii, California, South and North Carolina, Texas, New Jersey, New York and Oregon added together.

![USA_plot](https://github.com/patriciazapatab/project-1/blob/main/images/usa_areas.png?raw=true)


# What months prefer the sharks to attack? Has this changed from year 2000?

After analyzing the data it is clear that sharks conciously wait for humans to be relaxed in late summer to attack. July, August and September are the months with more attacks. 

![month_plot](https://github.com/patriciazapatab/project-1/blob/main/images/month.png?raw=true)

If we look only at the data after 2000 we can observe a few changes. Even though July, August and September still have the higher number of attacks, during the last years attacks in September have become more frequent than in August. It is possible that climate change and the increase in water temperature have affected sharks behaviours. 

![month_after_2000_plot](https://github.com/patriciazapatab/project-1/blob/main/images/month_2000.png?raw=true)

When we take a deeper look into the prefered days to attack weekends win over weekdays, being Sunday the one with more attacks.

![day_of_week](https://github.com/patriciazapatab/project-1/blob/main/images/day_of_week.png?raw=true)

This is probably because of more people enjoying the beach during the weekend. Nevertheless, I like the idea of sharks deliberately thinking about ruining humans' days off.

# What is the most common injury among surfers attacked by sharks?

After classifying many ways of getting attacked by a shark we conclude that surfing is the more risky activity. This might be because both the shape and the movement of a surfer are the more similar thing to a tasty meal on the water.

This is common for both worldwide and Florida. But we can notice some differences for the rest of activities. For example, it is more common to get attacked by a shark fishing or spearfishing in Florida than in the rest of countries. 

Activities that receive more attacks worldwide:

![activities_worldwide](https://github.com/patriciazapatab/project-1/blob/main/images/activities_florida.png?raw=true)

Activities that receive more attacks in Florida:

![activities_Florida](https://github.com/patriciazapatab/project-1/blob/main/images/activities_worldwide.png?raw=true)

In terms of the most common injuries produced by shark bites on surfers, the lower limbs are the ones that suffer the most. Injuries involving the foot, the ankle or the heel account for slightly more than the 70% of surfers injuries.


![surfers_injuries](https://github.com/patriciazapatab/project-1/blob/main/images/surfers_injuries.png?raw=true)

# In Conclusion
- If you are a man between 10 and 20 years old avoid surfing on weekends in July in Florida, you have a higher chance than anyone else to get attacked by a shark.

- If you choose to ignore the first advice, protect your feet, or you run the risk of losing them.