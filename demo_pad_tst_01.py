import json
import pandas as pd
import sys 


# Transfer strinng to json strinng
def processing_str(only_str):    
    the_str = only_str[1:-1]
    the_str = the_str.replace(" ","")
    list_items = the_str.split(",")
    to_str = ""
    for item in list_items:
        kv = item.split(":")
        to_str = to_str + '"' + kv[0]+'":"'+kv[1]+'",'
    to_str = "{" + to_str[:-1] + "}"      
    return to_str


# Complete the string for Message Box
def msg_by_python(inputs):         
    # Transfer string into dictionary    
    pre_outputs = json.loads(inputs)        
    # Process the string for Message Box
    demo_inputs = pre_outputs.copy()
    demo_outputs = {"score": demo_inputs['score'], "level": demo_inputs['level']}    
    flag = int(demo_inputs['score'])
    del demo_inputs['score'] 
    del demo_inputs['level']      
    # Write to CSV file    
    if flag > 400:
        df = pd.DataFrame.from_dict([pre_outputs])    
        df.to_csv("D:\\tst_power_automate\\pad-tst-01\\predict_report.csv", index=False)
        inputs_str="=== 輸入資料 === \n {}\n\n === 預測結果 === \n {}\n\n\n ●資料已寫入csv檔，請檢查。"    
    else:
        inputs_str="=== 輸入資料 === \n {}\n\n === 預測結果 === \n {}"      
    msg = inputs_str.format(json.dumps(demo_inputs), json.dumps(demo_outputs))             
    return msg



if __name__ == "__main__":
    ipts = sys.argv[1:]
    ipts = ''.join(ipts)
    ipts = processing_str(ipts)
    msg = msg_by_python(ipts)
    print(msg)

