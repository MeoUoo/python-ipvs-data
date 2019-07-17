import json
import os

def load_data(filepath, name):
  _list = []
  with open(filepath) as f:
    lines = f.readlines()
    for line in lines:
      line = line.strip("\n").split("\t")
      _list.append({"start": line[0], "end": line[1], "source": name})
  result = json.dumps(_list)
  return result

def save_data(_list, filepath):
  with open(filepath, 'w') as outfile:
    outfile.write(_list)

if __name__ == '__main__':
  ipvs = ["/Users/richctrl/Desktop/ip运营商/广电.txt", "/Users/richctrl/Desktop/ip运营商/华数.txt", 
  "/Users/richctrl/Desktop/ip运营商/教育网.txt", "/Users/richctrl/Desktop/ip运营商/金桥网.txt", 
  "/Users/richctrl/Desktop/ip运营商/联通.txt", "/Users/richctrl/Desktop/ip运营商/铁通.txt", 
  "/Users/richctrl/Desktop/ip运营商/网通.txt", "/Users/richctrl/Desktop/ip运营商/移动.txt",
  "/Users/richctrl/Desktop/ip运营商/盈联.txt", "/Users/richctrl/Desktop/ip运营商/油田.txt", 
  "/Users/richctrl/Desktop/ip运营商/有线.txt", "/Users/richctrl/Desktop/ip运营商/长城.txt",
  "/Users/richctrl/Desktop/ip运营商/中邦.txt", "/Users/richctrl/Desktop/ip运营商/中科网.txt",
  "/Users/richctrl/Desktop/ip运营商/珠江.txt", "/Users/richctrl/Desktop/ip运营商/电信.txt",
  "/Users/richctrl/Desktop/ip运营商/东南.txt", "/Users/richctrl/Desktop/ip运营商/方正.txt"]
  for item in ipvs:
    _, file = os.path.split(item)
    name = file.split(".")[0]
    filepath = "/Users/richctrl/Desktop/" + name + ".txt"
    _list = load_data(item, name)
    save_data(_list, filepath)
