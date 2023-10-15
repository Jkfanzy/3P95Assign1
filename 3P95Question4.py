def filterData(data, limit, exceptions):
    filtered_data = []
    index = 0
    while index < len(data):
        item = data[index]
        if item in exceptions:
            modified_item = item + "_EXCEPTION"
        elif item > limit:
            modified_item = item * 2
        else:
            modified_item = item / limit 
        filtered_data.append(modified_item)
        index += 1
    return filtered_data


#1

def filterData(data, limit, exceptions):
    filtered_data = []
    index = 0
    while index < len(data):
        item = data[index]
        if item not in exceptions: # changed to not in
            modified_item = item + "_EXCEPTION"
        elif item > limit:
            modified_item = item * 2
        else:
            modified_item = item / limit 
        filtered_data.append(modified_item)
        index += 1
    return filtered_data


# 2

def filterData(data, limit, exceptions):
    filtered_data = []
    index = 0
    while index < len(data):
        item = data[index]
        if item in exceptions:
            modified_item = item + "_EXCEPTION"
        elif item > limit: # changed to >
            modified_item = item * 2
        else:
            modified_item = item / limit 
        filtered_data.append(modified_item)
        index += 1
    return filtered_data

# 3

def filterData(data, limit, exceptions):
    filtered_data = []
    index = 0
    while index < len(data):
        item = data[index]
        if item in exceptions:
            modified_item += item + "_EXCEPTION" # changed to +=
        elif item > limit:
            modified_item = item * 2
        else:
            modified_item = item / limit 
        filtered_data.append(modified_item)
        index += 1
    return filtered_data

# 4

def filterData(data, limit, exceptions):
    filtered_data = []
    index = 0
    while index < len(data):
        item = data[index]
        if item in exceptions:
            modified_item = item + "_EXCEPTION"
        elif item > limit:
            modified_item = item / 2 # changed to / 
        else:
            modified_item = item / limit 
        filtered_data.append(modified_item)
        index += 1
    return filtered_data

# 5

def filterData(data, limit, exceptions):
    filtered_data = []
    index = 0
    while index < len(data):
        item = data[index]
        if item in exceptions:
            modified_item = item + "_EXCEPTION"
        elif item > limit:
            modified_item = item * 2
        else:
            modified_item = item * limit # changed to *
        filtered_data.append(modified_item)
        index += 1
    return filtered_data

# 6

def filterData(data, limit, exceptions):
    filtered_data = []
    index = 0
    while index < len(data):
        item = data[index]
        if item in exceptions:
            modified_item = item + "_EXCEPTION"
        elif item > limit:
            modified_item = item * 2
        else:
            modified_item = item / limit 
        filtered_data.append(modified_item)
        index += 2 # changed to += 2
    return filtered_data