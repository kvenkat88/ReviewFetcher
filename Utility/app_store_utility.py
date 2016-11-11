import feedparser
import datetime
import re
from Utility import general_utility as gl
from Config import api_endpoints as api_end
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#######################################################################################################################################################################
#Reference URL to deal ncoding issues in windows - http://stackoverflow.com/questions/32382686/unicodeencodeerror-charmap-codec-cant-encode-character-u2010-character-m
#http://stackoverflow.com/questions/878972/windows-cmd-encoding-change-causes-python-crash
#http://blog.hoachuck.biz/blog/2013/04/19/pythonista-an-impressive-app-in-apple-app-store/
#https://www.mkyong.com/mongodb/mongodb-aggregate-and-group-example/
#######################################################################################################################################################################

def total_no_of_page_retriever(feed_main_url):
    feed_info_retrieve = feedparser.parse(feed_main_url)
    lastPage_identification =  feed_info_retrieve['feed']['links'][3]['href']
    PagesList = int(re.findall(r".*page=(\d*)/.*", lastPage_identification)[0])
    print("Theoritical number of pages: " + str(PagesList))
    maxPages = PagesList
    if PagesList<10:
        print("number of pages available for the condition(PagesList<10): " + str(maxPages))
        return maxPages
    elif PagesList>10:
        print("number of pages available for the condition(PagesList>10): " + str(maxPages))
        return maxPages
    else:
        maxPages = 10
        print("number of pages available for the condition(else part): " + str(maxPages))
        return maxPages

def page_review_comments_fetcher_whole_app_review(PageUrl):
    review_comments = []
    feed_entry= feedparser.parse(PageUrl)
    for a in feed_entry.entries:
            review_comments_dict = {}
            review_id_list = a.id
            review_id_split = review_id_list.split('/')

            if review_id_split[4] != "app":
                review_comments_dict['_id'] = review_id_split[9]
                review_comments_dict['review_entry_title'] = a.title
                review_comments_dict['updated_time'] = a.updated
                review_comments_dict['review_comment_added_to_db_date'] = datetime.datetime.utcnow().isoformat()[
                                                                          :-3] + "Z"
            else:
                # review_comments_dict['_id'] = None
                pass

            if 'im_rating' not in a:
                #review_comments_dict['review_rating'] = None
                pass
            else:
                review_comments_dict['review_rating'] = int(a.im_rating)

            if 'im_version' not in a:
                #review_comments_dict['review_app_version'] = None
                pass
            else:
                review_comments_dict['review_app_version'] = a.im_version

            if ('summary' not in a) or ("<table border" in a.summary ):
                #review_comments_dict['review_comments'] = None
                pass
            else:
                review_comments_dict['review_comments'] = a.summary

            review_comments.append(review_comments_dict)
    return review_comments

def page_review_comments_fetcher_particular_day_app_review(PageUrl):
    review_comments = []
    feed_entry= feedparser.parse(PageUrl)
    present_day_date_validate = gl.validate_datetime(feed_entry['feed']['updated'])
    current_date_time = gl.retrieve_today_date()
    if present_day_date_validate == True:
        for a in feed_entry.entries:
                review_comments_dict = {}
                if a.updated.split('T')[0] == current_date_time:
                    review_id_list = a.id
                    review_id_split = review_id_list.split('/')
                    if review_id_split[4] != "app":
                        review_comments_dict['_id'] = review_id_split[9]
                        review_comments_dict['review_entry_title'] = a.title
                        review_comments_dict['updated_time'] = a.updated
                        review_comments_dict['review_comment_added_to_db_date'] = datetime.datetime.utcnow().isoformat()[:-3] + "Z"
                    else:
                        # review_comments_dict['_id'] = None
                        pass

                    if 'im_rating' not in a:
                        #review_comments_dict['review_rating'] = None
                        pass
                    else:
                        review_comments_dict['review_rating'] = int(a.im_rating)

                    if 'im_version' not in a:
                        #review_comments_dict['review_app_version'] = None
                        pass
                    else:
                        review_comments_dict['review_app_version'] = a.im_version

                    if ('summary' not in a) or ("<table border" in a.summary ):
                        #review_comments_dict['review_comments'] = None
                        pass
                    else:
                        review_comments_dict['review_comments'] = a.summary

                    review_comments.append(review_comments_dict)
                else:
                    #print "Current Day App Review Comments are not available for parsing"
                    pass
        return review_comments

