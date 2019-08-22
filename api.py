from flask import Flask, jsonify, request
from flask_restful import Resource, Api

import requests
import concurrent.futures



#BASE_URL = WAS REMOVED TO HIDE THE IDENTITY OF THE HIRING ORGANISATION

app = Flask(__name__)
api = Api(app)



class Failure(Resource):
    def get(self):
        return {'error': 'Tags parameter is required'}, 400

class mAPI(Resource):

    def get(self,tags):
        #Variables
        tag = ""
        tagAr = []
        post = []
        postId = {}

        #Convert tags string into a list of strings
        for x in tags:
            if x == ',':
                tagAr.append(tag)
                tag = ""
            else:
                tag += x
        
        tagAr.append(tag)


        #Perform request for each tag in tagAr in parrallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
            res = list(pool.map(self.perform_request,tagAr))

        sortBy = request.args.get("sortBy")

        
        #Combine data from request, store in post
        for i in range(len(res)):
            for j in range(len(res[i]["posts"])):
                if res[i]["posts"][j]["id"] not in postId:
                    post.append(res[i]["posts"][j])
                    postId[res[i]["posts"][j]["id"]] = 1

        if sortBy == "id" or sortBy =="reads" or sortBy =="likes" or sortBy =="popularity":
            #Set Direction
            direction = request.args.get("direction")
            if direction == None:
                rev = True
            elif direction == "desc":
                rev = True
            elif direction == "asc":
                rev = False
            else:
                return {'error': 'sortBy parameter is invalid'}, 400
            #Sort Through post Array
            post = sorted(post, key = lambda i: i[sortBy],reverse = rev)

        elif sortBy!= None:
            return {'error': 'sortBy parameter is invalid'}, 400
        return {"posts": post}, 200

    def perform_request(self,tag):
        #Returns the json of the request
        return requests.get(BASE_URL + "?tag=" + tag).json()



api.add_resource(Failure,'/api/post')
api.add_resource(mAPI,'/api/post/<string:tags>')


if __name__ == '__main__':
    app.run(debug=True)