import pymongo
import datetime

client = pymongo.MongoClient("mongodb://root:dmuestc@mongodb.dmuestc.xyz:32127/")

db = client["FoodDelivery"]

user_collection = db["user"]
good_collection = db["good"]
address_collection = db["address"]
order_collection = db["order"]

test_user = {
    "user_id": "test_user",
    "user_type": "user",
    "password": "password",
    "phone": "xxxxxxxxx",
    "nid": "shjadkhkjashkdj",
    "create_time": datetime.datetime.now(),
    "modify_time": datetime.datetime.now(),
}

# test find
user = user_collection.find_one({"user_id": "test_user"})
print(user)

# result = user_collection.insert_one(test_user)
# insert_id = result.inserted_id
# user = user_collection.find_one({"_id": insert_id})
# print(user)
