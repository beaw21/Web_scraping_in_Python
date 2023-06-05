import session_sonar
import pandas as pd
import requests

auth = session_sonar.session(session_sonar.url_api, session_sonar.params)


# def Function(api, fromPage=1, toPage=5, **page):
#     data = page.get('page', [])
#     for i in range(fromPage, toPage + 1, 1):
#         call = requests.session(api + i)
#         data += call.json()
#         object_json = pd.json_normalize(data)
#         print("loading page" + str(i))
#     if len(object_json["issues"]) < session_sonar.params["ps"]:
#         return "empty list data"
#
#
# obj_page = Function(auth, fromPage=1, toPage=40)
# df = pd.DataFrame(obj_page)

