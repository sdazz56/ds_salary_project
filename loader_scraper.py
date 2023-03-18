import glassdoor_scraper as gs
import pandas as pd

#path="/Users/sonudazz/Documents/ds_salary_proj/chromedriver";

df=gs.get_jobs('Data Scientist',15, False, 15);

df

