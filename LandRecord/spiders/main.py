# ----------- Import Libraries ----------- #
import requests
from scrapy import Selector
import pandas as pd

# ----------- Taking request, response and handle exception ----------- #
def jamabandi_nic_in():

    url = 'https://jamabandi.nic.in/land%20records/NakalRecord'
    cookies = {
        'jamabandiID': '1nl02vnjlt2okmfdv5ln52bu',
    }
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-IN,en-GB;q=0.9,en;q=0.8,tr-TR;q=0.7,tr;q=0.6,en-US;q=0.5',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://jamabandi.nic.in',
        'referer': 'https://jamabandi.nic.in/land%20records/NakalRecord',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }
    data = {
        '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$GridView1',
        '__EVENTARGUMENT': 'Select$0',
        '__LASTFOCUS': '',
        '__VIEWSTATE': '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',
        '__VIEWSTATEGENERATOR': '9C91F57C',
        '__SCROLLPOSITIONX': '0',
        '__SCROLLPOSITIONY': '0',
        '__VIEWSTATEENCRYPTED': '',
        '__EVENTVALIDATION': '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',
        'ctl00$ContentPlaceHolder1$a': 'RdobtnKhasra',
        'ctl00$ContentPlaceHolder1$ddldname': '01',
        'ctl00$ContentPlaceHolder1$ddltname': '001',
        'ctl00$ContentPlaceHolder1$ddlvname': '02848',
        'ctl00$ContentPlaceHolder1$ddlPeriod': '2017-2018',
        'ctl00$ContentPlaceHolder1$ddlkhasra': '1',
    }

    s = requests.Session()

    response1 = s.post(url, cookies=cookies, data=data)

    if response1.status_code == 200:
        pass
    else:
        response1 = s.post(url, cookies=cookies, headers=headers, data=data)

    url_new = 'https://jamabandi.nic.in/land%20records/Nakal_khewat'
    response2 = s.get(url_new, cookies=cookies, headers=headers)

    if response2.status_code == 200:
        pass
    else:
        response2 = s.get(url_new)

    main_html_respo = Selector(response1)
    html_respo = Selector(response2)

# -------- Applied logic for x-path, list and dictionary ------- #

    try:
        district_name = main_html_respo.xpath('//select[@name="ctl00$ContentPlaceHolder1$ddldname"]//option[@selected="selected"]/text()').get('')
    except:
        district_name = ''

    try:
        district_code = main_html_respo.xpath('//select[@name="ctl00$ContentPlaceHolder1$ddldname"]//option[@selected="selected"]//@value').get('')
    except:
        district_code = ''

    try:
        tehsil_name = main_html_respo.xpath('//select[@name="ctl00$ContentPlaceHolder1$ddltname"]//option[@selected="selected"]/text()').get('')
    except:
        tehsil_name = ''

    try:
        tehsil_code = main_html_respo.xpath('//select[@name="ctl00$ContentPlaceHolder1$ddltname"]//option[@selected="selected"]/@value').get('')
    except:
        tehsil_code = ''

    try:
        village_name = main_html_respo.xpath('//select[@name="ctl00$ContentPlaceHolder1$ddlvname"]//option[@selected="selected"]/text()').get('')
    except:
        village_name = ''

    try:
        village_code = main_html_respo.xpath('//select[@name="ctl00$ContentPlaceHolder1$ddlvname"]//option[@selected="selected"]/@value').get('')
    except:
        village_code = ''

    try:
        jamabandi_Year = main_html_respo.xpath('//select[@name="ctl00$ContentPlaceHolder1$ddlPeriod"]/option[@selected="selected"]/text()').get('')
    except:
        jamabandi_Year = ''

    khatoni_no_list = []
    khewat_no_list = []
    khewat_list = html_respo.xpath('//table[@id="GridView1"]//tr')
    for i in khewat_list:
        khewat_khatoni_no_list = i.xpath(f'.//td')

        khewat_no = ''
        for j in khewat_khatoni_no_list:
            if khewat_no == '':
                khewat_no = j.xpath('.//text()').get('')
                if khewat_no:
                    khewat_no_list.append(khewat_no)
            else:
                khatoni_no = j.xpath('.//text()').get('')
                if khatoni_no:
                    khatoni_no_list.append(khatoni_no)
                    break

    khatoni_no = ','.join([i.strip() for i in khatoni_no_list if i.strip()])
    khewat_no = ','.join([i.strip() for i in khewat_no_list if i.strip()])

    inner_details_key_list = html_respo.xpath('//table//tr//td//span[contains(@id,"Label")]/text()').getall()
    inner_details_value_list = html_respo.xpath('//table//tr//td//span[contains(@id,"lbl")]/text()').getall()
    main_inner_details_value_list = []
    for inner_details_key, inner_details_value in zip(inner_details_key_list, inner_details_value_list):
        main_inner_details_value_list.append(f'{inner_details_key} - {inner_details_value}'.replace(':', ''))

    inner_details = ', '.join(main_inner_details_value_list)

# ----------- Pass attributes data in item ------------#

    item = {}
    item['district_name'] = district_name
    item['district_code'] = district_code
    item['tehsil_name'] = tehsil_name
    item['tehsil_code'] = tehsil_code
    item['village_name'] = village_name
    item['village_code'] = village_code
    item['jamabandi_Year'] = jamabandi_Year
    item['khatoni_no'] = khatoni_no
    item['khewat_no'] = khewat_no
    item['inner_details'] = inner_details

#---------- Data file export in excel format -----------#

    df = pd.DataFrame([item])
    df.to_excel('jamabandi.xlsx', index=False)


if __name__ == '__main__':
    jamabandi_nic_in()
