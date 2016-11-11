import pymongo
from pymongo.errors import ConnectionFailure
import sys
from Utility import app_store_utility as gl
import datetime
from Config import api_endpoints as api_end
from Utility import app_store_utility as app_utl

#http://blog.mycodesite.com/mongodb-basics-and-tips/
#http://codehandbook.org/pymongo-tutorial-crud-operation-mongodb/
#http://altons.github.io/python/2013/01/21/gentle-introduction-to-mongodb-using-pymongo/
#https://docs.mongodb.com/manual/reference/method/db.collection.insert/
#http://api.mongodb.com/python/current/faq.html

#http://salmanwahed.github.io/2015/05/01/flask-restful-mongodb-api/
#http://blog.luisrei.com/articles/flaskrest.html
#http://altons.github.io/python/2013/01/21/gentle-introduction-to-mongodb-using-pymongo/
#https://blog.openshift.com/rest-web-services-with-python-mongodb-and-spatial-data-in-the-cloud-part-2/
#http://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_RESTAPI_with_Flask.php
#http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
'''
def connect_db(mongo_instance):
    # Connection to Mongo DB
    conn = None
    try:
        conn=pymongo.MongoClient(mongo_instance)
        print "MongoDB Connected successfully!!!"
    except pymongo.errors.ConnectionFailure, e:
       print "Could not connect to MongoDB: %s" % e
       sys.exit(1)
    return conn

def create_or_use_db(mongo_instance,db_name,coll_name):
    try:
        conn = connect_db(mongo_instance)
        db_created = None
        col_name = None
        if conn:
            if db_name not in conn.database_names():
                print "Creating the new DB - %s for usage"%(db_name)
                create_db = conn[db_name]
                if create_db:
                    db_created = db_name
                    collection = create_db[str(create_db)]
                    if collection:
                        col_name = coll_name
                print db_created,col_name
                return db_created,col_name
            else:
                print "DB - %s is already available then use it"%(db_name)
                if coll_name in conn[db_name].collection_names(include_system_collections=False):
                    print "Collection - %s already available" %(coll_name)
                return db_name,coll_name
    except Exception as e:
        print "Exception Ocuured while performing the operations in MongoDB: %s" % e
        sys.exit(1)

'''

mongo_instance = "localhost:27017"
db_name = "app_store_holder"
xtv_coll_name = "xtv_record"
xtv_connect_coll_name = "xtv_connect_record"
xtv_x1_remote_coll_name = "xtv_x1_remote_record"
xtv_home_coll_name = "xtv_home_record"
xtv_remote_coll_name = "xtv_remote_record"

