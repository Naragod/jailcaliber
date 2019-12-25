# global variables
# ***************************************************************
decimal_places = 4


# general functions
# ***************************************************************
def toNumPlaces(data, places=decimal_places):
  return implement_recursion(data, lambda x: round(x, places), [])


# general implementation of a recursive function in which data
# from the array is popped off on each iteration. The result
# must be passed in with every call to this function. It seems
# that if result is not passed in, its value will not be
# implitly cleared and remain populated.
def implement_recursion(data, cb, result):
  if len(data) == 0:
    return result

  result.append(cb(data.pop(0)))
  return implement_recursion(data, cb, result)


# filter functions
# ***************************************************************
def key_exits(obj, key):
  if key in obj:
    return True
  return False


# returns the index of the first obj found in the list or -1 otherwise
def search_for(data, key, value, index=0):
  if len(data) == index:
    return -1

  current = data[index]
  if key_exits(current, key):
    if current[key] == value:
      return index

  return search_for(data, key, value, index + 1)


# returns an array of all the indices of the searched for object, key and value
def search_for_all(data, key, value, result=[], index=0):
  res_index = search_for(data, key, value, index)
  if res_index == -1:
    return result

  result.append(res_index)
  return search_for_all(data, key, value, result, res_index + 1)


# Receives in a dictionary and a list of keys or a single key.
# It will return the dictionary filtered by the specified params.
def filter_dict_by_param(data, params):
  return {key: data[key] for key in data.keys() if key in params}


# Receives in a list of dictionaries and a list of params and it will return
# a list of dictionaries filtered by those params. If the group_by and aggregate
# options are passed in, it will return a single dictionary with all of the specified
# values
def filter_list_by_param(data, params, group_by="", aggregate=False):
  if not aggregate:
    return [filter_dict_by_param(d_point, params) for d_point in data]

  if group_by not in params:
    print("The chosen aggregate value `groub_by` must be in the filtered list `params`")
    return False

  return {group_by: [filter_dict_by_param(d_point, params)[group_by] for d_point in data]}


# This assumes a dictionary with one single key.
# If a multikey dictionary is passed in, it will return the value of the first key
def get_dict_val(dictionary):
  key = [key for key in dictionary.keys()][0]
  return dictionary[key]
