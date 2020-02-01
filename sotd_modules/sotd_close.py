def sendMail(to, subject, text):
    assert type(to)==list

    msg = MIMEMultipart()
    msg['From'] = self.smtpUser
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    server = smtplib.SMTP('mail.everysale.co.uk:587')
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    server.login(self.smtpUser, self.smtpPass)
    server.sendmail(self.smtpUser, to, msg.as_string())

    server.quit()

def get_last_job_key(api_key, project_id):

    client = ScrapinghubClient(api_key)

    projects = client.projects.list()

    project = client.get_project(project_id)
    last_jobs = project.jobs.iter(state="finished", count=1)
    for item in last_jobs:
        last_job_key = item["key"]

    job = client.get_job(last_job_key)

    return last_job_key

def get_last_items_scraped_number(api_key, job_key):

    items_count = 0
    hot_deal_count = 0
    reselling_count = 0
    i = 0

    while (((self.items_scraped * 2) < items_count) or (items_count < (self.items_scraped / 2))) and (i < 5):
        items_count = 0
        hot_deal_count = 0
        reselling_count = 0
        self.old_reselling_list = []
        i += 1
        r = requests.get(f'https://storage.scrapinghub.com/items/{job_key}?apikey={api_key}&format=csv&include_headers=0&fields=name,price,rrp,url,images,colour,sizes,department,gender,main_category,sub_category,discount_perc,pound_saving,percentage_group,price_category,hot_deal,unsored_sizes,stock,shop,brand,description,description2,date_found,devliery_cost,click_collect,commission,images2,custom1,custom2,custom3,custom4')
        content = r.text

        new = re.match('.*?([0-9]+)$', job_key).group(1)
        sub = int(new) - 1
        job_key = job_key.replace(new, str(sub))

        data = list(csv.reader(content.split('\n'), delimiter=','))
        for row in data[:-1]:
            if (float(row[1]) < float(row[2]) * self.items_discount):
                items_count += 1
            if (float(row[1]) < float(row[2]) * self.hot_deal_discount):
                hot_deal_count += 1
            if (float(row[1]) < float(row[2]) * self.reselling_discount):
                reselling_count += 1
                self.old_reselling_list.append(row)

        print("###########################")
        print("One While Instance")
        print(f"Final i value: {i}")
        print(f"Last items Scraped: {items_count}")
        print(f"self.items_scraped: {self.items_scraped}")
        print(f"Last Hot Deals Scraped: {hot_deal_count}")
        print(f"self.hot_deal_scraped: {self.hot_deal_scraped}")
        print(f"Last reselling Scraped: {reselling_count}")
        print(f"self.reselling_scraped: {self.reselling_scraped}")
        print("###########################")


        time.sleep(3)
        print(f"RUN WHILE LOOP {i} TIMES")

    if 1 < i < 5:
        items_count = 0
        print("THERE WERE BETWEEN 2 AND 4 LOOPS BEFORE BREAK - NO IMPORT!")

    if i == 5 and ((self.items_scraped * 3) < items_count) and (items_count > 15):
        items_count = 0

    print("###########################")
    print("This caused a BREAK in the While Loop")
    print(f"Final i value: {i}")
    print(f"Last items Scraped: {items_count}")
    print(f"self.items_scraped: {self.items_scraped}")
    print(f"Last Hot Deal Scraped: {hot_deal_count}")
    print(f"self.hot_deal_scraped: {self.hot_deal_scraped}")
    print(f"Last reselling Scraped: {reselling_count}")
    print(f"self.reselling_scraped: {self.reselling_scraped}")
    print("###########################")
    print("###########################")

    return items_count, hot_deal_count, reselling_count

def otherstuff(store_url):

    job_key = sotd_close.get_last_job_key(self.api_key, self.project_id)

    items_count, hot_deal_count, reselling_count = sotd_close.get_last_items_scraped_number(self.api_key, job_key)

    for new in self.new_reselling_list:
        old_names = [x[0] for x in self.old_reselling_list]
        if new[0] not in old_names:
            self.reselling_list.append(new)

    print(f"This is the OLD Reselling Items: {self.old_reselling_list}")
    print(f"This is the NEW Reselling Items: {self.new_reselling_list}")
    print(f"These are the Difference Reselling Items: {self.reselling_list}")

    if (self.reselling_scraped - reselling_count >= 1):

        num = self.reselling_scraped - reselling_count
        body = f"{num} New Items were found on {self.new_name} \n\nView the New Sale Items Here: http://www.saleoftheday.co.uk/shop/ \n\nItem List: \n\n"

        for item_info in self.reselling_list:
            info = f"Product: {item_info[0]} \nBuy Now: {item_info[3]} \nPrice: £{'%.2f' % item_info[1]} \nRRP: £{'%.2f' % item_info[2]} \nDiscount: {item_info[9]}% \nAvailable Sizes: {item_info[6]}\n\n"
            if item_info[1] > 0:
                body = body + info

        self.messageSubject = f"{num} New Items were found on {self.new_name}"
        sotd_close.sendMail([self.toAdd], self.messageSubject, body)
        print("###########################")
        print("SENT EMAIL")
        print("###########################")


    if ((((self.items_scraped - items_count >= 2) or (items_count - self.items_scraped >= 4)) and (items_count > 0) and (self.items_scraped > 0)) or (((self.hot_deal_scraped - hot_deal_count >= 1) or (hot_deal_count - self.hot_deal_scraped >= 1)) and (items_count > 0) and (self.items_scraped > 0))):
        time.sleep(5)
        try:
            requests.get(f'https://us-central1-indigo-pod-316.cloudfunctions.net/{store_url}',timeout=5)
        except:
            pass
