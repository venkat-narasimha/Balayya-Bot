import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the BOT_TOKEN environment variable
BotToken = os.getenv('BotToken')

#inviteLink
invite_link ='👉 [Click here](https://discord.com/api/oauth2/authorize?client_id=794782697440280626&permissions=8&scope=bot)'

#bot profile
dp1='https://cdn.discordapp.com/attachments/1093230444645974217/1093230555946029187/B_Bot_Dp.png'
dp2='https://cdn.discordapp.com/attachments/1093230444645974217/1093230775148752977/bb_dp_2.jpg'
mansion_house='https://cdn.discordapp.com/attachments/1093230444645974217/1093230682207178772/mansion_house.jpg'

dailouge_pics =[
'https://cdn.discordapp.com/attachments/1093229958303858719/1093230873748447315/1.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093230999913111593/1-2-1.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231015302012988/2.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231032100204605/2-2-1.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231037359869962/3-2-1.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231040069374063/3.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231049594642632/4.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231057639309433/4-1-1.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231077675516017/5.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231082444423208/5-1-1.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231085325910027/6.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231094410772652/7.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231097778810910/6-1-1.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231104053481645/7-2-1.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231117093572789/8.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231130406289438/9.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231139407286323/8-2-1.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231144876646481/9-2-1.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231157627342928/10-1-1.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231161351864421/10.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231179827785760/11-1-1.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231185485910126/12-1-2.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231189063639150/13-1-1.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231202472833184/14-1-1.jpg'
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231222496440360/15-3-1.jpg',
'https://cdn.discordapp.com/attachments/1093229958303858719/1093231225726050304/ruler.jpg'
]


greeting_gifs = [
'https://cdn.discordapp.com/attachments/1093230022413791413/1093238013972201592/g1.gif',
'https://cdn.discordapp.com/attachments/1093230022413791413/1093238063037161592/g2.gif',
'https://cdn.discordapp.com/attachments/1093230022413791413/1093238080737136741/g3.gif',
'https://cdn.discordapp.com/attachments/1093230022413791413/1093238091277414553/g4.gif',
'https://cdn.discordapp.com/attachments/1093230022413791413/1093238098894262272/g5.gif',
'https://cdn.discordapp.com/attachments/1093230022413791413/1093238124970258432/g6.gif',
'https://cdn.discordapp.com/attachments/1093230022413791413/1093238948823834655/g7.gif'
]


movie_dialouge =[
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400412754804776/1.-Samara-Simha-Reddy.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400525506089010/1-Legend.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400537690554429/2-Simha_1.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400545512927232/2-simha.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400548419584070/3.-Lengend.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400559958097970/4.-simha.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400564009816174/3-Narasimha-Naidu.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400568782930011/4-Legend.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400585841168494/5.-Neeku-bail-ippichindi.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400591935471726/5-Sarihadhu-lo.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400609408946216/6.-Nuvvu-bhayapedithe.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400623208202281/7.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400625888383027/6-Gautami-Putra.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400633899499560/7-Bobbili-Simham.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400641914818610/8.-Naku-emotions-Legend.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400657874137098/8-Rowdy-Inspector.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400667256803359/9.-Central-Legend.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400731052167258/9-Lion.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400731370917908/10-narasimha-naidu.jpg',
'https://cdn.discordapp.com/attachments/1093230085995253863/1093400731777769553/10-Veerabhadra..jpg'
]

