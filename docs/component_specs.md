***Software components**
____________
____________
Data manager
___________
Our main data sets are including movies data and reviews data. The data are stored in two separate CSV files. Our data manager will import the data, handle missing values and null values, clean these two data sets and finally merge them together. So the data manager includes three parts: clean reviews data, clean movies data, merge movies and reviews data. 

The reviews data are including 13419 entries. The columns are including: 'critic', 'fresh', 'imdb', 'publication', 'quote', 'review_date',rtid', 'title'.

The movies data are including 9423 entries. The coulmd are including: 'title', 'imdbID', 'year', 'rtID', 'rtAllCriticsRating','rtAllCriticsNumReviews', 'rtAudienceNumRatings', 'rtAudienceScore'.

Visualization manager Ⅰ
___________
It has the input of year range including start year and end year. After receiving the year, it calculates the medium rating grouped by year and only select the year within the range. And it will plot the trend for the median rating for that period. The output is a clear trend line and in the x-axis we have year, in the y-axis we can see the median rating.

Visualization manager Ⅱ
___________
With the support of  word-sentiments from NRC Word Emotion Association  as well as NLTK library in Python, we did the sentiment analysis for all the quotes of a certain critic. We firstly select the top 5 critics in that year who have most quotes. And then we visualize their sentiment scores. The visualization will show five charts for those five critics and it had a dropdown for filtering different emotions. 

Visualization manager III
___________
By having quotes of the five critics, we use wordcloud package to do the word frequency analysis and visualize the words frequency as word cloud. 


Interactions to accomplish use cases
___________
Overall, the interactions are between the user and the interface, the interface and the Python program, the Python program and the data manager. The data manager will clean all the data first and create a usable subset of data. Then the visualization part can use the data for plot.

i.e. Use Case as a Movie Magazine Manager

The users are firsly input a time range to see the overal median ratings among all the movies within that time span. The program will generate a plot to show the trendline of median ratings. And then the user could select a year that he/she is interested in. The program will generate a table showing the most popular critics within that year who have the top amount of critics. Then the program will show the sentiment analysis for these five critics and users could compare the critics in each emotion. By knowing the emotion tendency of a specific critic the magzine manager could have a better understanding of the potential critics. 

_____________
_____________
Preliminary plan
___________
•	Load the data, clean the data and explore the data 
•	Clarify goal for this project and determine the user cases 
•	Write the preliminary code and determine the data manager and visualization manager
•	Code review with TA and update the code 
•	Write up the project and set up for the Python Program
•	Make the program ready-to-use and do final Presentation


