import time
from tqdm import tqdm
def optimize(config_lists,trial,nb_trials=10):
    #Compute default value for every parameter
    default_config = {}
    doc = {}
    for param_name in config_lists:
        default_config[param_name] = config_lists[param_name][0]
    #Optimize each parameter one by one
    for it in range(3):
        doc = {}
        for param_name in config_lists:
            print(param_name)
            doc[param_name] = {}
            #Compute score for each value of parameter
            param_vals = config_lists[param_name]
            scores = [0]*len(param_vals)
            for idx_val in range(len(param_vals)):
                doc[param_name][param_vals[idx_val]] = []
                print('   ',param_vals[idx_val])
                for t in tqdm(range(nb_trials)):
                    config_param_val = default_config.copy()
                    config_param_val[param_name] = param_vals[idx_val]
                    score_param,doc_param = trial(**config_param_val)
                    scores[idx_val] += score_param/nb_trials
                    doc[param_name][param_vals[idx_val]].append((config_param_val,doc_param))
            #Find idx max
            for i,s in enumerate(scores):
                if s == max(scores):
                    default_config[param_name] = param_vals[i]
    return default_config,doc