slogans=[
'**Jublie hills Banjara hills Balayya kodithe hospital bills**',
'**Hyderabad secunderabad Balayya Babu zindabad**',
'**Ramudu beemudu ma Balayya Babu demudu**',
'**Oopu groupu Balayya Babu thopu**',
'**Varshakalam lo current kotha Ammaila gundello Balayya Babu motha**',
'**India ki pm modi industry ki Balayya Babu daddy**',
'**1234 Balayya babu never before**',
'**Maza frooti Balayya Babu naughty**',
'**Jiljil jiga ma Balayya Babu sega**',
'**Uppukaaram Balayya meda chaavadu ma mamakaram**',
'**Paina kinda oopu Balayya Babu thopu**',
'**Ayodhya lo Ramayya……Andhra lo Balayya**',
'**One two three…..Balayya babu mukhyamantri**',
'**1-2-3-4 Balayya never before**',
'**Ramudu- Bheemudu…….Balayya babu ma devudu**',
'**Akkada Balayya…… Ikkada Balayya**',
'**Aaha Balayya ….. ooho Balayya**',
'**Adigo Balayya..Idigo balayya**',
'**Coca-Cola Pepsi…Balayya Babu Sexy**',
'**Annam lo Perugu Ledhu Balayya Babu ki Thirugu Ledu**',
'**Palakura Pappu Balayya Babu Nippu**',
'**Hyderabad…Secunderabad… Balayyababu Zindabad**',
'**Pappu lo Popu Balayya Babu Thopu**',
'**Vadevadu Videvadu Ma Balayya Babu ki Addu Evadu**',
'**Jill Jill Jiga Maa Balayya Babu sega**',
'**Bike loan..Car loan Balayaa Babu Cyclone**',
'**Hero Honda Splendor Balayya Babu Thunder**',
'**Varshakalam lo Current Kotha Ammaila Gundello Balayya Babu Motha**',
'**Adavilo pudithe simham la puttali Maro janmantuunte balayya abhimanila puttali**',
'**Palakura Pappu balayya babu nippu**',
'**Big house small house balayya babu mansion House**',
'**Ballayya Babu meeda Prema chavaduu marokkare meda Prema puttadu**',
'**Arjuna palguna ma balayya babu dhi simha garjana**',
'**Memu thinedhi uppu karam balayya babu meedha chavadhu maku mamakaram**',
'**Ac Cooler – Balayya babu is ruler**',
'**Smoking is injurious – Balayya babu dangerous**',
'**Water quarter – balayya babu dictator**',
'**Intlo undi swimming pool..balayya vaade word bloody fool**',
'**Stethoscope tho vinte ochedi lab dubuuu Ma balayya tho petukunte avtharu gabbu gabbu**',
'**Migatha heros antha tuppu balayyababu nippu**',
'**Bongu Ringu Balayya Babu Kingu**',
'**AM PM balyyababu CM**',
'**Coco-cola Pepsi Balayya Babu Sexy**'
]

bye_list=['https://cdn.discordapp.com/attachments/1093409711686156319/1093410230668365874/balayya_bye.gif',
     'https://cdn.discordapp.com/attachments/1093409711686156319/1093410231020691547/balayya_selavu.gif',]

come_list=['https://cdn.discordapp.com/attachments/1093409739184021514/1093410277854294087/balayya_come_here.gif',
      'https://cdn.discordapp.com/attachments/1093409739184021514/1093410278202429451/balayya_horse.gif']

dance_list=['https://cdn.discordapp.com/attachments/1093409798927691796/1093410594880765952/balayya_konga.gif',
       'https://cdn.discordapp.com/attachments/1093409798927691796/1093410595220492328/balayya_moodswings.gif',
       'https://cdn.discordapp.com/attachments/1093409798927691796/1093410595577024532/balayya_natyam.gif',
       'https://cdn.discordapp.com/attachments/1093409798927691796/1093410595983867985/dance.gif',
       'https://cdn.discordapp.com/attachments/1093409798927691796/1093410596323594280/natyam.gif']

eat_list=['https://cdn.discordapp.com/attachments/1093409832645709899/1093410588320878642/balayya_eat.gif',
     'https://cdn.discordapp.com/attachments/1093409832645709899/1093410588958400522/eat_banana.gif']

entry_list=['https://cdn.discordapp.com/attachments/1093409849309679618/1093410622709977138/balayya_control.gif',
       'https://cdn.discordapp.com/attachments/1093409849309679618/1093410623066476584/balayya_entrance.gif',
       'https://cdn.discordapp.com/attachments/1093409849309679618/1093410623439773757/balayya_Im_back.gif',
       'https://cdn.discordapp.com/attachments/1093409849309679618/1093410623745970247/reyy.gif']

