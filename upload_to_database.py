import json
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials


def main():

    all_category = {
        "category1": [],
        "category2": [],
        "category3": [],
        "category4": [],
        "category5": [],
        "category6": [],
    }

    # ===================== Firebase =====================================
    # このPythonファイルと同じ階層に認証ファイルを配置して、ファイル名を格納
    JSON_PATH = 'firebaseの認証ファイル.json'

    # Firebase初期化
    cred = credentials.Certificate(JSON_PATH)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    # ====================================================================
    

    #スクレイピングデータ
    DATA_FILE = 'raw_data1800.json'
    with open(DATA_FILE) as f:
        datas = json.load(f)

    i = 0
    for data in datas:
        db.collection('products').document(data['id']).set(data) 
        if data['type'] == 'おにぎり' or data['type'] == '寿司' or data['type'] == 'サンドイッチ・ロールパン' or data['type'] == 'パン' or data['type'] == '中華まん' :
            all_category["category1"].append(data['id'])      
        elif data['type'] == 'お弁当' or data['type'] == 'そば・うどん・中華麺' or data['type'] == 'スパゲティ・パスタ' or data['type'] == 'グラタン・ドリア' :    
            all_category["category2"].append(data['id'])
        elif data['type'] ==  '惣菜' or  data['type'] == '揚げ物・フランク・焼き鳥' or data['type'] == 'おでん' :
            all_category["category3"].append(data['id'])
        elif data['type'] == 'スイーツ' or data['type'] == 'アイス' or data['type'] == 'ドーナツ':
            all_category["category4"].append(data['id'])
        elif data['type'] == 'サラダ':
            all_category["category5"].append(data['id'])
        elif data['type'] == '飲料':
            all_category['category6'].append(data['id'])
        else:
            continue


    db.collection('categories').document('category').set(all_category)
    
    

if __name__ == '__main__':
    main()