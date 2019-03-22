# School-Violence-Investigation
According to the Academy for Critical Incident Analysis, between 2000 and 2010, there were 57 incidents of school violence worldwide that had two or more victims.  Twenty eight (almost half!) of those occurred in the United States alone.  Over the past few decades, students and teachers have expressed a growing concern about safety at schools, specifically related to these incidents.  There are a variety of opinions on how best to reduce or protect against these events: increase in security, frequent drills to prepare, mental health outreach, etc.  However, for each suggestion there is always the question of how feasible it is in terms of resources (time and money) to implement nationwide.

This question lead to my analysis of school shooting incidents in the United States from 2010-2018.  It is my purpose through this study to determine if there are early warning signs or common characteristics of areas with school violence in the United States.  More specifically, I am interested in the following questions:
1.  Which variables have the largest positive or negative impact on the likelihood of school violence?
2.  Is school violence more likely to be clustered in similar areas/ times, or more uniformly distributed?
3.  What are the (if any) common characteristics of the schools or counties in which you find the majority of recent school violence?
4.  What relationship (if any) is there between a county’s overall adult/teen health and the likelihood of a school shooting occurring?

## Data
My analysis is based on the following sources:
1.  The Washington Post’s dataset records information on school violence since Columbine in 1998.  It is easily downloadable as a .csv file from the link as well as clear documentation on the variables included.
  Link: https://github.com/washingtonpost/data-school-shootings
2.  County Health Rankings records information and ranks counties in the United States based on various characteristics from 2010 to current.  It is also easily downloadable as a .csv file from the link with clear documentation on the variables included
  Link: http://www.countyhealthrankings.org/explore-health-rankings/rankings-data-documentation

## Results
In this investigation of school violence in the United States from 2010-2018, there were several interesting realizations about its connection to other factors, some particular to the school and others to the county as a whole.  For example, the highest casualty rates all belonged to the “indiscriminate” shooting category, while the majority of all events were “targeted” but with smaller casualty rates, suggesting that interventions may be better focused on these types of school shootings.  It was also surprising that targeted/indiscriminate school shootings occur much higher during January than one would expect.  Possibly, there is a connection between the post-holidays high and a student’s mental health.

However, the in-depth analysis using supervised and unsupervised machine learning algorithms was more inconclusive.  The Ridge regression model struggled to accurately predict the casualty rate of an incident, and the Lasso regression showed no strong features in relation to the casualty rate as well.  The Logistic regression model also struggled to predict the likelihood of an incident of school violence occurring.

## Future Considerations
First, because of the limited scope of the county health data, I was unable to use the complete Washington Post dataset, substantially limiting the size of my sample.  In future studies, I would search for health data that goes further back to include more of the school violence data points.

Secondly, I would like to investigate other model's abilities to predict the severity of an event (via the casualty rate), such as random forests.  Perhaps these could provide a more accurate/reliable prediction than the Ridge linear regression was able to do.
