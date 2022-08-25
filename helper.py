import os
import random
import pandas as pd


def get_collection():
    data_dir = os.getcwd()+'/collection'
    collection_df = pd.read_csv(
        data_dir+'/wcma-collection.csv', low_memory=False)
    return collection_df


def generate_object():
    random_int = random.randint(0, len(get_collection()))
    random_object = get_collection().iloc[random_int]
    object_string = str(random_object[1]) + ', ' + str(random_object[2]) + ', ' + str(random_object[7]) + \
        ', ' + str(random_object[12]) + ', ' + str(random_object[4])
    print(object_string)
    return object_string
