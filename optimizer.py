import time
from tqdm import tqdm
def optimize(config_lists,trial,nb_trials=10,nb_iteration=3):
    #Compute default value for every parameter
    default_config = {} #best config found yet (default at first)
    doc = {}
    for param_name in config_lists:
        default_config[param_name] = config_lists[param_name][0] #the default config is the first value of each parameter in their respective lists of values
    #Optimize each parameter one by one
    for it in range(nb_iteration): #Run nb_iteration steps of optimization
        doc = {}
        for param_name in config_lists: #Select a parameter
            print(param_name)
            doc[param_name] = {}
            #Compute score for each value of parameter
            param_vals = config_lists[param_name]
            scores = [0]*len(param_vals)
            for idx_val in range(len(param_vals)): #Select a value of the parameter
                doc[param_name][param_vals[idx_val]] = []
                print('   ',param_vals[idx_val])
                for t in tqdm(range(nb_trials)):
                    config_param_val = default_config.copy() #Get the best config found yet 
                    config_param_val[param_name] = param_vals[idx_val] #Change only one parameter
                    score_param,doc_param = trial(**config_param_val) #Run the test and get results
                    scores[idx_val] += score_param/nb_trials #Add the score to the average
                    doc[param_name][param_vals[idx_val]].append((config_param_val,doc_param)) #Add data to the doc
            #Find the best value for the parameter
            for i,s in enumerate(scores):
                if s == max(scores): 
                    default_config[param_name] = param_vals[i] #Put it in the best config found yet
    return default_config,doc
