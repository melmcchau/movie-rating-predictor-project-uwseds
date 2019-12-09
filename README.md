# CSE583-Movie Critic Analysis Over Time - Group 5
[![Build Status](https://travis-ci.org/melmcchau/movieCriticsOverTime.svg?branch=master)](https://travis-ci.org/melmcchau/movieCriticsOverTime)

### Project Overview
Reviews on movies are created by critics and have an impact on the success and awards of a given movie. These reviews include chunks of text that describe the movie and the review. This repository provides the user information about how movies have been rated over time and details about critic sentiment so they can investigate changes. 

### File Organization

#### 1.Data
The data folder includes the two data sets we use in the project, they are:
* List of movies that came out from 1903 to 2011
* List of reviews from Rotten Tomatoes from 1929 to 2013 including their score, the reviewer, and the reviewer contents

#### 2.Docs
The docs folder includes the design documents of the project, they are:
* Functional Specification 
This document include the background of the assignment, the user profile, the data sources  as well as use cases.
* Component Specification 
This document have sections for software components, interactions to accomplish use cases and priliminary plan.
* Presentation
This document include the presentation for our project overview, data source, user case and analysis. 

#### 3.Code
The code folder includes
* the ipython notebook (which is used as a front-end)
* individual modules that clean, process, and present the data

### How to Use
To use this program, you will need access to the following packages:
Pandas, Altair, Jupyter Notebook

You can interact with the program using the jupyter notebook named "Movie Critics Over Time". 
* As an interested user:
    1. Clone the repository to your computer using git clone https://github.com/melmcchau/movieCriticsOverTime.git
    2. Navigate to the folder in the command line and type "jupyter notebook"
    3. Run the Jupyter Notebook for "movieCriticsOverTime" - Add time ranges and years of interest to explore the data.
    4. Reset and re-run as needed. 
  
 * As a developer looking to re-use the code:
    1. Clone the repository to your computer
    2. Navigate to the folder and open Jupyter Notebook
    3. Replace the data source with your data source (ensure that the formatting matches)
    4. Make necessary changes to apply it to your use case
  

