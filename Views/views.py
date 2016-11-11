from flask import Flask, jsonify, url_for, redirect, request,abort,Blueprint,render_template
from models.db_models import MongoDBClient
import json
mongo = MongoDBClient()

app_store = Blueprint('app_store', __name__)

@app_store.route('/')
@app_store.route('/index')
def home():
    return render_template('index1.html')

@app_store.route('/sub')
def home1():
    return render_template('subPage.html')

@app_store.route('/api/get_reviews', methods=['GET'])
def get_go_bulk_records():
    """
           Method to retrieve the whole set of reviews available in the database based upon the app_name.
           :param data: app_name should be used while calling the url from web/application developed
           :return Return the set of review records
           url_usage : http://127.0.0.1:5000/api/get_reviews?app_name=<app_name>
    """
    if request.method == "GET":
        if 'app_name' in request.args:
            if request.args['app_name'] == "xtv":
                output = mongo.retrieve_xtv_records()
                return jsonify({'result': output})

            elif request.args['app_name'] == "xfn_connect":
                output = mongo.retrieve_xtv_connect_records()
                return jsonify({'result': output})

            elif request.args['app_name'] == "xfn_x1_remote":
                output = mongo.retrieve_xtv_x1_remote_records()
                return jsonify({'result': output})

            elif request.args['app_name'] == "xfn_home":
                output = mongo.retrieve_xtv_home_records()
                return jsonify({'result': output})

            elif request.args['app_name'] == "xfn_remote":
                output = mongo.retrieve_xtv_remote_records()
                return jsonify({'result': output})

            else:
                abort(404)
        else:
            abort(404)
    else:
        abort(404)

@app_store.route('/api/app_versions_view', methods=['GET'])
def get_records_by_versions():
    """
               Method to retrieve the whole set of reviews available in the database based upon the versions range
               :param data: app_name and version range should be used while calling the url from web/application developed
               :return Return the set of review records for the version ranges
               url_usage : http://127.0.0.1:5000/api/app_versions_view?app_name=<app_name>&range1="3.8.0"&range2="3.9.1"
    """
    if request.method == "GET":
        #print request.args.getlist('app_name','range1')
        if 'app_name' in request.args:
            if request.args['app_name'] == "xtv" and request.args['range1']!=None and request.args['range2']!=None :
                output = mongo.retrieve_xtv_records_based_on_versions(str(request.args['range1']),str(request.args['range2']))
                return jsonify({'result': output})
            elif request.args['app_name'] == "xfn_connect" and request.args['range1']!=None and request.args['range2']!=None :
                output = mongo.retrieve_xtv_connect_records_based_on_versions(str(request.args['range1']),str(request.args['range2']))
                return jsonify({'result': output})
            elif request.args['app_name'] == "xfn_x1_remote" and request.args['range1']!=None and request.args['range2']!=None :
                output = mongo.retrieve_xtv_x1_remote_records_based_on_versions(str(request.args['range1']),str(request.args['range2']))
                return jsonify({'result': output})
            elif request.args['app_name'] == "xfn_home" and request.args['range1']!=None and request.args['range2']!=None :
                output = mongo.retrieve_xtv_home_records_based_on_versions(str(request.args['range1']),str(request.args['range2']))
                return jsonify({'result': output})
            elif request.args['app_name'] == "xfn_remote" and request.args['range1']!=None and request.args['range2']!=None :
                output = mongo.retrieve_xtv_remote_records_based_on_versions(str(request.args['range1']),str(request.args['range2']))
                return jsonify({'result': output})
            else:
                abort(404)
        else:
            abort(404)
    else:
        abort(404)

@app_store.route('/api/review_ratings_view', methods=['GET'])
def get_records_by_ratings():
    """
                   Method to retrieve the whole set of reviews available in the database based upon the ratings range
                   :param data: app_name and ratings range should be used while calling the url from web/application developed
                   :return Return the set of review records for the ratings ranges
                   url_usage : http://127.0.0.1:5000/api/review_ratings_view?app_name=<app_name>&range1="3.8.0"&range2="3.9.1"
    """
    if request.method == "GET":
        #print request.args.getlist('app_name','range1')

        if 'app_name' in request.args:
            if request.args['app_name'] == "xtv" and request.args['range1']!=None and request.args['range2']!=None :
                output = mongo.retrieve_xtv_records_based_on_ratings(int(request.args['range1']),int(request.args['range2']))
                return jsonify({'result': output})

            elif request.args['app_name'] == "xfn_connect" and request.args['range1']!=None and request.args['range2']!=None :
                output = mongo.retrieve_xtv_connect_records_based_on_ratings(int(request.args['range1']),int(request.args['range2']))
                return jsonify({'result': output})

            elif request.args['app_name'] == "xfn_x1_remote" and request.args['range1']!=None and request.args['range2']!=None :
                output = mongo.retrieve_xtv_x1_remote_records_based_on_ratings(int(request.args['range1']),int(request.args['range2']))
                return jsonify({'result': output})

            elif request.args['app_name'] == "xfn_home" and request.args['range1']!=None and request.args['range2']!=None :
                output = mongo.retrieve_xtv_home_records_based_on_ratings(int(request.args['range1']),int(request.args['range2']))
                return jsonify({'result': output})

            elif request.args['app_name'] == "xfn_remote" and request.args['range1']!=None and request.args['range2']!=None :
                output = mongo.retrieve_xtv_remote_records_based_on_ratings(int(request.args['range1']),int(request.args['range2']))
                return jsonify({'result': output})

            else:
                abort(404)
        else:
            abort(404)
    else:
        abort(404)

