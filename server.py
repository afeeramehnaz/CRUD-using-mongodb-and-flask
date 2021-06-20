from flask import Flask,Response, request
import pymongo
import json
from bson.objectid import ObjectId
app=Flask(__name__)

try:
   mongo=pymongo.MongoClient(
       host="localhost",
       port=27017,
       serverSelectionTimeoutMS = 1000

   )
   db=mongo.company
   mongo.server_info()

except:
   print("ERROR -cant connect  ")

#####################
@app.route("/users",methods=["GET"])
def get_some_users():
    try:
        data=list(db.users.find())
        for user in data:
            user["_id"]=str(user["_id"])
        return Response(
            response=json.dumps(data),
           
            status=200,
            mimetype="application/json"
        )
        
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps(
            {"message":"cannot read users"}),
            status=200,
            mimetype="application/json"
        )

 



########################

#####################
@app.route("/users",methods=["DELETE"])
def DELETE_users():
    try:
        dbResponse=db.users.delete_one({"_id":ObjectId(id)})
        return Response(
            response=json.dumps("USER DELETED"),
           
            status=200,
            mimetype="application/json"
        )
        
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps(
            {"message":"cannot delete users"}),
            status=200,
            mimetype="application/json"
        )

 



########################


@app.route("/users/<id>",methods=["PATCH"])

def update_user(id):
    try:
        dbResponse=db.users.update_one({"_id":ObjectId(id)},
        {"$set":{"name":request.form["name"]}})
        for attr in dir(dbResponse):
            print(f"***{attr}***")


        return Response(
            response=json.dumps(
        {"message":" update user",
            
            }),
            status=500,
            mimetype="application/json"
        )
    except Exception as ex:
        return Response(
            response=json.dumps(
            {"message":"sorry cannot  user",
            
            }),
            status=200,
            mimetype="application/json"
        )
    




##############################

@app.route("/users",methods=["POST"])
def create_users():
    try:
        user={"name":request.form["name"],
        "lastname":request.form["lastname"]}
        dbResponse=db.users.insert_one(user)
        print(dbResponse.inserted_id)
        #for attr in dir(dbResponse):
         #   print(attr)
        return Response(
            response=json.dumps(
            {"message":"user created",
            "id":f"{dbResponse.inserted_id}"
            }),
            status=200,
            mimetype="application/json"
        )

    except Exception as ex:
        print(ex)

##########################################3
if (__name__=="__main__"):
    app.run(port=80,debug=True)