from scapy.all import *
from scapy.layers.dot11 import Dot11

conf.use_pcap=True

results = {}


def callBack(pkt):
    # print(pkt.show())

    # Check for mac address
    if pkt.haslayer(Dot11):
        key = None
        if not pkt.FCfield.to_DS and pkt.FCfield.from_DS:
            if pkt.addr3 is not None:
                key = pkt.addr3
        else:
            if pkt.addr2 is not None:
                key = pkt.addr2

        # Check for existing results
        if key is not None:
            if key not in results.keys():
                results[key] = {}
                results[key]["samplesRssi"] = 0
                results[key]["maxRssi"] = -100
                results[key]["minRssi"] = 0
                results[key]["avgRssi"] = 0
                results[key]["samplesNoise"] = 0
                results[key]["maxNoise"] = -100
                results[key]["minNoise"] = 0
                results[key]["avgNoise"] = 0
                results[key]["ssid"] = ""

            # Store SSID
            if pkt.type == 0 and pkt.subtype == 8:
                if key in results.keys():
                    if results[key]["ssid"] == "":
                        results[key]["ssid"] = pkt.info

            if key in results.keys():
                # Store rssi values
                curRssi = pkt.dBm_AntSignal
                if curRssi != 0:
                    if results[key]["maxRssi"] < curRssi:
                        results[key]["maxRssi"] = curRssi

                    if results[key]["minRssi"] > curRssi:
                        results[key]["minRssi"] = curRssi

                    avgRssi = results[key]["avgRssi"]
                    samples = results[key]["samplesRssi"] + 1
                    avgRssi = (((samples - 1) * avgRssi) + curRssi) / samples

                    results[key]["samplesRssi"] = samples
                    results[key]["avgRssi"] = avgRssi

                # Store Noise values
                curNoise = pkt.dBm_AntNoise
                if curNoise != 0:
                    if results[key]["maxNoise"] < curNoise:
                        results[key]["maxNoise"] = curNoise

                    if results[key]["minNoise"] > curNoise:
                        results[key]["minNoise"] = curNoise

                    avgNoise = results[key]["avgNoise"]
                    samples = results[key]["samplesNoise"] + 1
                    avgNoise = (((samples - 1) * avgNoise) + curNoise) / samples

                    results[key]["samplesNoise"] = samples
                    results[key]["avgNoise"] = avgNoise


i = 0
while i < 5:
    sniff(iface='en0', monitor='True', prn=callBack, count=200)
    i += 1
    print("Iteration %d" %(i))

for res in results:
    print(res, results[res])