@app_store.route('/api/single_ratings_view', methods=['GET'])
def get_records_for_particular_ratings():
    """
               Method to retrieve the whole set of reviews available in the database based upon the ratings range
               :param data: app_name and ratings should be used while calling the url from web/application developed
               :return Return the set of review records for the ratings
               url_usage : http://127.0.0.1:5000/api/single_ratings_view?app_name=<app_name>&rating=5
    """
    if request.method == "GET":
        #print request.args.getlist('app_name','range1')
        if 'app_name' in request.args:
            if request.args['app_name'] == "xtv" and request.args['rating']!=None:
                output = mongo.retrieve_xtv_retrieve_single_item('review_rating',int(request.args['rating']))
                return jsonify({'result': output})
            elif request.args['app_name'] == "xfn_connect" and request.args['rating']!=None:
                output = mongo.retrieve_xtv_connect_retrieve_single_item('review_rating',int(request.args['rating']))
                return jsonify({'result': output})
            elif request.args['app_name'] == "xfn_x1_remote" and request.args['rating'] != None:
                output = mongo.retrieve_xtv_x1_remote_retrieve_single_item('review_rating',
                                                                                 int(request.args['rating']))
                return jsonify({'result': output})

            elif request.args['app_name'] == "xfn_home" and request.args['rating'] != None:
                output = mongo.retrieve_xtv_home_retrieve_single_item('review_rating',
                                                                                 int(request.args['rating']))
                return jsonify({'result': output})

            elif request.args['app_name'] == "xfn_remote" and request.args['rating'] != None:
                output = mongo.retrieve_xtv_remote_retrieve_single_item('review_rating',
                                                                                 int(request.args['rating']))
                return jsonify({'result': output})

            else:
                abort(404)
        else:
            abort(404)
    else:
        abort(404)

@app_store.route('/api/single_versions_view', methods=['GET'])
def get_records_for_particular_version():
    """
               Method to retrieve the whole set of reviews available in the database based upon the versions range
               :param data: app_name and version range should be used while calling the url from web/application developed
               :return Return the set of review records for the version ranges
               url_usage : http://127.0.0.1:5000/api/single_versions_view?app_name=<app_name>&version="3.8.0"
    """
    if request.method == "GET":
        #print request.args.getlist('app_name','range1')
        if 'app_name' in request.args:
            if request.args['app_name'] == "xtv" and request.args['version']!=None:
                output = mongo.retrieve_xtv_retrieve_single_item('review_app_version',str(request.args['version']))
                return jsonify({'result': output})

            elif request.args['app_name'] == "xfn_connect" and request.args['version']!=None:
                output = mongo.retrieve_xtv_connect_retrieve_single_item('review_app_version',str(request.args['version']))
                return jsonify({'result': output})

            elif request.args['app_name'] == "xfn_x1_remote" and request.args['version'] != None:
                output = mongo.retrieve_xtv_x1_remote_retrieve_single_item('review_app_version',
                                                                                 str(request.args['version']))
                return jsonify({'result': output})

            elif request.args['app_name'] == "xfn_home" and request.args['version'] != None:
                output = mongo.retrieve_xtv_home_retrieve_single_item('review_app_version',
                                                                                 str(request.args['version']))
                return jsonify({'result': output})

            elif request.args['app_name'] == "xfn_remote" and request.args['version'] != None:
                output = mongo.retrieve_xtv_remote_retrieve_single_item('review_app_version',
                                                                                 str(request.args['version']))
                return jsonify({'result': output})

            else:
                abort(404)
        else:
            abort(404)
    else:
        abort(404)


@app_store.route('/api/all_ratings', methods=['GET'])
def get_all_ratings():
        """
                   Method to retrieve the whole set of reviews available in the database based upon the versions range
                   :param data: app_name and version range should be used while calling the url from web/application developed
                   :return Return the set of review records for the version ranges
                   url_usage : http://127.0.0.1:5000/api/ratings_list?app_name=<app_name>
        """
        if request.method == "GET":
            if 'app_name' in request.args:
                if request.args['app_name'] == "xtv":
                    output = mongo.retrieve_xtv_records_all_ratings_single_view()
                    return jsonify({'result': sorted(output)})

                elif request.args['app_name'] == "xfn_connect":
                    output = mongo.retrieve_xtv_connect_records_all_ratings_single_view()
                    return jsonify({'result': sorted(output)})

                elif request.args['app_name'] == "xfn_x1_remote":
                    output = mongo.retrieve_xtv_x1_remote_records_all_ratings_single_view()
                    return jsonify({'result': sorted(output)})

                elif request.args['app_name'] == "xfn_home":
                    output = mongo.retrieve_xtv_home_records_all_ratings_single_view()
                    return jsonify({'result': sorted(output)})

                elif request.args['app_name'] == "xfn_remote":
                    output = mongo.retrieve_xtv_remote_records_all_ratings_single_view()
                    return jsonify({'result': sorted(output)})

                else:
                    abort(404)
            else:
                abort(404)
        else:
            abort(404)

