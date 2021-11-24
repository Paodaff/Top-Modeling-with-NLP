from os import read
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
sites = [
    "https://www.netex.co.il/index/?c=852BBAA9-A8CB-46CC-98DB-F18140CFC481",
    "https://www.netex.co.il/index/?c=3703D1A2-AD17-491A-BF5A-D155612844BF",
    "https://www.netex.co.il/index/?c=0CD633A4-E011-4A9E-81AB-C9236953CC47",
    "https://www.netex.co.il/index/?c=46A3B2FD-C375-44C4-894E-C906AE61F8F2",
    "https://www.netex.co.il/index/?c=DDBB736E-F697-47DF-B220-C4D14DD03AEB",
    "https://www.netex.co.il/index/?c=96660494-EF28-4124-B342-B6EEC84ECEB6",
    "https://www.netex.co.il/index/?c=95536D35-13EF-45E7-A930-B6E6432D48CD",
    "https://www.netex.co.il/index/?c=1F0A37D2-7377-45BE-9108-A3A89301C0E9",
    "https://www.netex.co.il/index/?c=1B18ECFD-A497-42D1-9B00-902265DB7E52",
    "https://www.netex.co.il/index/?c=3378CCA3-BB5B-4B72-85CE-7FC90CD614CF",
    "https://www.netex.co.il/index/?c=1C97F967-11CC-4FCD-B345-73F7F685752B",
    "https://www.netex.co.il/index/?c=B42295C1-DA6A-4D57-A8F9-6AF4B49AD913",
    "https://www.netex.co.il/index/?c=115F6462-F36C-439A-A811-651C9715A4B8",
    "https://www.netex.co.il/index/?c=3B705D8F-1432-446B-842F-5ACD9C894007",
    "https://www.netex.co.il/index/?c=7643002D-FFFE-4439-B2F9-590DADE1F8FF",
    "https://www.netex.co.il/index/?c=389AAD14-ED8E-4374-9F7E-5501185D3C1B",
    "https://www.netex.co.il/index/?c=A3D65B13-F5C5-47A7-BCE0-54474D0D8E67",
    "https://www.netex.co.il/index/?c=E512245C-C659-4702-A430-4CD05F6CEA78",
    "https://www.netex.co.il/index/?c=F7C3DDB9-D6B8-4CD1-9702-486FCE308ECD",
    "https://www.netex.co.il/index/?c=881AAB72-AD7D-4A81-B983-478E17F69799",
    "https://www.netex.co.il/index/?c=A4F5D10B-A5A9-4C52-A221-3A7730D4DF54",
    "https://www.netex.co.il/index/?c=30BBF4A6-BE6B-4B3F-A949-3840204ACF19",
    "https://www.netex.co.il/index/?c=5C28BAD1-B429-4657-B54A-1F4FA0C2DD08",
    "https://www.netex.co.il/index/?c=1FA979FC-336C-46B0-BD3F-1F7315D34996",
    "https://www.netex.co.il/index/?c=1B8A9E44-3BE1-4E4D-B159-12410444B51E",
    "https://www.netex.co.il/index/?c=C60E7455-BCD9-429D-B29D-0B91FD568516",
    "https://www.netex.co.il/index/?c=07B8323B-93C0-4147-8604-06785E9FF799",
    "https://www.netex.co.il/index/?c=F65721EF-3738-4281-9843-02A6CC8E14EF"
]

forums_per_page_script = """
arr = (document.getElementById("sites_list")).getElementsByTagName('li');
links = [];
len = arr.length;
for(let i = 0; i < len; i++){{
    links.push(arr[i].children[0].children[0].href);
}}
return links;
"""
number_of_pages = 'return document.getElementsByClassName("pagination")[0].childElementCount;'
get_links = """
li = document.getElementsByTagName('li');
links = [];
for(let i = 0; i < li.length; i++){{
    try{{
       links.push(li[i].children[0].children[0].href)    
    }}
    catch{{
        
    }}
}}
return links;
"""

reader = open("Forums_list2.txt", "r")
data = reader.read().split("\n")


# driver = webdriver.Chrome(ChromeDriverManager().install())

# reader = open("links_per_page.txt", "r")
# data = reader.read().split("\n")


# links_list = []
# for site in data:
#     driver.get(site)
#     time.sleep(1)
#     try:
#         links_list.extend(driver.execute_script(forums_per_page_script))
#     except:
#         print(f"{site} Is empty")
# textfile = open("Forums_list2.txt", "w")
# for element in links_list:
#     textfile.write(element + "\n")
# textfile.close()
abc = [
    "https://www.netex.co.il/index/?letter=%D7%90",
    "https://www.netex.co.il/index/?letter=%D7%91",
    "https://www.netex.co.il/index/?letter=%D7%92",
    "https://www.netex.co.il/index/?letter=%D7%93",
    "https://www.netex.co.il/index/?letter=%D7%94",
    "https://www.netex.co.il/index/?letter=%D7%95",
    "https://www.netex.co.il/index/?letter=%D7%96",
    "https://www.netex.co.il/index/?letter=%D7%97",
    "https://www.netex.co.il/index/?letter=%D7%98",
    "https://www.netex.co.il/index/?letter=%D7%99",
    "https://www.netex.co.il/index/?letter=%D7%9B",
    "https://www.netex.co.il/index/?letter=%D7%9C",
    "https://www.netex.co.il/index/?letter=%D7%9E",
    "https://www.netex.co.il/index/?letter=%D7%A0",
    "https://www.netex.co.il/index/?letter=%D7%A1",
    "https://www.netex.co.il/index/?letter=%D7%A2",
    "https://www.netex.co.il/index/?letter=%D7%A4",
    "https://www.netex.co.il/index/?letter=%D7%A6",
    "https://www.netex.co.il/index/?letter=%D7%A7",
    "https://www.netex.co.il/index/?letter=%D7%A8",
    "https://www.netex.co.il/index/?letter=%D7%A9",
    "https://www.netex.co.il/index/?letter=%D7%AA"
]
# list_of_links = []
# for letter in abc:
#     driver.get(letter)
#     time.sleep(1)
#     n_p = driver.execute_script(number_of_pages)
#     if n_p == 0:
#         list_of_links.extend(driver.execute_script(get_links))
#     else:
#         for page in range(1,n_p):
#             driver.get(f"{letter}&c=&pageID={page}")
#             time.sleep(1)
#             list_of_links.extend(driver.execute_script(get_links))
# textfile = open("links_per_page.txt", "w")
# for element in list_of_links:
#     textfile.write(element + "\n")
# textfile.close()
