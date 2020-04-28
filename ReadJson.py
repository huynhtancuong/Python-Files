import json


class temperature:
    def __init__(self, argtime, argvalue):
        self.year   = int(argtime[0:4])
        self.month  = int(argtime[5:7])
        self.day    = int(argtime[8:10])
        self.hour   = int(argtime[11:13])
        self.minute = int(argtime[14:16])
        self.second = int(argtime[17:19])
        self.value  = float(argvalue)


json_file = open("Temperature-20200421-1421.json", "r")
data = json.load(json_file)

counter = 0

for line in range(len(data)):
    argtime     = data[line]["created_at"]
    argvalue    = data[line]["value"]
    atime       = temperature(argtime, argvalue)
    print("[%2dh%2dm%2ds][%2d/%2d/%4d] Temperature = %.2f*C" % (atime.hour, atime.minute, atime.second, atime.day, atime.month, atime.year, atime.value))
    counter += 1

print('records = ',counter)
