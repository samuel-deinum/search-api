This programs uses flask flask_restful, requests, and futures.  These libraries need
to be installed for it to work.  Run the api.py file to create the RESTful App. 



Testing:

If no tags are present, an error message will appear
    http://127.0.0.1:5000/api/post
If tags are not found in data, the post array will be empty
    http://127.0.0.1:5000/api/post/testdummy
If one tag is present, all post with that tag will appear
    http://127.0.0.1:5000/api/post/tech
If two or more tags are present, any post with these tags will appear
    http://127.0.0.1:5000/api/post/tech,health
If tags are seperated by anything but a comma or question mark, the post array will be empty
    http://127.0.0.1:5000/api/post/tech-health, http://127.0.0.1:5000/api/post/tech.health
If tags are seperated by a question mark, results from the first tag will appear and no parameters
    will be activated
    http://127.0.0.1:5000/api/post/tech?health
    http://127.0.0.1:5000/api/post/tech?health?sortBy=popularity
If the sortBy or direction parameter name is mispelt, they will not be activated.  Data is 
    rendered without sorting if sortBy is mispelt.  Data is rendered in descending order if 
    direction is mispelt
    http://127.0.0.1:5000/api/post/tech?sorBy=popularity
    http://127.0.0.1:5000/api/post/tech?sortB=popularity&direction=desc
    http://127.0.0.1:5000/api/post/tech?sortBy=popularity&irection=desc
    http://127.0.0.1:5000/api/post/tech?sorty=popularity&irection=desc
If the sortBy parameter is not "id", "reads", "likes", or "popularity", an error message will appear
    http://127.0.0.1:5000/api/post/tech?sortBy=test
If direction is not specified, the default is descending order
    http://127.0.0.1:5000/api/post/tech?sortBy=popularity
If direction parameter is not "asc" or "desc", an error message will appear
    http://127.0.0.1:5000/api/post/tech?sortBy=popularity&direction=acs


