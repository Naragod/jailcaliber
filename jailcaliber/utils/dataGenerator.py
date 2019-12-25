import string
import random as rn


# variables
# ***************************************************************
vin_size = 2


# functions
# ***************************************************************
def generate_random_val(t_range):
  return rn.randint(0, t_range)


def generate_time():
  base = 1503500000
  t_range = 200
  return base + generate_random_val(t_range)


def generate_vin(size=vin_size):
  return ''.join(rn.choice(string.ascii_uppercase + string.digits) for _ in range(size))


# The number of keys and values needs to be the same
def generate_template(keys=[], values=[], result={}):
  if len(keys) != len(values):
    print("Keys and values do not have the same number of items.")
    return result

  if len(keys) == 0:
    return result

  key = keys.pop(0)
  value = values.pop(0)
  result[key] = value
  return generate_template(keys, values, result)


def generate_entry():
  start_time = generate_time()
  keys = [
      "vin",
      "dissipation_value",
      "trip_milage",
      "rtc_time_start",
      "rtc_time_end"
  ]
  values = [
      generate_vin(),
      generate_random_val(100),
      generate_random_val(100),
      start_time,
      start_time + generate_random_val(10)
  ]
  return generate_template(keys, values)


def generate_data(size, result=[]):
  if(size == 0):
    return result

  result.append(generate_entry())
  return generate_data(size - 1, result)


# get energy/km dissipated for all data points
# if the trip milage is 0, set it to 1. This will need to be changed
def set_energy_per_milage(data):
  for d in data:
    if d["trip_milage"] == 0:
      d["trip_milage"] = 1
    e_per_k = d["dissipation_value"] / d["trip_milage"]
    d["e_per_k"] = round(e_per_k, 4)
  return data
