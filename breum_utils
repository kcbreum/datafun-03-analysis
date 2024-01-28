# Online Python-3 Compiler (Interpreter)
''' This module provides a reusable byline for the Impact Analytics's services. '''

import math
import statistics

# Defining variables
company_name: str = "Impact Analytics Inc."
count_active_projects: int = 6
has_international_presence: bool = True
average_client_satisfaction: float = 4.5
services_offered: list = ["Data Analysis", "Machine Learning Consulting", "Business Intelligence Solutions"]
satisfaction_scores: list = [4.4, 4.2, 4.8, 4.9, 4.3]

# Difining non-string variables
active_projects_string: str = f"Active Projects: {count_active_projects}"
international_presence_string: str = f"International Presence: {has_international_presence}"
client_satisfaction_string: str = f"Average Client Satisfaction: {average_client_satisfaction}"

# Calculating descriptive statistics
import statistics

smallest= min(satisfaction_scores)
largest= max(satisfaction_scores)
total= sum(satisfaction_scores)
count= len(satisfaction_scores)
mean= statistics.mean(satisfaction_scores)
mode= statistics.mode(satisfaction_scores)
median= statistics.median(satisfaction_scores)
standard_deviation=statistics.stdev(satisfaction_scores)

stats_string: str = f"""
Descriptive Statistics for Our Satisfaction Scores:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""

# Byline string
byline: str = f"""
{company_name}
{active_projects_string}
{international_presence_string}
{client_satisfaction_string}
{services_offered}
{stats_string}
"""

# Defining main function
def main():
    ''' Display all output'''
    print(company_name)
    print(active_projects_string)
    print(international_presence_string)
    print(client_satisfaction_string)
    print(services_offered)
    print(stats_string)

    # If all of the above works, then the byline should work too:
    print(byline)
    
# Conditions
if __name__ == '__main__':
    main()
