import pymongo

conn = pymongo.MongoClient()
db = conn.golangGinBlog
col = db.aboutMe

data = [
        {
        'sort':'aboutMe',
        'data':{    
                'stadyexp':'國立高雄師範大學（電子工程系）畢，在學期間主修電子學，工程數學。並且靠兩個考科入取交大光電所。此外在學期間也有選修積體電路，實作時有使用C語言。',
                'workexp':'由2020年開始擔任軟體工程師，負責php-laravel項目的維護，新增功能，網頁的架設，資料的規範及統整。比起硬體，我對軟體還是比較有興趣的。',
                'future':'期望未來自己可以參與到大型自動化專案，數據自動收集、自動遙控、自動下單等...以及整合在手機中利用app告知使用者數據及情報。',
                'interest':'對於有關電腦的事物都有興趣。如果可以像電影裡的黑客就更酷了。此外還對日本ACG文化有興趣，幾乎有時間就會接觸。',
                'personality':'注重化繁為簡，已最少的資源達到最理想的目標。不善與人起爭執，拿出誠懇與和善的態度化解爭執。',
                'note':'個人還是有很多故事可以講的。像是私立轉國立大學之一戰成名轉考跟放讀棄研究所等...。我只覺得人生不易，只能繼續加油了。',
                'step1':'開啟虛擬機器或者架設機器，比較著名的AWS,GCP都提供需多服務，則其中之一就是可以架設虛擬機。',
                'step2':'申請網域，像是AWS Route53並託管DNS，AWS,GCP也都有提供設定路由的服務，機器設定要開啟端口。',
                'step3':'最後只要在機器上架設環境並安裝一個能夠接收用戶請求並給出響應的程序，像是Nginx，就完成了。',
            }
        },
        {
        'sort':'projectInfo',
        'data':{    
                'pixivInfo_d':'由大型爬蟲框架scrapy，所收集之圖片。利用splash渲染js解析了二級、三級頁面得到了原圖origin網址鏈結。',
                'pixivInfo_w':'使用urllib與防止403的ssl完成下載。用cookie來保持登入狀態，可爬取會員專屬圖片。此站cookie相對長效，定期更換php session id 即可。',
                'ps5Info_d':'開賣即完售，官方售價15980，黃牛售價28880。自己要的東西，自己用實力拿。我相信自己的實作能力經得起挑戰。運氣也很不錯能挑戰成功。',
                'ps5Info_w':'使用gcpVM作為server。開賣瞬間機器自動將請求發送給電商網站的api，從server得到訂單編號後再自行將單轉給第三方支付。整個過程只花3秒。',
                'ps5Info_m':'不使用腳本，不使用框架，速度才是唯一考量。',
                'other_d':'為了符合客製化需求經常需要撰寫網頁特效，以及功能。全靠css,javaScript實現。',
                'other_w':'平時也經常統整、處理、運算數據，對於MySql MongoDB基本語法並不會陌生。',
                'jp_m':'自我紹介が遅れました、改めましてリンと申します、よろしくお願い致します。',
                'jp_w':'ゲーム製作会社でソフトエンジニアを務めております。勤務内容は主にAPI機能の新規作成とメンテナンス。データベースを使いデータを計算し，APIを通してwebpageに表示すること。会社で使ったフレームワークはphpのlaravelです。普段使うプログラミング言語はgolang, python3, php, JavaScript。データベースはmongoDB, MySQL。会社で使う作業システムはlinuxのcentOS, ubuntu, debian、UnixのMacOSとwindowsです。',
                'jp_d':'将来の目標は仕事を通して多く技術を研鑽したい、学びたい。そしてその技術を会社のプロジェクトに投入します。自己研鑽の途中は様々な困難に直面するかもしれませんが私は承知しております。それにもかかわらず、私は試したい、挑戦したいと思います。心構えがきめました、自分の最善をつくします。',
                'skill_d':'主要由Jquery與css跟插件完成的屏障，其功能為網頁在loading時讓操作者不去做其他操作以免請求太多對server造成負擔。',
                'skill_w':'舉凡ubuntu,centOS,debian,kali都有使用經驗，基本的linux語法都略知ㄧ二。e.g cd sudo chmod curl.. ',
            }
        },
        {
        'sort':'footer',
        'data':{
                'footer_0':'無情連結。',
                'footer_1':'github。',
                'footer_2':'dockerhub。',
                'footer_3':'個人簡介。',
            }
        },
        {
        'sort':'linkData',
        'data':{
                'link_0':'<strong><a href="https://www.buygames.com.tw">https://www.buygames.com.tw</a></strong><br>感謝此站提供PlayStation 5，優質商家。專賣遊戲主機，ps4,ps5,swtich遊戲軟體與周邊的店家。擁有實體店面。',
                'link_1':'<strong><a href="https://www.pixiv.net">https://www.pixiv.net</a></strong><br>使用者突破5000萬，主要由日本藝術家組成，以插圖、漫畫、小說創作為中心的社群網站。以及根據使用者反饋，營運方會積極改善網站。建立創作者跟鑑賞者更良好的互動。',
                'link_2':'<strong><a href="https://cdnjs.com">https://cdnjs.com</a></strong><br>提供各式框架或插件的網站，可以免費下載jquery,vue,react。也提供html標籤連接。可以直接連上該站使用項目。相當方便。',

            }
        }
        
    ]
for i in data:
    cur = col.insert_one(i)

# cur = col.aggregate([])
# for i in cur:
#     print(i)
