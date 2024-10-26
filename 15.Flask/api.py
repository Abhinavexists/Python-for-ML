# Put and Delete(HTTP verbs)
# Working with API's --JSON

from flask import Flask , jsonify , request

app = Flask(__name__)

## Initial Data in my to-do list
items = [
   {"id":1 , "name": "Item 1" , "description": "This is item 1"},
   {"id":2 , "name": "Item 2" , "description": "This is item 2"}
]

@app.route('/')
def home():
   return "Welcome to To-Do list app"

# GET : retrieve all the items
@app.route('/items' , methods = ['GET'])
def get_items():
   return jsonify(items)

# GET : Retireve a specific item by id
@app.route('/items/<int:item_id>' , methods = ['GET'])
def get_item(item_id):
   item = next((item for item in items if item["id"] == item_id) , None)
   if item is None:
      return jsonify({"error":"items not found"})
   return jsonify(item)

## Post : Create new task - API
@app.route('/items' , methods = ["POST"])
def create_items():
   if not request.json or not 'name' in request.json: # either requeest json is present or not 
       return jsonify({"error":"item not found"})     # or name variable is present or not in request
   new_item={
      "id" : items[-1]["id"] + 1 if items else 1,
      "name" :request.json['name'],
      "description":request.json["description"]
   }                                            
   items.append(new_item)
   return jsonify(new_item)

# PUT : We update an exisiting item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
   item = next((item for item in items if item["id"] == item_id), None)
   if item is None:
    return jsonify({"error": "Item not found"})
   item["name"] = request.json.get('name' , item['name'])
   item["description"] = request.json.get('description' , item['description'])
   return jsonify(item)

# DELETE : Delete an item
@app.route('/items/<int:item_id>' , methods=['DELETE'])
def delete_item(item_id):
   global items
   items = [item for item in items if item['id'] != item_id]
   return jsonify({"result": "Item deleted"})

    

if __name__ == '__main__':
   app.run(debug = True)