def page_info_parser_retrieve_whole_reviews_of_appID(feed_main_url):
    maxPages = total_no_of_page_retriever(feed_main_url)
    combined_review_coments_holder = []
    page = 1
    while page<maxPages+1:
        urlPos = re.sub("customerreviews","customerreviews/page="+str(page),feed_main_url)
        page_review_comment = page_review_comments_fetcher_whole_app_review(urlPos)
        print "#########################################################################################"
        print "Retrieving the Review comments information from the App Review Page No - %d and Page url- %s"%(page,urlPos)
        print "Reveiew Fetched for the Page No - %d are as follows " %(page)
        print page_review_comment
        combined_review_coments_holder.append(page_review_comment)
        print "#########################################################################################"
        page = page+1
    print
    print "Archeived Review Comments for the Application ID is as follows"
    return combined_review_coments_holder

def page_info_parser_retrieve_particular_day_reviews_of_appID(feed_main_url):
    maxPages = total_no_of_page_retriever(feed_main_url)
    combined_review_coments_holder = []
    page = 1
    while page<maxPages+1:
        urlPos = re.sub("customerreviews","customerreviews/page="+str(page),feed_main_url)
        page_review_comment = page_review_comments_fetcher_particular_day_app_review(urlPos)
        print "#########################################################################################"
        print "Retrieving the Review comments information from the App Review Page No - %d and Page url- %s"%(page,urlPos)
        print "Reveiew Fetched for the Page No - %d are as follows " %(page)

        if page_review_comment == []:
            print "No Comments are available"
            #print page_review_comment
        else:
            combined_review_coments_holder.append(page_review_comment)
            #print page_review_comment
            print "#########################################################################################"
        page = page+1
    print
    print "Archeived Review Comments for the Application ID is as follows"
    return combined_review_coments_holder

def retrive_entire_review_comments_for_appID(feed_main_url):
    review_comments = page_info_parser_retrieve_whole_reviews_of_appID(feed_main_url)
    return review_comments

def retrieve_daily_review_comments_for_appID(feed_main_url):
    review_comments = page_info_parser_retrieve_particular_day_reviews_of_appID(feed_main_url)
    return review_comments

def retrieve_xtv_whole_review_comments():
    feed_main_url = api_end.xtv_app_review_url_mostRecent()
    review_comments = page_info_parser_retrieve_whole_reviews_of_appID(feed_main_url)
    return review_comments

def retrieve_xtv_day_review_comments():
    feed_main_url = api_end.xtv_app_review_url_mostRecent()
    review_comments = page_info_parser_retrieve_particular_day_reviews_of_appID(feed_main_url)
    return review_comments

def retrieve_xtv_connect_whole_review_comments():
    feed_main_url = api_end.xfn_connect_app_review_url_mostRecent()
    review_comments = page_info_parser_retrieve_whole_reviews_of_appID(feed_main_url)
    return review_comments

def retrieve_xtv_connect_day_review_comments():
    feed_main_url = api_end.xfn_connect_app_review_url_mostRecent()
    review_comments = page_info_parser_retrieve_particular_day_reviews_of_appID(feed_main_url)
    return review_comments

def retrieve_xtv_x1_remote_whole_review_comments():
    feed_main_url = api_end.xtv_x1Remote_app_review_url_mostRecent()
    review_comments = page_info_parser_retrieve_whole_reviews_of_appID(feed_main_url)
    return review_comments

def retrieve_xtv_x1_remote_day_review_comments():
    feed_main_url = api_end.xtv_x1Remote_app_review_url_mostRecent()
    review_comments = page_info_parser_retrieve_particular_day_reviews_of_appID(feed_main_url)
    return review_comments

def retrieve_xtv_home_whole_review_comments():
    feed_main_url = api_end.xfn_home_app_review_url_mostRecent()
    review_comments = page_info_parser_retrieve_whole_reviews_of_appID(feed_main_url)
    return review_comments

def retrieve_xtv_home_day_review_comments():
    feed_main_url = api_end.xfn_home_app_review_url_mostRecent()
    review_comments = page_info_parser_retrieve_particular_day_reviews_of_appID(feed_main_url)
    return review_comments

def retrieve_xtv_remote_whole_review_comments():
    feed_main_url = api_end.xtv_Remote_app_review_url_mostRecent()
    review_comments = page_info_parser_retrieve_whole_reviews_of_appID(feed_main_url)
    return review_comments

def retrieve_xtv_remote_day_review_comments():
    feed_main_url = api_end.xtv_Remote_app_review_url_mostRecent()
    review_comments = page_info_parser_retrieve_particular_day_reviews_of_appID(feed_main_url)
    return review_comments


