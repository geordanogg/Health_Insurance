import pickle
import numpy  as np
import pandas as pd

class HealthInsurance:
    
    def __init__( self ):
        self.home_path             = '/home/geordano/repos/Health_Insurance/health_insurance_cross_sell/'
        self.age_scaler            = pickle.load( open( self.home_path + 'src/features/age_scaler.pkl','rb' ) ) 
        self.annual_premium_scaler = pickle.load( open( self.home_path + 'src/features/annual_premium_scaler.pkl','rb' ) )
        self.gender_scaler         = pickle.load( open( self.home_path + 'src/features/gender_scaler.pkl','rb' ) )
        self.historical_scaler     = pickle.load( open( self.home_path + 'src/features/historical_scaler.pkl','rb' ) )
        self.potential_scaler      = pickle.load( open( self.home_path + 'src/features/potential_scaler.pkl','rb' ) )
        self.region_code_scaler    = pickle.load( open( self.home_path + 'src/features/region_code_scaler.pkl','rb' ) )
        self.p_s_channel_scaler    = pickle.load( open( self.home_path + 'src/features/policy_sales_channel_scaler.pkl','rb' ) )
        self.vehicle_age_scaler    = pickle.load( open( self.home_path + 'src/features/vehicle_age_scaler.pkl','rb' ) )
        self.vintage_scaler        = pickle.load( open( self.home_path + 'src/features/vintage_scaler.pkl','rb' ) )
    
    # ======== defines map functions ========== #
    def vehicle_age_map(self, vehicle_age):
        if vehicle_age == '< 1 Year':
            return 1
        elif vehicle_age == '1-2 Year':
            return 1.5
        else:
            return 2


    def damage_map(self, damage):
        if damage == 'Yes':
            return 1
        else:
            return 0
    
    
    def gender_weight_map(self, gender):
        if gender == 'Male':
            return 0.6
        else:
            return 0.4
        
    
    def premium_weight_map(self, premium):
        if premium < 20000:
            return 0.5
        if 20000 <= premium <= 30000:
            return 2.5
        elif 30000 < premium <= 40000:
            return 3
        elif 40000 < premium <= 50000:
            return 2 
        elif 50000 < premium <= 60000:
            return 1.5
        elif 60000 < premium <= 70000:
            return 1 
        elif 70000 < premium:
            return 0.5

        return 0
    
    
    def age_weight_map(self, age):
        if 20 <= age < 30:
            return 2
        elif 30 <= age < 40:
            return 3
        elif 40 <= age < 50:
            return 4
        elif 50 <= age < 60:
            return 3
        elif 60 <= age < 70:
            return 2
        elif 70 <= age:
            return 1

        return 0
    
      
    def data_cleaning( self, data ):
        # Rename Columns
        data.columns = data.columns.str.lower()
        
        # Change Data Types
        data['id']                   = data['id'].astype( 'int32' )
        data['age']                  = data['age'].astype( 'int16' )
        data['driving_license']      = data['driving_license'].astype( 'uint8' )
        data['region_code']          = data['region_code'].astype( 'int16' )
        data['previously_insured']   = data['previously_insured'].astype( 'uint8' )
        data['policy_sales_channel'] = data['policy_sales_channel'].astype( 'int16' )
        data['vintage']              = data['vintage'].astype( 'uint8' )
        data['response']             = data['response'].astype( 'uint8' )
        
        return data 

    
    def feature_engineering( self, data ):
        # Feature Engineering
        # vehicle_age
        data['vehicle_age'] = data['vehicle_age'].map(self.vehicle_age_map)
        #data['vehicle_age'] = data['vehicle_age'].apply( lambda x: 2 if x == '> 2 Years' else 1.5 if x == '1-2 Year' else 1 )


        # vehicle_damage
        data['vehicle_damage'] = data['vehicle_damage'].map(self.damage_map).astype( 'uint8' ) 
        #data['vehicle_damage'] = data['vehicle_damage'].apply( lambda x: 1 if x == 'Yes' else 0 ).astype( 'uint8' ) 

        # potential
        # Calculus
        #potential =  (data['gender'].map(self.gender_weight_map) + data['annual_premium'].apply(self.premium_weight_map) + 
        #             data['age'].apply(self.age_weight_map) + data['driving_license']) 
        # insert column
        #data.insert(loc=len(data.columns)-1, column='potential', value=potential)

        # historical
        # Calculus
        #historical = (data['vehicle_age']**2 + data['vehicle_damage'] + data['previously_insured'])
        # insert column
        #data.insert(loc=len(data.columns)-1, column='historical', value=historical)
        
        return data
    
    
    def data_preparation( self, data ):
        # age - MinMax Scaler 
        data.loc[:,'age'] = self.age_scaler.transform( data[['age']].values)
        
        # annual_premium - Robust Scaler
        data.loc[:,'annual_premium'] = self.annual_premium_scaler.transform( data[['annual_premium']].values)

        # gender - Factorize Encoding
        factor_gender, unique = pd.factorize(data.loc[:,'gender'], sort=True)
        data.loc[:,'gender'] = factor_gender
        #data.loc[:, 'gender'] = data['gender'].map(self.gender_scaler )
        
        # historical - MinMax Scaler
        data.loc[:,'historical'] = self.historical_scaler.transform( data[['historical']].values)
        
        # potential - Robust Scaler
        data.loc[:,'potential'] = self.potential_scaler.transform( data[['potential']].values)

        # region_code - Target Encoding
        data.loc[:,'region_code'] = data.loc[:,'region_code'].map(self.region_code_scaler)

        # policy_sales_channel - Frequency Encoding
        data.loc[:,'policy_sales_channel'] = data.loc[:,'policy_sales_channel'].map(self.p_s_channel_scaler)

        # vehicle_age - Factorize Encoding
        factor_vehicle_age, unique = pd.factorize(data.loc[:,'vehicle_age'], sort=True)
        data.loc[:,'vehicle_age'] = factor_vehicle_age
        #data.loc[:, 'vehicle_age'] = data['vehicle_age'].map( self.vehicle_age_scaler )        
        
        # vintage - MinMax Scaler
        data.loc[:,'vintage'] = self.vintage_scaler.transform( data[['vintage']].values)

        # fillna
        data = data.fillna(0)

        # Feature Selection by Boruta
        cols_selected = ['age','annual_premium','region_code','policy_sales_channel',
                         'previously_insured','vehicle_damage','vintage']
        
        return data[ cols_selected ]
    
    
    def get_prediction( self, model, original_data, test_data ):
        # model prediction
        pred = model.predict_proba( test_data )
        
        # join prediction into original data
        original_data.loc[:,'score'] = pred[:,1].tolist()
        
        return original_data.to_json( orient='records', date_format='iso' )
