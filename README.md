# IA-XC-Results
I'm applying an ELO-MMR ranking algorithm to the individual results of Iowa HS Boys cross country meets for the year 2022.

You can contribute by creating .csv files with the following format:
  1. The filename must be formatted starting with the date and race name. "YYYY-MM-DD-RACE NAME.csv"
  2. The .csv file must be formatted with just one entry per line with this format: "CLASS SCHOOL FNAME LNAME GRADYEAR"

Place the .csv files in the csv input directory.  I will run the python script to convert them to json output files.  The json output files are used in the ranking algorithm.
