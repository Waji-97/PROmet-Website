from bs4 import BeautifulSoup
import requests

def scrape_job_posts():
    url = 'https://job.incruit.com/jobdb_list/searchjob.asp'
    params = {
        'svc': 'jobs',
        'job': 'list',
        'page': '1',
        'bsort': '3',
        'ind': '200010',
        'isalary': '101',
        'isalarymax': '200'
    }
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')
    job_posts = soup.select('#listContent > li')
    results = []
    for post in job_posts:
        title = post.select_one('.cl_top a').text.strip()
        company = post.select_one('.cpname').text.strip()
        location = post.select('.cl_md span')[2].text.strip()
        link = url + post.select_one('.cl_top a')['href']
        result = {'title': title, 'company': company, 'location': location, 'link': link}
        results.append(result)
    return results

print(scrape_job_posts())