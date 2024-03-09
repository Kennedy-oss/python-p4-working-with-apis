import requests

class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
    response = requests.get(URL)
    data = response.json()  # Parse JSON response
    if 'error' in data:
        print("Error from API:", data.get('message'))
    return data

  def program_agencies(self):
    programs = self.get_programs()
    # If the programs variable is an error message, we won't try to process it further.
    if 'error' in programs:
        return []
    
    programs_list = []
    # Additional processing here, adjusted based on the API's correct response structure

    return programs_list

programs = GetPrograms()
agencies = programs.program_agencies()

if agencies:
    for agency in set(agencies):
        print(agency)
else:
    print("No data to display due to API error.")
