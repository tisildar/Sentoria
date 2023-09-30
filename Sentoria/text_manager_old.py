
class General():

    def space():
        print(' ')

    def wrong_choice():
        General.space()
        print("Geçersiz seçenek. Lütfen seçmek istediğiniz seçeneğin solundaki rakamı yazıp enter tuşuna basınız.")
        General.space()
    
    def wrong_name():
        General.space()
        print("Hatalı bir isim girdiniz. Sembol veya rakam kullanmayınız.")
        General.space()

    def increase_stat_text(stat):
        General.space()
        print(f"{stat} BONUSUN 1 ARTTI")
        General.space()

    def deccrease_stat_text(stat):
        General.space()
        print(f"{stat} BONUSUN 1 AZALDI")
        General.space()

class CharactherCreation():
    def enterance():
        General.space()
        print('Ardfast şehrinin garnizonundasın. Buraya orduya katılmak için geldin. Karşında orduya alımdan sorumlu 3 asker var. Ortaki ağır zırhlı asker "İsmin ?" diye sordu ')

    def choose_possitive_ability_text(name):
        General.space()
        print(f'Pekala {name}. Yetenekli olduğun konu nedir ? Seni bir mücadelede ön plana çıkaran özelliğin nedir ?')

    def choose_possitive_ability_options_text():
        print('1- Gücüm ve kılıç ustalığım\n2- Çevikliğim ve Ok ile yay kullanma becerim\n3- Zekam ve büyü gücüm.')
        General.space()

    def choosing_strength_path_text(name):
        General.increase_stat_text('KUVVET')
        print("Sen cevabını verdikten sonra ağır zırhlı askerin dikkatini çektiğini fark ettin. Apğır zırhlı asker yüksek bir ses ile.")
        print(f'- Hah karmaşık sorunları basit yolla çözenlerdensin demek. Ben 2. Kaptan Broung. Bugünden itibaren benim emrim altında olacaksın. Peki söyle bana {name} en uzak olduğun alan nedir ?')
        General.space()

    def choose_possitive_ability_dexterity_text():
        General.increase_stat_text('ÇEVİKLİK')
        print("Cevabını ile ağır zırhlı askerin sağında sırtın büyükçe bir yay olan asker seni süzdü ve sana yaklaşıp sakince etrafında yürüdü. Ardından alaycı bir ses tonu ile")

    def choosing_dexterity_path_passive_check_fail_text(name):
        General.space()
        print("- Hmm demek becerikli biri olduğunu idda ediyorsun. Ben Eclana krallığının istihbarat biriminin yardımcı kaptanı Calude. Bu arada bunu düşünrmüşsün.")
        print("Calude'un elindekine baktığın az önce belinde olduğuna emin olduğun altın kesesini görmektesin. Calude muzipce gülümsedi ve altın keseni sana geri verdi")
        print(f'- Özür dilerim sadece becerikli olduğun kadar dikkatlimisin diye test etmek istemiştim zamanla alışırsın. Peki söyle bana {name} en uzak olduğun alan nedir ?')
        General.space()
            
    def choosing_dexterity_path_passive_check_success_text(name):
        print("- Hmm demek becerikli biri olduğunu idda ediyorsun. Ben Eclana krallığının istihbarat biriminin yardımcı kaptanı Calude.")
        print("Calude konuşurken belindeki altın kesende bir el hissettin. Elini beline götürerek sakince elin sahibine döndüğünde Claude'un seni taktir eden bakışları ile karşılaştın")
        print(f'- Oooo becerikli olduğun kadar dikkatlisinde bunu sevdim. Peki söyle bana {name} en uzak olduğun alan nedir ?')
        General.space()

    def choosing_intelligince_path_text(name):
        General.increase_stat_text('BÜYÜ')
        print("Cevabın ile birlikte ağır zırhlı askerin solunda bulunan cılız adamın gözlerinde mavi bir parıltı ile sana baktığını gördün.")
        print(f'- Demek mistik sanatların yolunda ilerleyen biri. Ben Ardfast şehrinin büyü akademisi konsey üyesi Awramor. Tanıştığımıza memnun oldum. Bu noktadan sonra akademinin emri altındasın. Peki söyle bana {name} Büyü ustalığında ki becerini hangi konuda ki beceriksizliğine borçlusun ?')
        General.space()

    def choose_intelligince_negative_ability_text():
        print('1- Kılıçlar ve silahlardan pek anlamıyorum.\n2- Pek el becerisi olan biri değilim')
        General.space()

    def choosing_intelligince_negative_ability_strength_text():
        General.deccrease_stat_text('KUVVET')
        print("Awramor: Pekala seni kaba kuvvet gereken işlerden uzak tutmak için elimden geleni yapacam.")
        General.space()

    def choosing_intelligince_negative_ability_dexterity_text():
        General.deccrease_stat_text('ÇEVİKLİK')
        print("Awramor: El becerisi isteyen görevlere denk gelmemen için elimden geleni yapacam.")
        General.space()

    def choose_strength_negative_ability_text():
        print('1- Pek el becerisi olan biri değilim.\n2- Mistik sanatların pek kafamın bastığı bir alan olduğunu söyleyemem')

    def choose_dexterity_negative_ability_text():
        print('1- Pek el becerisi olan biri değilim.\n2- Mistik sanatların pek kafamın bastığı bir alan olduğunu söyleyemem')

