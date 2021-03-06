def process_numbers(unprocessed_list):
    
    processed_list = []
    # if input is not list, return empty list
    if isinstance(unprocessed_list, list) == False:
        return processed_list
    
    # distinguish int ot str 
    for item in unprocessed_list:
        if isinstance(item, int):
            processed_list.append(item)
        elif isinstance(item, str):
            # for instance '4' -> 4
            # if not number, just ignore and go next
            if item.isnumeric():
                converted_item = int(item)
                processed_list.append(converted_item)
    
    processed_list.sort()
    return processed_list


def process_names(unprocessed_list):
    
    processed_list = []

    if isinstance(unprocessed_list, list) == False:
        return processed_list
    
    for item in unprocessed_list:
        if isinstance(item, str):
            # if it is numeric, just ignore and go next
            if item.isnumeric() == False:
                processed_list.append(item)
    
    processed_list.sort()
    return processed_list