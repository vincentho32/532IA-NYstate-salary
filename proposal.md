# Proposal

## Section 1: Motivation and Purpose

Our role: Data scientist consultancy firm

Target audience: People who would like to work in New York State and want to know the salary situation of different cities in New York State.

Our purpose is to provide our clients with the insights and information they need to succeed in their careers. Specifically, we focus on analyzing data related to job opportunities and salaries in different industries and geographic regions. By sharing our findings with our clients, we aim to help them make informed decisions about their career paths, negotiate better salaries, and achieve their professional goals.

## Section 2: Description of the data

In this project, I am using the Occupational Employment and Wage Statistics data collected by the New York State Government and shared by the [Data.gov](https://catalog.data.gov/dataset/occupational-employment-statistics) . The OEWS (Occupational Employment and Wage Statistics) survey is a biannual mail survey that gathers information from employers about occupational employment and wage rates of wage and salary workers in nonfarm establishments, categorized by industry. This survey relies on a sample of roughly 44,400 establishments, which is divided into two semiannual panels of around 7,400 sampled establishments each. These panels receive forms via mail in May and November of each year. From the data gathered, OEWS estimates are then generated.

The aim of our dashboard is to report actual salary and employment data and not forecast any data , and thus we have only utilized the following columns:

`Area Name` cities name in New York State \
`Occupational Title` job title \
`Employment` employment number of a specific job in a specifc city \
`Mean Wage` mean wage of a specifc job in a specific city \
`Median Wage` median wage of a specifc job in a specific city \
`Entry Wage` entry wage of a specifc job in a specific city \
`Experienced Wage` experienced wage of a specifc job in a specific city


## Section 3: Research questions and usage scenarios

Our project answers the broad research question of: “How do salary and employment of different jobs vary across different cities of the New York State?”. Below we have provided an usage scenario of our product by a member of our target audience:

Alex recently graduated from college with a degree in computer science and is looking for a job in New York state. Alex is interested in finding a job with a competitive salary and good growth opportunities.

He is having difficulty finding reliable salary information for specific job titles in New York state. Many job postings do not include salary information, which makes it difficult for Alex to determine whether a job is a good fit. Additionally, Alex is unsure about the average salary for a junior-level software engineer in New York state.

With this dataset, Alex can access information on the average salary for a variety of job titles in New York state. Alex can use this information to determine whether job offers are competitive and negotiate salary offers if needed. Additionally, Alex can use this information to research the average salary for junior-level software engineers in New York state, which could help them to determine an appropriate salary range for their job search.

With the dashboard, Alex can easily visualize the distribution of salaries for different job titles and industries in New York state. He can use the box plot to compare the median and range of salaries for different job titles and industries, and use the histogram to get a sense of the overall distribution of salaries. This information can help him to identify job opportunities that offer a competitive salary and determine whether a job offer is within the expected salary range for his level of experience.