#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup as bs

class Droppett():
  def __init__(self, username = None, password = None):
    if username is None:
      raise ValueError("Username not provided.")
    elif password is None:
      raise ValueError("Password not provided.")
    else:
      self.username = username
      self.password = password

  def _scrapeWeb(self):
    url = "https://droppett.com/?page_id=116"

    payload = f"myUsername={self.username}&myPassword={self.password}&submit.x=0&submit.y=0"
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0',
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return(response.text)

  def _getDroppettInfo(self):
    web_scrape = self._scrapeWeb()
    soup = bs(web_scrape, 'html.parser')
    cash = soup.find("div", class_="stats-stat balance").find("div", class_="value")
    cash = cash.text.strip().replace("$", "")
    cans = soup.find("div", class_="stats-stat containers").find("div", class_="value")
    cans = cans.text.strip()

    return cash, cans
