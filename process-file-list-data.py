import json
glist = []
def process_data(filepath):
  with open(filepath) as f:
    data = f.read()
    data = json.loads(data)
    for item in data:
      glist.append(item)

# def sort():
#   sorted(glist, key=lambda x:x["start"])

def save_to_outfile(filepath):
  g = json.dumps(glist)
  with open(filepath, 'w') as f:
    f.write(g)

if __name__ == '__main__':
  ipvs = ["/Users/richctrl/Desktop/广电.txt", "/Users/richctrl/Desktop/华数.txt", 
  "/Users/richctrl/Desktop/教育网.txt", "/Users/richctrl/Desktop/金桥网.txt", 
  "/Users/richctrl/Desktop/联通.txt", "/Users/richctrl/Desktop/铁通.txt", 
  "/Users/richctrl/Desktop/网通.txt", "/Users/richctrl/Desktop/移动.txt",
  "/Users/richctrl/Desktop/盈联.txt", "/Users/richctrl/Desktop/油田.txt", 
  "/Users/richctrl/Desktop/有线.txt", "/Users/richctrl/Desktop/长城.txt",
  "/Users/richctrl/Desktop/中邦.txt", "/Users/richctrl/Desktop/中科网.txt",
  "/Users/richctrl/Desktop/珠江.txt", "/Users/richctrl/Desktop/电信.txt",
  "/Users/richctrl/Desktop/东南.txt", "/Users/richctrl/Desktop/方正.txt"]
  for item in ipvs:
    process_data(item)
  save_to_outfile("./result.json")
