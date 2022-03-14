import json
import requests
import json
from ast import literal_eval

# def get

# Examples:
#   0x2033e559cddff6dd36ec204e3014faa75a01052e  -------->proxy address
#   0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae  -------->not a proxy


def impl_detector(proxyAddres):
    response= requests.get("https://api.etherscan.io/api?"
                        "module=contract&"
                        "action=getsourcecode&"
                        f"address={proxyAddres}&"
                        "apikey=WMXJBN6S7D838WIIN3M64UTA1IMN897HMV")

    data = json.loads(response.text)

    #print (data)

    try:
        proxy= data.get("result")[0].get("Proxy")
    except:
        print(f"error on contract at {proxyAddres}")
        proxy = 0

    if int(proxy)==1:
        
        implementation_Adress= data.get("result")[0].get("Implementation")
        
        implementation_source_Code = ""
        response2 = requests.get("https://api.etherscan.io/api?"
                        "module=contract&"
                        "action=getsourcecode&"
                        f"address={implementation_Adress}&"
                        "apikey=WMXJBN6S7D838WIIN3M64UTA1IMN897HMV")

        data2 = json.loads(response2.text)
        d3: str = data2.get("result")[0].get("SourceCode")
        if not d3.startswith("{"):
            return d3
        if "{{" in d3:
            d3 = d3.replace("{{", "{")
            d3 = d3.removesuffix('}')
        data3 = json.loads(d3)
        if data3.get("sources"):
            data3 = data3.get("sources")
        for item in data3.items():
            implementation_source_Code += item[1].get("content") + "\n\n"
        # implementation_source_Code= data2.get("result")[0].get("SourceCode")[0].get("content")
        return(implementation_source_Code)

    else:
        return(None)




# Read Proxy Address from a file.(Do not forget to craate file b)
f=open('C:\\Users\\sajad\\Desktop\\b.txt')
A= f.readlines()





# Write Implementation Source code in a Solidity file
proxyAddress=""
Implementation=""
for i in range(0, len(A)):
    path = A[i]
    print(f"processing {path}")
    split=path.split("/")
    file=split[len(split)-1]
    proxyAddress="0x" + file.split("_")[0]
    outputPath = path.replace(".sol\n", "Implementation.sol").replace("/", "\\")

    # proxyAddress=hex(literal_eval(address))
    Implementation = impl_detector(proxyAddress)
    if Implementation is not None:
        f=open(f'C:\\Users\\sajad\\Desktop\\ProxyAnalysisResults_1-29-2022\\proxies\\{outputPath}.sol', 'w')
        try:
            print(f"writing to {outputPath}")
            f.write(str(Implementation))
        except:
            print(f"Error writing implementation code from proxy at {proxyAddress}")
        f.close()





#def main(path: str):

#for i in range(0, len(B)):
#    print('\n',B[i],'\n')