fight_list=['https://cdn.discordapp.com/attachments/1093409864597909564/1093410737214455908/balayya_footbrick.gif',
       'https://cdn.discordapp.com/attachments/1093409864597909564/1093410737533231134/balayya_giant.gif',
       'https://cdn.discordapp.com/attachments/1093409864597909564/1093410737902338068/balayya_go_away.gif',
       'https://cdn.discordapp.com/attachments/1093409864597909564/1093410738334334986/balayya_go_there.gif',
       'https://cdn.discordapp.com/attachments/1093409864597909564/1093410738837667931/balayya_jaffa.gif',
       'https://cdn.discordapp.com/attachments/1093409864597909564/1093410739441631262/balayya_kick.gif',
       'https://cdn.discordapp.com/attachments/1093409864597909564/1093410739886235658/balayya_kill.gif',
       'https://cdn.discordapp.com/attachments/1093409864597909564/1093410740267909140/balayya_narikesta.gif',
       'https://cdn.discordapp.com/attachments/1093409864597909564/1093410740846731356/balayya_neo.gif',
       'https://cdn.discordapp.com/attachments/1093409864597909564/1093410741329084416/balayya_pindesta.gif',
       'https://cdn.discordapp.com/attachments/1093409864597909564/1093410760580923442/balayya_rage.gif',
       'https://cdn.discordapp.com/attachments/1093409864597909564/1093410760950038578/balayya_shoot.gif',
       'https://cdn.discordapp.com/attachments/1093409864597909564/1093410761314926612/balayya_silent.gif',
       'https://cdn.discordapp.com/attachments/1093409864597909564/1093410761797287976/balayya_warning.gif',
       'https://cdn.discordapp.com/attachments/1093409864597909564/1093410762225094707/getout.gif',
       'https://cdn.discordapp.com/attachments/1093409864597909564/1093410762556440576/what.gif']

flirt_list=['https://cdn.discordapp.com/attachments/1093409901038010419/1093410856936681583/balayya_thoda.gif',
       'https://cdn.discordapp.com/attachments/1093409901038010419/1093410857251246122/Balayya_wheelie.gif',
       'https://cdn.discordapp.com/attachments/1093409901038010419/1093410857616146562/jai_balayya.gif',
       'https://cdn.discordapp.com/attachments/1093409901038010419/1093410857981063208/balayya_swag1.gif',
       'https://cdn.discordapp.com/attachments/1093409901038010419/1093410865186873354/balayya_bolo.gif',
       'https://cdn.discordapp.com/attachments/1093409901038010419/1093410865535004812/balayya_brush.gif',
       'https://cdn.discordapp.com/attachments/1093409901038010419/1093410865878929458/balayya_flirt.gif',
       'https://cdn.discordapp.com/attachments/1093409901038010419/1093410866256420904/balayya_like.gif',
       'https://cdn.discordapp.com/attachments/1093409901038010419/1093410866675855401/balayya_littlefinger.gif',
       'https://cdn.discordapp.com/attachments/1093409901038010419/1093410866990420048/balayya_meesam.gif',
       'https://cdn.discordapp.com/attachments/1093409901038010419/1093410867338551366/balayya_notty.gif',
       'https://cdn.discordapp.com/attachments/1093409901038010419/1093410867682488340/balayya_playboy.gif',
       'https://cdn.discordapp.com/attachments/1093409901038010419/1093410868038996008/balayya_rajini.gif',
       'https://cdn.discordapp.com/attachments/1093409901038010419/1093410868374544454/balayya_swag.gif']

night_list=['https://cdn.discordapp.com/attachments/1093409940162482236/1093410852130017290/balayya_GN.gif']

hi_list=['https://cdn.discordapp.com/attachments/1093409953932390410/1093410886594601010/balayya_hi_there.gif']

peace_list=['https://cdn.discordapp.com/attachments/1093409970202095707/1093410922413961267/balayya_peace.gif']

shock_list=['https://cdn.discordapp.com/attachments/1093410144701927435/1093410999031308319/balayya_feared.gif',
       'https://cdn.discordapp.com/attachments/1093410144701927435/1093410999522037780/balayya_shock.gif']

actions_list= [bye_list,come_list,dance_list,eat_list,entry_list,fight_list,flirt_list,night_list,hi_list,peace_list,shock_list]
