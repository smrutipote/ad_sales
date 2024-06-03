import config
import numpy as np
import pickle
import json

class AdSales():
    def __init__(self, tv,radio, social_media, influencer):
        self.tv = tv
        self.radio = radio
        self.social_media = social_media
        self.influencer = influencer
        
    def load_saved(self):
        with open(config.MODEL_PATH,'rb') as f:
            self.model = pickle.load(f)
        
        with open(config.PROJECT_PATH,'r') as f:
            self.project_data = json.load(f)
            
    def get_prediction(self):
        self.load_saved()
        
        test_array = np.zeros(len(self.project_data['columns']))
        test_array[0]= self.tv
        test_array[1]= self.radio
        test_array[2]= self.social_media
        influ_index = self.project_data['columns'].index('influencer_'+ self.influencer)        
        test_array[influ_index] = 1
        print(test_array)
        
        predict = self.model.predict([test_array])[0]
        print(f'The sales prediction is {predict}')
        return predict
 
 
if __name__ == '__main__':
    tv = 52.2
    radio = 36.2
    social_media = 7.5
    influencer = 'nano'
    
    obj = AdSales(tv, radio, social_media, influencer)
    obj.get_prediction()