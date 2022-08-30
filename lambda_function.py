import pickle 

filename = 'iris_model.sav'
model = pickle.load(open(filename, 'rb'))

def predict(features):
    return model.predict(features).tolist()

def lambda_handler(event, context):
    values = event['values']
    result = predict(values)
    return result
# predict([[1,2,3,4]])