class MongoDBClient(object):
    def __init__(self):
        try:
            connection=pymongo.MongoClient(mongo_instance)
            print "MongoDB Connected successfully!!!"
            db = connection[db_name]
            self.xtv_record_collection = db[xtv_coll_name]
            self.xtv_connect_record_collection = db[xtv_connect_coll_name]
            self.xtv_x1_remote_record_collection = db[xtv_x1_remote_coll_name]
            self.xtv_home_record_collection = db[xtv_home_coll_name]
            self.xtv_remote_record_collection = db[xtv_remote_coll_name]

        except pymongo.errors.ConnectionFailure, e:
           print "Could not connect to MongoDB: %s" % e
           sys.exit(1)
        except Exception as e:
            print "Exception Ocuured while performing the operations in MongoDB: %s" % e
            sys.exit(1)

    def insert_record_xtv(self,item):
        self.xtv_record_collection.insert(item)

    def insert_record_xtv_connect(self,item):
        self.xtv_connect_record_collection.insert(item)

    def insert_record_xtv_x1_remote(self,item):
        self.xtv_x1_remote_record_collection.insert(item)

    def insert_record_xtv_home(self,item):
        self.xtv_home_record_collection.insert(item)

    def insert_record_xtv_remote(self, item):
        self.xtv_remote_record_collection.insert(item)

    # Duplicate Entry finder
    def find_duplicate_entry_item(self, revie_comment_id):
        pipe = [
            {'$group': {
                '_id': {'_id': '$%s' % (revie_comment_id)},
                'uniqueIds': {'$addToSet': "$_id"},
                'count': {'$sum': 1}
            }},
            {'$match': {'count': {'$gt': 1}}}
        ]
        s = self.xtv_record_collection.aggregate(pipeline=pipe)
        for a in s:
            if revie_comment_id not in a['uniqueIds']:
                print "Review_Comment_Id - %s is not available.Hence adding this to Database Collections" % (
                revie_comment_id)
                return False
            else:
                print "Review_Comment_Id - %s is already available in the Database collection" % (revie_comment_id)
                return True

    def find_duplicate_entry_item_xtv_connect(self, revie_comment_id):
        pipe = [
            {'$group': {
                '_id': {'_id': '$%s' % (revie_comment_id)},
                'uniqueIds': {'$addToSet': "$_id"},
                'count': {'$sum': 1}
            }},
            {'$match': {'count': {'$gt': 1}}}
        ]
        s = self.xtv_connect_record_collection.aggregate(pipeline=pipe)
        for a in s:
            if revie_comment_id not in a['uniqueIds']:
                print "Review_Comment_Id - %s is not available.Hence adding this to Database Collections" % (
                revie_comment_id)
                return False
            else:
                print "Review_Comment_Id - %s is already available in the Database collection" % (revie_comment_id)
                return True

    def find_duplicate_entry_item_xtv_x1_remote(self, revie_comment_id):
        pipe = [
            {'$group': {
                '_id': {'_id': '$%s' % (revie_comment_id)},
                'uniqueIds': {'$addToSet': "$_id"},
                'count': {'$sum': 1}
            }},
            {'$match': {'count': {'$gt': 1}}}
        ]
        s = self.xtv_x1_remote_record_collection.aggregate(pipeline=pipe)
        for a in s:
            if revie_comment_id not in a['uniqueIds']:
                print "Review_Comment_Id - %s is not available.Hence adding this to Database Collections" % (
                revie_comment_id)
                return False
            else:
                print "Review_Comment_Id - %s is already available in the Database collection" % (revie_comment_id)
                return True

    def find_duplicate_entry_item_xtv_home(self, revie_comment_id):
        pipe = [
            {'$group': {
                '_id': {'_id': '$%s' % (revie_comment_id)},
                'uniqueIds': {'$addToSet': "$_id"},
                'count': {'$sum': 1}
            }},
            {'$match': {'count': {'$gt': 1}}}
        ]
        s = self.xtv_home_record_collection.aggregate(pipeline=pipe)
        for a in s:
            if revie_comment_id not in a['uniqueIds']:
                print "Review_Comment_Id - %s is not available.Hence adding this to Database Collections" % (
                revie_comment_id)
                return False
            else:
                print "Review_Comment_Id - %s is already available in the Database collection" % (revie_comment_id)
                return True

    def find_duplicate_entry_item_xtv_remote(self, revie_comment_id):
        pipe = [
            {'$group': {
                '_id': {'_id': '$%s' % (revie_comment_id)},
                'uniqueIds': {'$addToSet': "$_id"},
                'count': {'$sum': 1}
            }},
            {'$match': {'count': {'$gt': 1}}}
        ]
        s = self.xtv_remote_record_collection.aggregate(pipeline=pipe)
        for a in s:
            if revie_comment_id not in a['uniqueIds']:
                print "Review_Comment_Id - %s is not available.Hence adding this to Database Collections" % (
                revie_comment_id)
                return False
            else:
                print "Review_Comment_Id - %s is already available in the Database collection" % (revie_comment_id)
                return True


    def xtv_insert_record_without_null_values(self,review_comments_repo_list):
        for review_comment_list in review_comments_repo_list:
            for item in review_comment_list:
                if bool(item) == False:
                    pass
                else:
                    #print item['_id']
                    retrieved_id = self.find_duplicate_entry_item(item['_id'])
                    if retrieved_id==False or retrieved_id == None:
                        self.insert_record_xtv(item)

    def xtv_connect_insert_record_without_null_values(self,review_comments_repo_list):
        for review_comment_list in review_comments_repo_list:
            for item in review_comment_list:
                if bool(item) == False:
                    pass
                else:
                    #print item['_id']
                    retrieved_id = self.find_duplicate_entry_item_xtv_connect(item['_id'])
                    if retrieved_id==False or retrieved_id == None:
                        self.insert_record_xtv_connect(item)

    def xtv_x1_remote_insert_record_without_null_values(self,review_comments_repo_list):
        for review_comment_list in review_comments_repo_list:
            for item in review_comment_list:
                if bool(item) == False:
                    pass
                else:
                    #print item['_id']
                    retrieved_id = self.find_duplicate_entry_item_xtv_x1_remote(item['_id'])
                    if retrieved_id==False or retrieved_id == None:
                        self.insert_record_xtv_x1_remote(item)

    def xtv_home_insert_record_without_null_values(self,review_comments_repo_list):
        for review_comment_list in review_comments_repo_list:
            for item in review_comment_list:
                if bool(item) == False:
                    pass
                else:
                    #print item['_id']
                    retrieved_id = self.find_duplicate_entry_item_xtv_home(item['_id'])
                    if retrieved_id==False or retrieved_id == None:
                        self.insert_record_xtv_home(item)

    def xtv_remote_insert_record_without_null_values(self,review_comments_repo_list):
        for review_comment_list in review_comments_repo_list:
            for item in review_comment_list:
                if bool(item) == False:
                    pass
                else:
                    #print item['_id']
                    retrieved_id = self.find_duplicate_entry_item_xtv_remote(item['_id'])
                    if retrieved_id==False or retrieved_id == None:
                        self.insert_record_xtv_remote(item)

    def retrieve_xtv_records(self):
        bulk_record = self.xtv_record_collection.find()
        output = []
        for s in bulk_record:
            output.append(s)
        return output

    def retrieve_xtv_connect_records(self):
        bulk_record = self.xtv_connect_record_collection.find()
        output = []
        for s in bulk_record:
            output.append(s)
        return output

    def retrieve_xtv_x1_remote_records(self):
        bulk_record = self.xtv_x1_remote_record_collection.find()
        output = []
        for s in bulk_record:
            output.append(s)
        return output

    def retrieve_xtv_home_records(self):
        bulk_record = self.xtv_home_record_collection.find()
        output = []
        for s in bulk_record:
            output.append(s)
        return output

    def retrieve_xtv_remote_records(self):
        bulk_record = self.xtv_remote_record_collection.find()
        output = []
        for s in bulk_record:
            output.append(s)
        return output

    def retrieve_xtv_records_based_on_versions(self,range1,range2):
        bulk_record = self.xtv_record_collection.find({'review_app_version': {'$gt':range1, '$lt': range2}})
        output = []
        for s in bulk_record:
            output.append(s)
        return output

    def retrieve_xtv_records_based_on_ratings(self,range1,range2):
        bulk_record = self.xtv_record_collection.find({'review_rating': {'$gte':range1, '$lt': range2}})
        output = []
        for s in bulk_record:
            output.append(s)
        return output

    def retrieve_xtv_records_based_on_current_date(self):
        date2 = datetime.datetime.strftime(datetime.datetime.now, '%Y-%m-%d')
        bulk_record = self.xtv_record_collection.find({'updated_time': date2})
        output = []
        for s in bulk_record:
            output.append(s)
        return output

    def retrieve_xtv_records_based_on_bulk_date(self,range1,range2):
        #date2 = datetime.datetime.strftime(datetime.datetime.now, '%Y-%m-%d')
        bulk_record = self.xtv_record_collection.find(
            {'updated_time': {'$gte': "%s" % (range1), '$lt': "%s" % (range2)}})
        output = []
        for s in bulk_record:
            output.append(s)
        return output

    def retrieve_xtv_records_all_ratings_single_view(self):
        bulk_record = self.xtv_record_collection.distinct('review_rating')
        print bulk_record
        return bulk_record

    def retrieve_xtv_records_all_versions_single_view(self):
        bulk_record = self.xtv_record_collection.distinct('review_app_version')
        print bulk_record
        return bulk_record

    def retrieve_xtv_connect_records_all_ratings_single_view(self):
        bulk_record = self.xtv_connect_record_collection.distinct('review_rating')
        print bulk_record
        return bulk_record

    def retrieve_xtv_connect_records_all_versions_single_view(self):
        bulk_record = self.xtv_connect_record_collection.distinct('review_app_version')
        print bulk_record
        return bulk_record

    def retrieve_xtv_x1_remote_records_all_ratings_single_view(self):
        bulk_record = self.xtv_x1_remote_record_collection.distinct('review_rating')
        print bulk_record
        return bulk_record

    def retrieve_xtv_x1_remote_records_all_versions_single_view(self):
        bulk_record = self.xtv_x1_remote_record_collection.distinct('review_app_version')
        print bulk_record
        return bulk_record

    def retrieve_xtv_home_records_all_ratings_single_view(self):
        bulk_record = self.xtv_home_record_collection.distinct('review_rating')
        print bulk_record
        return bulk_record

    def retrieve_xtv_home_records_all_versions_single_view(self):
        bulk_record = self.xtv_home_record_collection.distinct('review_app_version')
        print bulk_record
        return bulk_record

    def retrieve_xtv_remote_records_all_ratings_single_view(self):
        bulk_record = self.xtv_remote_record_collection.distinct('review_rating')
        print bulk_record
        return bulk_record

    def retrieve_xtv_remote_records_all_versions_single_view(self):
        bulk_record = self.xtv_remote_record_collection.distinct('review_app_version')
        print bulk_record
        return bulk_record

    def retrieve_xtv_retrieve_single_item(self,key_name,value):
        bulk_record = self.xtv_record_collection.find({str(key_name): value})
        output = []
        for s in bulk_record:
            output.append(s)
        return output

    def retrieve_xtv_connect_retrieve_single_item(self,key_name,value):
        bulk_record = self.xtv_connect_record_collection.find({str(key_name): value})
        output = []
        for s in bulk_record:
            output.append(s)
        return output

    def retrieve_xtv_x1_remote_retrieve_single_item(self,key_name,value):
        bulk_record = self.xtv_x1_remote_record_collection.find({str(key_name): value})
        output = []
        for s in bulk_record:
            output.append(s)
        return output

    def retrieve_xtv_home_retrieve_single_item(self,key_name,value):
        bulk_record = self.xtv_home_record_collection.find({str(key_name): value})
        output = []
        for s in bulk_record:
            output.append(s)
        return output

    def retrieve_xtv_remote_retrieve_single_item(self,key_name,value):
        bulk_record = self.xtv_remote_record_collection.find({str(key_name): value})
        output = []
        for s in bulk_record:
            output.append(s)
        return output

    #Methods for scheduler.
    def retrieve_xtv_whole_review_comments(self):
        feed_main_url = api_end.xtv_app_review_url_mostRecent()
        review_comments = app_utl.page_info_parser_retrieve_whole_reviews_of_appID(feed_main_url)
        self.xtv_insert_record_without_null_values(review_comments)

    def retrieve_xtv_day_review_comments(self):
        feed_main_url = api_end.xtv_app_review_url_mostRecent()
        review_comments = app_utl.page_info_parser_retrieve_particular_day_reviews_of_appID(feed_main_url)
        self.xtv_insert_record_without_null_values(review_comments)

    def retrieve_xtv_connect_whole_review_comments(self):
        feed_main_url = api_end.xfn_connect_app_review_url_mostRecent()
        review_comments = app_utl.page_info_parser_retrieve_whole_reviews_of_appID(feed_main_url)
        self.xtv_connect_insert_record_without_null_values(review_comments)

    def retrieve_xtv_connect_day_review_comments(self):
        feed_main_url = api_end.xfn_connect_app_review_url_mostRecent()
        review_comments = app_utl.page_info_parser_retrieve_particular_day_reviews_of_appID(feed_main_url)
        self.xtv_connect_insert_record_without_null_values(review_comments)

    def retrieve_xtv_x1_remote_whole_review_comments(self):
        feed_main_url = api_end.xtv_x1Remote_app_review_url_mostRecent()
        review_comments = app_utl.page_info_parser_retrieve_whole_reviews_of_appID(feed_main_url)
        self.xtv_x1_remote_insert_record_without_null_values(review_comments)

    def retrieve_xtv_x1_remote_day_review_comments(self):
        feed_main_url = api_end.xtv_x1Remote_app_review_url_mostRecent()
        review_comments = app_utl.page_info_parser_retrieve_particular_day_reviews_of_appID(feed_main_url)
        self.xtv_x1_remote_insert_record_without_null_values(review_comments)

    def retrieve_xtv_home_whole_review_comments(self):
        feed_main_url = api_end.xfn_home_app_review_url_mostRecent()
        review_comments = app_utl.page_info_parser_retrieve_whole_reviews_of_appID(feed_main_url)
        self.xtv_home_insert_record_without_null_values(review_comments)

    def retrieve_xtv_home_day_review_comments(self):
        feed_main_url = api_end.xfn_home_app_review_url_mostRecent()
        review_comments = app_utl.page_info_parser_retrieve_particular_day_reviews_of_appID(feed_main_url)
        self.xtv_home_insert_record_without_null_values(review_comments)

    def retrieve_xtv_remote_whole_review_comments(self):
        feed_main_url = api_end.xtv_Remote_app_review_url_mostRecent()
        review_comments = app_utl.page_info_parser_retrieve_whole_reviews_of_appID(feed_main_url)
        self.xtv_remote_insert_record_without_null_values(review_comments)

    def retrieve_xtv_remote_day_review_comments(self):
        feed_main_url = api_end.xtv_Remote_app_review_url_mostRecent()
        review_comments = app_utl.page_info_parser_retrieve_particular_day_reviews_of_appID(feed_main_url)
        self.xtv_remote_insert_record_without_null_values(review_comments)


#fd = gl.retrieve_xtv_remote_whole_review_comments()
#df = MongoDBClient()
#df.retrieve_xtv_remote_whole_review_comments()
