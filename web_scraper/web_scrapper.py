import requests
from bs4 import BeautifulSoup
import json

url = "https://en.wikipedia.org/wiki/History_of_Mexico"


def get_citations_needed_count(url):
    page = requests.get(url)
    soup =BeautifulSoup(page.content,'html.parser')
    results = soup.find_all('a',href='/wiki/Wikipedia:Citation_needed')
    return len(results)


print(get_citations_needed_count(url))


def get_citations_needed_report(url):
    page = requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    results = soup.find_all('a',href='/wiki/Wikipedia:Citation_needed')
    content = []
    for i in range(len(results)):
            try:
                citation_number = 1+i
                paragraph = results[i].parent.parent.parent.getText().strip()


                content.append({'Citation number':citation_number, 'Paragraph':paragraph})

            except AttributeError as e:
                continue
    return content

print(get_citations_needed_report(url))


















#----------------------- demo
# page = requests.get(URL)
# print(page.content)

# soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)

# results = soup.find(id="SearchResults")
# # print(results.prettify())

# jobs_list = results.find_all('span', class_='card-content')
# print(f"Type is {type(jobs_list)} and Length is {len(jobs_list)}")

# # print(jobs_list[0])


# class Job:
#     all_jobs = []
#     def __init__(self, title, company, location):
#         self.title = title
#         self.company = company
#         self.location = location
#         Job.all_jobs.append({'title':self.title, 'location': self.location, 'company':self.company})

#     def __repr__(self):
#         return f"\nTitle: {self.title}\nCompany: {self.company}\nLocation: {self.location}\n"

#     @classmethod
#     def dump_all(cls):
#         return cls.all_jobs



# all_jobs = []

# for job in jobs_list:
#     try:
#         company = job.find('div', class_='company').find('span', class_='name').text.strip()
#         title = job.find('h2', class_='title').find('a').text.strip()
#         location = job.find('div', class_='location').text.strip()
#         # Using a dictionary:
#         # all_jobs.append({'title':title, 'company':company, 'location':location})

#         #Using the Job class:
#         all_jobs.append(Job(title, company, location))
#     except AttributeError as e:
#         continue

# print(all_jobs)

# with open('data.json', 'w') as outfile:
#     json.dump(Job.dump_all(), outfile) # Using the class method of Job class
#     # json.dump(all_jobs, outfile) # Regular dictionary dumping


# # Search for all Python jobs
# # jobs_list_python = results.find_all('h2', string = lambda text: 'python' in text.lower()) # Filter
# # print(len(jobs_list_python))
