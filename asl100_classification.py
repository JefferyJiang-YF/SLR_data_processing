import json
import os
asl_100 = ['book', 'drink', 'computer', 'before', 'chair', 'go', 'clothes', 'who', 'candy', 'cousin', 'deaf', 'fine', 'help', 'no', 'thin', 'walk', 'year', 'yes', 'all', 'black', 'cool', 'finish', 'hot', 'like', 'many', 'mother', 'now', 'orange', 'table', 'thanksgiving', 'what', 'woman', 'bed', 'blue', 'bowling', 'can', 'dog', 'family', 'fish', 'graduate', 'hat', 'hearing', 'kiss', 'language', 'later', 'man', 'shirt', 'study', 'tall', 'white', 'wrong', 'accident', 'apple', 'bird', 'change', 'color', 'corn', 'cow', 'dance', 'dark', 'doctor', 'eat', 'enjoy', 'forget', 'give', 'last', 'meet', 'pink', 'pizza', 'play', 'school', 'secretary', 'short', 'time', 'want', 'work', 'africa', 'basketball', 'birthday', 'brown', 'but', 'cheat', 'city', 'cook', 'decide', 'full', 'how', 'jacket', 'letter', 'medicine', 'need', 'paint', 'paper', 'pull', 'purple', 'right', 'same', 'son', 'tell', 'thursday']
asl_dict = {}
def addIndex():
    for i in range(len(asl_100)):
        temp = {str(i+1):asl_100[i]} # asl_100 start with 1 rather than 0 
        asl_dict.update(temp)

addIndex()
source_path = r'C:\Users\JiangYufeng\Desktop\gloss'
with open('nslt_100.json',"r") as f:
    new_path = 'C:\deep-learning\WLASL\data'
    load = json.load(f)
    
    # print(type(load)) # <class 'dict'>
    # print(len(load)) 2038
    for key, value in load.items():
        #print(value.get("subset")) 获取其分类
        #print(value.get("action")[0]) 获取视频索引
        #print(asl_dict.get("1"))
        if value.get("subset") == 'train':
            pass
        elif value.get("subset") == 'val':
            pass
        else:
            pass
#print(os.path.join('C:\deep-learning\WLASL\data','test'))