***Software components**
____________
____________
Data manager
___________
The data are stored in csv file and we import it into Python Jupyter Notebook. The data itself is messy and the data quality is not high. We only keep reviews data with quotes which are not null value. We only selected the features we need from both data sets and stored them into Python DataFrame. So the data manager includes three parts: clean reviews data, clean movies data, merge movies and reviews data. 

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

Interested in a Critic - Derek Adams, by loading into our Python program. The interface will jump out a blank to let the user fill in the Critic’s name that she/he is interested in. After inputting the name, the data manager will query the data needed for the plot. The Python function will do the plot and show the visualization in the interface. If the user is also interested in the sentiment, the Python program will call the data manager again and show the emotion analysis. 

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


