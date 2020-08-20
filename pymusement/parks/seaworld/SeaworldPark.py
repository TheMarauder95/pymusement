#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup as bs
from pymusement.park import Park
from pymusement.ride import Ride
from pymusement.show import Show

PARK_URL_FORMAT = 'https://{0}.com/{1}/ride-wait-times/'
#SHOW_URL_FORMAT = 'https://seas.te2.biz/v1/rest/venue/{0}/shows/{1}'

class SeaworldPark(Park):
        
    def __init__(self):
        super(SeaworldPark, self).__init__()
        self._park_url = PARK_URL_FORMAT.format(self.getId(), self.getCity())


    def _buildPark(self):
        parsed_page = self._get_page(self._park_url)
        for poi in parsed_page:
            self._build_ride(poi)

       # parsed_page = self._get_page(self._show_url)
        #for poi in parsed_page:
      #      self._build_show(poi)

    def _get_page(self, url):
        # Make page request, return Beautiful Soup request
        response = requests.get(url) 
        soup = bs(response.text,'html.parser')
        table = soup.find_all('div',{'class':'row ride-times-wrapper'})
        return table

    def _build_ride(self, poi):
        # Create dictionary with attraction information
        ride = Ride()
        
        name = poi.find('div',{'class':'col-xs-6 col-md-6 ride-times-title'}).text
        time = poi.find('div',{'col-xs-4 col-md-4 ride-times-hours'})
        if time == None:
            time = 'Closed'
        else: time = time.text
        
        
        ride.setName(name)
        if time == 'Closed':
            ride.setTime(-1)
            ride.setClosed()
        else: 
            time = time.split()[0]
            ride.setTime(time)
            ride.setOpen()
        
        self.addRide(ride)

  #  def _build_show(self, row):
      #  result = Show()

  #      self.addShow(result)
