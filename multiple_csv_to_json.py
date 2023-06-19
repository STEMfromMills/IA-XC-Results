import os, glob, csv, datetime, json

path = 'csv input'

jsonresult = 0
race = 0

for filename in sorted(glob.glob(os.path.join(path, '*.csv'))):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
      reader = csv.reader(f)
      i = 0
      results_list = []
      for row in reader:
         result = []
         result.append(row[0])
         result.append(i)
         result.append(i)
         results_list.append(result)
         i += 1
   
   year = 0
   month = 0
   day = 0
   
   split_filename = filename.split("-")
   
   year = int(split_filename[0].strip("csv input/"))
   month = int(split_filename[1])
   day = int(split_filename[2])

   race_name = split_filename[3].strip(".csv")
   epoch_time = int(datetime.datetime(year,month,day,0,0,race).strftime('%s'))
   
   dictionary = {}
   dictionary = {
      "name": race_name,
      "time_seconds": epoch_time,
      "standings": results_list
   }
   
   if race == 59:
      race = 0
   else:
      race += 1
   
   
   json_object = json.dumps(dictionary, indent=4)

   output_file_name = ""
   output_file_name = "json output/" + str(jsonresult) + ".json"

   jsonresult += 1

   with open(output_file_name, "w") as outfile:
      outfile.write(json_object)

   