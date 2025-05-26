from constant import collection 

def create_user():
    user_dict ={
        "name"     :  "sharanya",
        "password" :  "sharanya331",
        "dept"     :  "BCA",
        "domain"   :  "AI"
    }

    if user_dict:

        user = collection.insert_one(user_dict)

        if user.inserted_id:
            return f'Data Inserted Successfully'
        else:
            return f'Failed to Insert Data'
        

    if user_dict:
        user=collection.find_one({"name": user_dict["name"]})

        if user:
            return f'User exists with name: {user}'
        else:
            return f'User does not exist'


    if user_dict:
        user = collection.update_one({"name": user_dict["name"]}, {"$set": {"name": "sharanya31"}})

        if user.modified_count:

            return f'Data Updated Successfully'
        else:
            return f'Failed to Update Data'
        

    if user_dict:
        user = collection.delete_one({"name": user_dict["name"]})

        if user.deleted_count:
            return f'Data Deleted Successfully'
        else:
            return f'Failed to Delete Data'
           
        
    

def main():
    print('create_user():', create_user())

if __name__ == "__main__":
    main()