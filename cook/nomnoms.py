import json
from .models import Ingredient

def populate():
    with open('cook/food.json') as f:
        try:
            data = json.load(f)
            rows = data['rows']
            for row in rows:
                name_string = row[1]
                try:
                    data_dict = eval(row[0])
                    Ingredient.objects.create(title = name_string, 
                                            description = data_dict['Description'],
                                            category = data_dict['Category'],
                                            data = data_dict['Data'])    
                except:
                    data_dict = {}
                
  
                print('created item {0} with category {1}'.format(name_string, data_dict['Category']))
        finally:
            f.close()
def flush_ingredients():
    Ingredient.objects.delete()





