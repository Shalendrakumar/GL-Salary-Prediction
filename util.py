import pickle
import json
import numpy as np

__all_columns = None
__size = None
__type_of_ownership = None
__Sector = None
__Revenue = None
__job_state = None
__job_simp = None
__seniority = None
__model = None

#Size,Type_of_ownership,Sector,Revenue,job_state,job_simp,seniority

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __all_columns
    global __size
    global __type_of_ownership
    global __sector
    global __revenue
    global __job_state
    global __job_simp
    global __seniority
    global __model

    with open("./artifacts/all_columns.json", "r") as f:
        __all_columns = json.load(f)['all_columns'] 
        
    with open("./artifacts/size_columns.json", "r") as f:
          __size = json.load(f)['size_columns']  
          
    with open("./artifacts/Type_columns.json", "r") as f:
        __type_of_ownership = json.load(f)['Type_columns']
        
    with open("./artifacts/sector_columns.json", "r") as f:
        __sector = json.load(f)['sector_columns']
        
    with open("./artifacts/Revenue_columns.json", "r") as f:
        __revenue = json.load(f)['Revenue_columns']
        
    with open("./artifacts/job_state_columns.json", "r") as f:
        __job_state = json.load(f)['job_state_columns']
        
    with open("./artifacts/job_simp_columns.json", "r") as f:
        __job_simp = json.load(f)['job_simp_columns']
        
    with open("./artifacts/seniority_columns.json", "r") as f:
        __seniority = json.load(f)['seniority_columns']
    
    with open('./artifacts/final_model_file_rf.pickle', 'rb') as f:
        __model = pickle.load(f)
     
    print("loading saved artifacts...done")

def replace_size_string():
    size=[]
    for i in __size:
        i = i.replace("size_", "")
        size.append(i)
    return size    
def replace_too_string():
    too=[]
    for i in __type_of_ownership:
        i = i.replace("type of ownership_", "")
        too.append(i.title())
    return too         
def replace_sector_string():
    sec=[]
    for i in __sector:
        if i=='sector_-1':
            i='none'
            sec.append(i)
        else:      
            i = i.replace("sector_", "")
            sec.append(i.title())
    return sec

def replace_revenue_string():
    revenue=[]
    for i in __revenue:
        i = i.replace("revenue_", "")
        revenue.append(i)
    return revenue 

def replace_job_state_string():
    job_s=[]
    for i in __job_state:
        i = i.replace("job_state_", "")
        job_s.append(i.upper())
    return job_s 

def replace_seniority_string():
    sen=[]
    for i in __seniority:
        i = i.replace("seniority_", "")
        sen.append(i.upper())
    return sen 

def replace_designation_string():
    designation=[]
    for i in __job_simp:
        i = i.replace("job_simp_", "")
        designation.append(i.title())
    return designation 
    
def get_estimated_salary(size):
    try:
        size_index = __all_columns.index(size.lower())
        print(size_index)
    except:
        loc_index = -1 
        
def predict_salary(rating,hourly,age,python_yn,spark,aws,size,type_of_ownership,sector,revenue,job_state,job_simp,seniority):    
    
    Size_index = __all_columns.index(size.lower())
    TOO_index = __all_columns.index(type_of_ownership.lower())
    Sector_index = __all_columns.index(sector.lower())
    Revenue_index = __all_columns.index(revenue.lower())
    job_state_index = __all_columns.index(job_state.lower())
    job_simp_index = __all_columns.index(job_simp.lower())
    seniority_index = __all_columns.index(seniority.lower())

    x = np.zeros(len(__all_columns))
    x[0] = rating
    x[1] = hourly
    x[2] = age
    x[3] = python_yn
    x[4] = spark
    x[5] = aws
 
    if Size_index >= 0:
        x[Size_index] = 1
    if TOO_index >= 0:
        x[TOO_index] = 1
    if Sector_index >= 0:
        x[Sector_index] = 1        
    if Revenue_index >= 0:
        x[Revenue_index] = 1
    if job_state_index >= 0:
        x[job_state_index] = 1
    if job_simp_index >= 0:
        x[job_simp_index] = 1 
    if seniority_index >= 0:
        x[seniority_index] = 1         
      
    return round(__model.predict([x])[0],2)
    
def get_all_columns():
    return __all_columns
    
def get_company_size():
    return __size

def get_type_of_ownership():
    return __type_of_ownership

def get_sector():
    return __sector

def get_revenue():
    return __revenue
    
def get_job_state():
    return __job_state

def get_job_designation():
    return __job_simp

def get_seniority():
    return __seniority
    
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_all_columns(),'\n')
    print(get_company_size(),'\n')
    print(get_type_of_ownership(),'\n')
    print(get_sector(),'\n')
    print(get_revenue(),'\n')
    print(get_job_state(),'\n')
    print(get_job_designation(),'\n')
    print(get_seniority(),'\n')
    print(get_estimated_salary('size_10000+ employees'))
    print(predict_salary(3.8,0,47,1,0,0,'Size_501 to 1000 employees','Type of ownership_Company - Private','Sector_Aerospace & Defense',
               'Revenue_$50 to $100 million (USD)','job_state_NM','job_simp_data scientist','seniority_na') )
    
