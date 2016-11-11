import json
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def signal_json_processor():
        """
        Method to load the Info.json file and parsing
        :param  data : NA
        :return: Returns a JSON file for parsing.
        """
        configPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Config'))
        with open(configPath + '/Info.json') as data_file:
                data = json.load(data_file)
        return data

def app_review_url(app_id,sort_by):
    """
            Method to create the app store url for different xfinity app available in App Store.
            :param  data : App ID from App Store,sortBy argument data (mostRecent/xml,mostCritical/xml,etc.)
            :return: Return App Review URL
    """
    feed_url = 'https://itunes.apple.com/us/rss/customerreviews/id=%s/sortBy=%s?l=en'%(app_id,sort_by)
    return feed_url

def xtv_go_app_review_url_mostRecent():
    json_data = signal_json_processor()
    feed_review_url = app_review_url(json_data['AppStore_Application_ID']['xfinity_tv_go'],"mostRecent/xml")
    print feed_review_url
    return feed_review_url

def xfn_connect_app_review_url_mostRecent():
    json_data = signal_json_processor()
    feed_review_url = app_review_url(json_data['AppStore_Application_ID']['xfinity_connect'],"mostRecent/xml")
    return feed_review_url

def xtv_app_review_url_mostRecent():
    json_data = signal_json_processor()
    feed_review_url = app_review_url(json_data['AppStore_Application_ID']['xfinity_tv'],"mostRecent/xml")
    return feed_review_url

def xtv_x1Remote_app_review_url_mostRecent():
    json_data = signal_json_processor()
    feed_review_url = app_review_url(json_data['AppStore_Application_ID']['xfinity_tv_x1_remote'],"mostRecent/xml")
    return feed_review_url

def xfn_home_app_review_url_mostRecent():
    json_data = signal_json_processor()
    feed_review_url = app_review_url(json_data['AppStore_Application_ID']['xfinity_home'],"mostRecent/xml")
    return feed_review_url

def xtv_Remote_app_review_url_mostRecent():
    json_data = signal_json_processor()
    feed_review_url = app_review_url(json_data['AppStore_Application_ID']['xfinity_tv_remote'],"mostRecent/xml")
    return feed_review_url

def xtv_go_app_review_url_mostCritical():
    json_data = signal_json_processor()
    feed_review_url = app_review_url(json_data['AppStore_Application_ID']['xfinity_tv_go'],"mostCritical/xml")
    return feed_review_url

def xfn_connect_app_review_url_mostCritical():
    json_data = signal_json_processor()
    feed_review_url = app_review_url(json_data['AppStore_Application_ID']['xfinity_connect'],"mostCritical/xml")
    return feed_review_url

def xtv_app_review_url_mostCritical():
    json_data = signal_json_processor()
    feed_review_url = app_review_url(json_data['AppStore_Application_ID']['xfinity_tv'],"mostCritical/xml")
    return feed_review_url

def xtv_x1Remote_app_review_url_mostCritical():
    json_data = signal_json_processor()
    feed_review_url = app_review_url(json_data['AppStore_Application_ID']['xfinity_tv_x1_remote'],"mostCritical/xml")
    return feed_review_url

def xtv_Remote_app_review_url_mostCritical():
    json_data = signal_json_processor()
    feed_review_url = app_review_url(json_data['AppStore_Application_ID']['xfinity_tv_remote'],"mostCritical/xml")
    return feed_review_url

def xfn_home_app_review_url_mostCritical():
    json_data = signal_json_processor()
    feed_review_url = app_review_url(json_data['AppStore_Application_ID']['xfinity_home'],"mostCritical/xml")
    return feed_review_url

