Background 
___________

Reviews on movies are created by critics and have an impact on the success and awards of a given movie. These reviews include chunks of text that describe the movie and the review, this project is providing the user information about how a critic rates movies over time so they can see if there is variation in rating and sentiment over the years. The problems we will solved are as follows:
•	The median of movie rating trend line for all the movies we have during a time span
•	Sentiment analysis for the top five critics who have most quotes in a specific year
•	Word frequency analysis for the quotes of top critics in a specific year

User Profile
____________
The movie research center or some movie magazine organizations care about the critic’s rating and sentiment. Knowing the rating trend line as well as the sentiment analysis for a specific critic could help them better choose the right critic for evaluating important movies.
Our deliverable will be python modules, users could program with Python and run the functions, the program will have step-by-step instruction to lead the user see the results they need.  

Data Sources
____________
Our data sources are including reviews data and movies data from Rotten Tomatoes websites. Both the movies data and reviews data are tabular data saved in CSV file. 
•	The Movies data are including 65000 different movies from 1903 to 2011. The data structure including movie id, release year, number of reviews as well as ratings. 
•	The Reviews data are ranging from 1929 to 2013 including their score, the reviewer, and the reviewer contents

User Case
___________

To use: open jupyter notebook and run the kernel

•	Use Case 1 

Input:  When prompted, input a starting year and end year of interest

Output: A rating trend line within the time span 
__

After viewing the visualization over time, select a year of interest to you. 

•	Use Case 2

Input:  when prompted, imput a year of interest to you from the visualizaiton

Output: TOP5 Critics/ Sentiment Score /Interactive Comparison/Word Cloud for the five critics 
__

