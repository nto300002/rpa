from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# ドライバーの初期化
chrome_options = Options()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# ウェブサイトにアクセス
driver.get("https://asobe202007.com/")

try:
    wait = WebDriverWait(driver, 20)

    # ページの読み込み完了を待機
    wait.until(lambda x: x.execute_script("return document.readyState") == "complete")

    # telクラスを持つ要素を全て取得
    tel_elements = driver.find_elements(By.CLASS_NAME, "tel")

    if tel_elements:
        print(f"telクラスを持つ要素が{len(tel_elements)}個見つかりました")

        for i, element in enumerate(tel_elements, 1):
            # telクラス要素内のaタグを取得
            a_elements = element.find_elements(By.TAG_NAME, "a")

            if a_elements:
                print(f"\n要素 {i}のaタグ:")
                for j, a_element in enumerate(a_elements, 1):
                    # 複数の方法でテキストを取得
                    text = a_element.text.strip()
                    href = a_element.get_attribute('href')
                    inner_text = a_element.get_attribute('innerText')
                    text_content = a_element.get_attribute('textContent')

                    # imgタグがある場合はalt属性を取得
                    img_elements = a_element.find_elements(By.TAG_NAME, "img")
                    img_alt = None
                    if img_elements:
                        img_alt = img_elements[0].get_attribute('alt')

                    print(f"    Link {j}:")
                    print(f"        Text: {text}")
                    print(f"        Inner Text: {inner_text}")
                    print(f"        Text Content: {text_content}")
                    if img_alt:
                        print(f"        Image Alt: {img_alt}")
                    if href:
                        print(f"        URL: {href}")

                    # 親要素全体のテキストも取得
                    parent_text = element.text.strip()
                    print(f"        Parent Element Text: {parent_text}")

                    # ファイルに保存
                    with open('tel_links.txt', 'a', encoding='utf-8') as f:
                        f.write(f"\n要素 {i} - Link {j}:\n")
                        f.write(f"Text: {text}\n")
                        f.write(f"Inner Text: {inner_text}\n")
                        f.write(f"Text Content: {text_content}\n")
                        if img_alt:
                            f.write(f"Image Alt: {img_alt}\n")
                        if href:
                            f.write(f"URL: {href}\n")
                        f.write(f"Parent Text: {parent_text}\n")
                        f.write("-" * 50 + "\n")
            else:
                print(f"\n要素 {i}にはaタグが見つかりませんでした")
    else:
        print("telクラスを持つ要素は見つかりませんでした")

except TimeoutException:
    print("ページの読み込みに時間がかかりすぎました。")

finally:
    # ブラウザを閉じる
    driver.quit()
