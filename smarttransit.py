# import requests
# url="http://smarttransit.cewit.stonybrook.edu/smarttransit"
# post_url=url+"/user_call/getServiceLevelAndNote.php"
#
# #
# # rl: "/user_call/getRoutesByServiceLevel.php",
# #         type: 'POST',
# #         data: 'serviceLevelID=' + smart.servicelevel,
# s = requests.Session()
# r=s.head(url)
# print r.text
# d={'routeID':'Hospital'}
# r=s.post(
#     url=url+'/user_call/getRouteDescriptionByRoute.php',
#     data=d)
# print r.text


from requests import Session

session = Session()

# HEAD requests ask for *just* the headers, which is all you need to grab the
# session cookie
session.head('http://sportsbeta.ladbrokes.com/football')

response = session.post(
    url='http://sportsbeta.ladbrokes.com/view/EventDetailPageComponentController',
    data={
        'N': '4294966750',
        'form-trigger': 'moreId',
        'moreId': '156#327',
        'pageType': 'EventClass'
    },
    headers={
        'Referer': 'http://sportsbeta.ladbrokes.com/football'
    }
)

print response.text