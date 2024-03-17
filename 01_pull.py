# -----------------------------------------------
#  1. Data Acquisition:
# 
#  Objective: Download all the public course 
#  catalog data in raw HTML format from a 
#  university website.
# 
#  Tools/Resources: Extract all the course 
#  catalog data from one of the follow 
#  three universities:
#     Harvard: https://courses.my.harvard.edu
#     BU: https://www.bu.edu/academics/cas/courses
#     NE: https://catalog.northeastern.edu/course-descriptions
# -----------------------------------------------

import urllib.request
import ssl
import time
import random

# this is the workaround for the SSL certificate error
context = ssl._create_unverified_context()

# URL to the file
urls = [
    'https://www.bu.edu/academics/cas/courses/african-american-studies/',
    'https://www.bu.edu/academics/cas/courses/african-american-studies/2/',
    'https://www.bu.edu/academics/cas/courses/african-american-studies/3/',
    'https://www.bu.edu/academics/cas/courses/african-american-studies/4/',
    'https://www.bu.edu/academics/cas/courses/african-studies-culture-in-english/',
    'https://www.bu.edu/academics/cas/courses/swahili/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-african-languages-linguistics/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-african-languages-linguistics/2/',
    'https://www.bu.edu/academics/cas/courses/isixhosa/',
    'https://www.bu.edu/academics/cas/courses/wolof/',
    'https://www.bu.edu/academics/cas/courses/american-studies/',
    'https://www.bu.edu/academics/cas/courses/anthropology/',
    'https://www.bu.edu/academics/cas/courses/anthropology/2/',
    'https://www.bu.edu/academics/cas/courses/anthropology/3/',
    'https://www.bu.edu/academics/cas/courses/anthropology/4/',
    'https://www.bu.edu/academics/cas/courses/anthropology/5/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-arabic/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-arabic/2/',
    'https://www.bu.edu/academics/cas/courses/archaeology/',
    'https://www.bu.edu/academics/cas/courses/archaeology/2/',
    'https://www.bu.edu/academics/cas/courses/archaeology/3/',
    'https://www.bu.edu/academics/cas/courses/astronomy/',
    'https://www.bu.edu/academics/cas/courses/biochemistry-molecular-biology/',
    'https://www.bu.edu/academics/cas/courses/biology/',
    'https://www.bu.edu/academics/cas/courses/biology/2/',
    'https://www.bu.edu/academics/cas/courses/biology/3/',
    'https://www.bu.edu/academics/cas/courses/biology/4/',
    'https://www.bu.edu/academics/cas/courses/biology/5/',
    'https://www.bu.edu/academics/cas/courses/biology/6/',
    'https://www.bu.edu/academics/cas/courses/biology/7/',
    'https://www.bu.edu/academics/cas/courses/chemistry/',
    'https://www.bu.edu/academics/cas/courses/chemistry/2/',
    'https://www.bu.edu/academics/cas/courses/chemistry/3/',
    'https://www.bu.edu/academics/cas/courses/chemistry/4/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-chinese/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-chinese/2/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-chinese/3/',
    'https://www.bu.edu/academics/cas/courses/cinema-media-studies/',
    'https://www.bu.edu/academics/cas/courses/cinema-media-studies/2/',
    'https://www.bu.edu/academics/cas/courses/classical-studies/',
    'https://www.bu.edu/academics/cas/courses/classical-studies/2/',
    'https://www.bu.edu/academics/cas/courses/classical-studies/3/',
    'https://www.bu.edu/academics/cas/courses/modern-greek/',
    'https://www.bu.edu/academics/cas/courses/comparative-literature/',
    'https://www.bu.edu/academics/cas/courses/comparative-literature/2/',
    'https://www.bu.edu/academics/cas/courses/comparative-literature/3/',
    'https://www.bu.edu/academics/cas/courses/computer-science/',
    'https://www.bu.edu/academics/cas/courses/computer-science/2/',
    'https://www.bu.edu/academics/cas/courses/computer-science/3/',
    'https://www.bu.edu/academics/cas/courses/computer-science/4/',
    'https://www.bu.edu/academics/cas/courses/core-curriculum/',
    'https://www.bu.edu/academics/cas/courses/earth-environment/',
    'https://www.bu.edu/academics/cas/courses/earth-environment/2/',
    'https://www.bu.edu/academics/cas/courses/earth-environment/3/',
    'https://www.bu.edu/academics/cas/courses/earth-environment/4/',
    'https://www.bu.edu/academics/cas/courses/earth-environment/5/',
    'https://www.bu.edu/academics/cas/courses/economics/',
    'https://www.bu.edu/academics/cas/courses/economics/2/',
    'https://www.bu.edu/academics/cas/courses/economics/3/',
    'https://www.bu.edu/academics/cas/courses/economics/4/',
    'https://www.bu.edu/academics/cas/courses/economics/5/',
    'https://www.bu.edu/academics/cas/courses/editorial-studies/',
    'https://www.bu.edu/academics/cas/courses/english/',
    'https://www.bu.edu/academics/cas/courses/english/2/',
    'https://www.bu.edu/academics/cas/courses/english/3/',
    'https://www.bu.edu/academics/cas/courses/english/4/',
    'https://www.bu.edu/academics/cas/courses/english/5/',
    'https://www.bu.edu/academics/cas/courses/english/6/',
    'https://www.bu.edu/academics/cas/courses/english/7/',
    'https://www.bu.edu/academics/cas/courses/first-year-experience/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-french/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-french/2/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-german/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-hebrew/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-hindi/',
    'https://www.bu.edu/academics/cas/courses/history/',
    'https://www.bu.edu/academics/cas/courses/history/2/',
    'https://www.bu.edu/academics/cas/courses/history/3/',
    'https://www.bu.edu/academics/cas/courses/history/4/',
    'https://www.bu.edu/academics/cas/courses/history/5/',
    'https://www.bu.edu/academics/cas/courses/history/6/',
    'https://www.bu.edu/academics/cas/courses/history/7/',
    'https://www.bu.edu/academics/cas/courses/art-history/',
    'https://www.bu.edu/academics/cas/courses/art-history/2/',
    'https://www.bu.edu/academics/cas/courses/art-history/3/',
    'https://www.bu.edu/academics/cas/courses/art-history/4/',
    'https://www.bu.edu/academics/cas/courses/interdisciplinary-studies/',
    'https://www.bu.edu/academics/cas/courses/international-relations/',
    'https://www.bu.edu/academics/cas/courses/international-relations/2/',
    'https://www.bu.edu/academics/cas/courses/international-relations/3/',
    'https://www.bu.edu/academics/cas/courses/international-relations/4/',
    'https://www.bu.edu/academics/cas/courses/international-relations/5/',
    'https://www.bu.edu/academics/cas/courses/international-relations/6/',
    'https://www.bu.edu/academics/cas/courses/international-relations/7/',
    'https://www.bu.edu/academics/cas/courses/internships/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-italian/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-japanese/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-japanese/2/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-japanese/3/',
    'https://www.bu.edu/academics/cas/courses/jewish-studies/',
    'https://www.bu.edu/academics/cas/courses/jewish-studies/2/',
    'https://www.bu.edu/academics/cas/courses/jewish-studies/3/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-korean/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-korean/2/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-linguistics/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-linguistics/2/',
    'https://www.bu.edu/academics/cas/courses/literary-translation/',
    'https://www.bu.edu/academics/cas/courses/marine-science/',
    'https://www.bu.edu/academics/cas/courses/mathematics-statistics/',
    'https://www.bu.edu/academics/cas/courses/mathematics-statistics/2/',
    'https://www.bu.edu/academics/cas/courses/mathematics-statistics/3/',
    'https://www.bu.edu/academics/cas/courses/mathematics-statistics/4/',
    'https://www.bu.edu/academics/cas/courses/natural-sciences/',
    'https://www.bu.edu/academics/cas/courses/neuroscience/',
    'https://www.bu.edu/academics/cas/courses/neuroscience/2/',
    'https://www.bu.edu/academics/cas/courses/neuroscience/3/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-persian/',
    'https://www.bu.edu/academics/cas/courses/philosophy/',
    'https://www.bu.edu/academics/cas/courses/philosophy/2/',
    'https://www.bu.edu/academics/cas/courses/philosophy/3/',
    'https://www.bu.edu/academics/cas/courses/philosophy/4/',
    'https://www.bu.edu/academics/cas/courses/physics/',
    'https://www.bu.edu/academics/cas/courses/physics/2/',
    'https://www.bu.edu/academics/cas/courses/physics/3/',
    'https://www.bu.edu/academics/cas/courses/political-science/',
    'https://www.bu.edu/academics/cas/courses/political-science/2/',
    'https://www.bu.edu/academics/cas/courses/political-science/3/',
    'https://www.bu.edu/academics/cas/courses/political-science/4/',
    'https://www.bu.edu/academics/cas/courses/political-science/5/',
    'https://www.bu.edu/academics/cas/courses/political-science/6/',
    'https://www.bu.edu/academics/cas/courses/political-science/7/',
    'https://www.bu.edu/academics/cas/courses/political-science/8/',
    'https://www.bu.edu/academics/cas/courses/political-science/9/',
    'https://www.bu.edu/academics/cas/courses/political-science/10/',
    'https://www.bu.edu/academics/cas/courses/political-science/11/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-portuguese/',
    'https://www.bu.edu/academics/cas/courses/psychology/',
    'https://www.bu.edu/academics/cas/courses/psychology/2/',
    'https://www.bu.edu/academics/cas/courses/psychology/3/',
    'https://www.bu.edu/academics/cas/courses/religion/',
    'https://www.bu.edu/academics/cas/courses/religion/2/',
    'https://www.bu.edu/academics/cas/courses/religion/3/',
    'https://www.bu.edu/academics/cas/courses/religion/4/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-russian/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-russian/2/',
    'https://www.bu.edu/academics/cas/courses/sea-semester/',
    'https://www.bu.edu/academics/cas/courses/senior-year-development/',
    'https://www.bu.edu/academics/cas/courses/sociology/',
    'https://www.bu.edu/academics/cas/courses/sociology/2/',
    'https://www.bu.edu/academics/cas/courses/sociology/3/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-spanish/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-spanish/2/',
    'https://www.bu.edu/academics/cas/courses/modern-languages-turkish/',
    'https://www.bu.edu/academics/cas/courses/womens-studies/',
    'https://www.bu.edu/academics/cas/courses/womens-studies/2/',
    'https://www.bu.edu/academics/cas/courses/womens-studies/3/',
    'https://www.bu.edu/academics/cas/courses/writing/',
]

# fetch content
def pull(url):
    # fetch the content
    response = urllib.request.urlopen(url, context=context).read()
    # decode the content
    text = response.decode('utf-8')
    # return the content
    return text

# save file
def store(data, file):
    f = open('data/' + file+ '.html', 'w')
    f.write(data)
    f.close()
    print('File saved as ' + file+ '.html')

# loop through the URLs
for url in urls:
    start_index = url.find('courses/') + len('courses/')
    end_index = url.rfind('/')
    data = pull(url)
    file = url[start_index:end_index].replace('/', '-')
    print('Fetching ' + file)
    store(data, file)
    # pause for a random time
    time.sleep(random.randint(10, 25))