from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    # デバッグモードで起動済みのChromeに接続するための設定
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    
    # WebDriverを初期化
    driver = webdriver.Chrome(options=chrome_options)
    
    # 新しいタブでGoogle Mapsを開く
    driver.execute_script("window.open('https://www.google.com/maps', '_blank');")
    
    # 新しく開いたタブに切り替え
    driver.switch_to.window(driver.window_handles[-1])
    
    # ファイルから市役所名を読み込み
    with open("shiyakusyo.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        if lines:
            city_name = lines[0].strip()
            
            # 検索ボックスを見つけて入力
            try:
                search_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "searchboxinput"))
                )
                search_query = f"{city_name} 市役所"
                search_box.send_keys(search_query)
                search_box.send_keys(Keys.ENTER)
                
                # 検索結果が表示されるまで待機
                time.sleep(3)
                
                # ここで残りの処理を実装
                # ...
                
                # ファイルの先頭行を削除
                with open("shiyakusyo.txt", "r", encoding="utf-8") as file:
                    remaining_lines = file.readlines()[1:]
                
                with open("shiyakusyo.txt", "w", encoding="utf-8") as file:
                    file.writelines(remaining_lines)
                    
            except Exception as e:
                print(f"エラーが発生しました: {e}")
        else:
            print("shiyakusyo.txtが空です")
    
    # ブラウザは閉じない（永続化）
    print("処理完了。ブラウザは開いたままです。")

if __name__ == "__main__":
    main()
