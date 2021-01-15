import nltk
import re

class AdFromLink:

    def init(self):
        with open("blocklist.txt") as f:
            advertisement_agencies = f.readlines()
        self.advertisement_agencies = [x.strip() for x in advertisement_agencies]

    def get_new_block_list(self, found_agencies):
        matrix = []
        k = 0
        for ad in self.advertisement_agencies:
            seen = False
            for ag in found_agencies:
                k += 1
                if ag[0] == ad:
                    seen = True
                    matrix.append(ag[1])
            if seen == False:
               matrix.append(0)
        return matrix


    def get_ads_from_link(self, link):
        with open("documents/" + link, 'r') as file:
            html_text = file.read()
        found_agencies = []
        for website in self.advertisement_agencies:
            if len(re.findall(website, html_text)) > 0:
                found_agencies.append([website,len(re.findall(website, html_text))])
        return found_agencies