#!/usr/bin/python3
"""for testing th file storage 
"""

#!/usr/bin/python3
from models import storage
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = User()
my_model.name = "Berrchid"
my_model.last_name = "PLace"
my_model.my_number = 200
my_model.save()
print(my_model)