def compact_doc(doc):
    #Computes the average of the doc
    compacted_doc = {}
    for param_name in doc:
        compacted_doc[param_name] = {}
        for param_val in doc[param_name]:
            compacted_doc[param_name][param_val] = {}
            for (config,result) in doc[param_name][param_val]:
                for key in result:
                    try:
                        compacted_doc[param_name][param_val][key] += result[key]/len(doc[param_name][param_val])
                    except KeyError:
                        compacted_doc[param_name][param_val][key] = result[key]/len(doc[param_name][param_val])
    return compacted_doc
