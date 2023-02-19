import json
import numpy as np
import os,sys,shutil
### Do classification on WLASL
new_dict = {}
with open("WLASL_v0.3.json","r") as f:
    load = json.load(f)
    # print("Done!")
    # print(load)
    #print(len(load)) # 2000
    #print(type(load)) # <class 'list'>
    # print(load[0]['instances'][0]["video_id"]) # list + dict + list + dict

# print(len(load[0]['instances'])) # 每个gloss视频的数量 ！！
Gloss = [] # Store the gloss to the list
for i in range(2000):
    Gloss.append(load[i]["gloss"])
    # if load[i]["gloss"] == 'never':
    #     print(i)

defaultPath = r'C:\Users\JiangYufeng\Desktop\WLASL2000'
actions = np.array(Gloss)
# print(actions)
# mkdirs for each gloss
for action in actions:
    try:
        os.makedirs(os.path.join(defaultPath,action))
    except:
        pass

source_folder=r'C:\Users\JiangYufeng\Desktop\WLASL2000\WLASL2000'
# new_path = r'C:\Users\JiangYufeng\Desktop\WLASL2000\{}'.format()

with open("video_id.json","r") as id_file:
    load_id = json.load(id_file)
    # print(type(load_id)) # <class 'dict'>
    
        
        # print(item) # output is each gloss
        # print(load_id[item]) # output is video_id for each gloss
        # print(len(load_id)) 
    file_list = os.listdir(source_folder)
    for file_obj in file_list:
        for item in load_id:
            new_path = r'C:\Users\JiangYufeng\Desktop\WLASL2000\{}'.format(item)
            file_path=os.path.join(source_folder,file_obj)
            file_name,file_extend=os.path.splitext(file_obj)
            for i in range(len(load_id[item])):
                
                # print(i,'current target copy path:', new_path,item)
                if file_name == load_id[item][i]:
                    newfile_path = os.path.join(new_path, file_obj)
                    shutil.copyfile(file_path,newfile_path)
                    break
                else:
                    if i == (len(load_id[item]) - 1 ):
                        break
                    else:
                        continue
                
# file_list=os.listdir(source_folder)
# for file_obj in file_list:
#     file_path=os.path.join(source_folder,file_obj)
#     file_name,file_extend=os.path.splitext(file_obj)
#     with open("video_id.json","r") as id_file:
#         load_id = json.load(id_file)
#         for i in load_id:
#             new_path = r'C:\Users\JiangYufeng\Desktop\WLASL2000\{}'.format(i))
#             if file_name == 