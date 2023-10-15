import time
from bs4 import BeautifulSoup
import requests as req

t_start = time.ctime().split()[-2].split(':')[1],time.ctime().split()[-2].split(':')[2]
t_next = time.ctime().split()[-2].split(':')[1],time.ctime().split()[-2].split(':')[2]
#выведет первые 3 буквы дня недели
t = time.ctime().split()[0]
t = time.ctime()[0]
t = time.ctime().split()[0]

url = 'https://goodlooker.ru/kak-pohudet-za-nedelju.html'
r = req.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
headers = soup.find_all('h3')

Sunday_slimming = []
Monday_slimming = []
Tuesday_slimming = []
Wednesday_slimming = []
Thursday_slimming = []
Friday_slimming = []
Saturday_slimming = []
cur = 0
cycle = 0
for header in headers:
    if cycle == 0 :
        Sunday_slimming.append(header.text)
        cur +=1
    if cycle == 1 :
        Monday_slimming.append(header.text)
        cur +=1
    if cycle == 2 :
        Tuesday_slimming.append(header.text)
        cur +=1
    if cycle == 3 :
        Wednesday_slimming.append(header.text)
        cur +=1
    if cycle == 4 :
        Thursday_slimming.append(header.text)
        cur +=1
    if cycle == 5 :
        Friday_slimming.append(header.text)
        cur +=1
    if cycle == 6 :
        Saturday_slimming.append(header.text)
        cur +=1

    if cur == 10:
        cur = 0
        cycle += 1

Sunday_g = []
Monday_g= []
Tuesday_g = []
Wednesday_g = []
Thursday_g = []
Friday_g = []
Saturday_g= []
cur_g = 0
cycle_g = 0
images = soup.find_all('img')

for image in images:
    image_url = image['src']
    if image_url.endswith('.gif'):
        file_response = req.get(image_url)
        # print (image_url)
        if cycle_g == 0 :
            Sunday_g.append(image_url)
            cur_g +=1
        if cycle_g == 1 :
            Monday_g.append(image_url)
            cur_g +=1
        if cycle_g == 2 :
            Tuesday_g.append(image_url)
            cur_g +=1
        if cycle_g == 3 :
            Wednesday_g.append(image_url)
            cur_g +=1
        if cycle_g == 4 :
            Thursday_g.append(image_url)
            cur_g +=1
        if cycle_g == 5 :
            Friday_g.append(image_url)
            cur_g +=1
        if cycle_g == 6 :
            Saturday_g.append(image_url)
            cur_g +=1

        if cur_g == 10:
            cur_g = 0
            cycle_g += 1
Monday_g = ['https://goodlooker.ru/wp-content/uploads/2021/05/Shag_v_storonu_razgibanie_ruk.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/04/Sumo_prised_ruki_vverh.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/05/Podtyagivaniya_kolenej_k_grudi_kardio.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/03/Shag_nazad_podemy_ruk_dva_vida.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/05/Planka_koleno_vniz.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/03/Plovec_sognutie_ruki.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/05/Vypady_nazad_v_poluprisede.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/05/Udari_vpered_s_shagom.gif',
            'https://goodlooker.ru/wp-content/uploads/2020/12/Twist_ugolok_nogi_sognuti_2.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/01/Mostik_mah_sognutoj_nogoj_vverh.gif']

Tuesday_g = ['https://goodlooker.ru/wp-content/uploads/2021/05/Legkie_udary_vpered_s_boksom.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/04/Prised_koleno_vverh.gif',
            'https://goodlooker.ru/wp-content/uploads/2020/12/Planka_pauk_bystro.gif',
            'https://goodlooker.ru/wp-content/uploads/2020/08/Zhim_rukami_vverh_sidya_na_kolenyah.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/04/Iz_priseda_v_glubokij_vypad.gif',
            'https://goodlooker.ru/wp-content/uploads/2020/12/Mah_sognutoj_nogoj_lezha_na_zhivote.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/05/Prisedanie_s_shagom_razvedenie_ruk.gif',
            'https://goodlooker.ru/wp-content/uploads/2020/04/Vypad_otvedenie_nogi_nazad_2.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/05/Skruchivanie_vityagivanie_ruk_tri_raza.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/05/Mah_nogoj_vverh_vbok.gif']

Wednesday_g = ['https://goodlooker.ru/wp-content/uploads/2021/05/Razvedenie_ruk_shag_nazad.gif',
                'https://goodlooker.ru/wp-content/uploads/2021/05/Sumo_prised_pulse.gif',
                'https://goodlooker.ru/wp-content/uploads/2021/04/Skruchivanie_koleno_lokot_cardio.gif',
                'https://goodlooker.ru/wp-content/uploads/2021/05/Otzhimaniya_ot_kolen_podem_loktej.gif',
                'https://goodlooker.ru/wp-content/uploads/2020/06/Ohotnichya_sobaka.gif',
                'https://goodlooker.ru/wp-content/uploads/2020/12/Bokovaya_planka_skruchivanie_s_rukoj.gif',
                'https://goodlooker.ru/wp-content/uploads/2021/02/Vypady_vpered_malaja_amplituda_cardio.gif',
                'https://goodlooker.ru/wp-content/uploads/2020/12/Poperemennye_mahi_v_storonu_cardio.gif',
                'https://goodlooker.ru/wp-content/uploads/2021/05/Sit_up_ruki_vpered.gif',
                'https://goodlooker.ru/wp-content/uploads/2021/05/Mah_nogoj_vpered_nazad_vverh_vniz.gif']

Thursday_g = ['https://goodlooker.ru/wp-content/uploads/2021/04/Zahlesty_goleni_jack.gif',
                'https://goodlooker.ru/wp-content/uploads/2020/11/Prised_uzkij_shirokij.gif',
                'https://goodlooker.ru/wp-content/uploads/2021/04/Podtyagivanie_kolena_s_shagom_nazad.gif',
                'https://goodlooker.ru/wp-content/uploads/2021/03/Podem_nog_na_chetverenkah.gif',
                'https://goodlooker.ru/wp-content/uploads/2021/05/Hyperextensia_razvedenie_ruk_nog.gif',
                'https://goodlooker.ru/wp-content/uploads/2020/11/Iz_planki_v_sobaku_mordoj_vniz_v_alpinist.gif',
                'https://goodlooker.ru/wp-content/uploads/2021/05/Vypady_nazad_koleo_lokot.gif',
                'https://goodlooker.ru/wp-content/uploads/2021/03/Perepryzhki_v_polurisede_medlenno.gif',
                'https://goodlooker.ru/wp-content/uploads/2021/05/Dvojnie_skruchivanie_naiskosok.gif',
                'https://goodlooker.ru/wp-content/uploads/2021/03/Nozhnici_razvedenie_nog.gif']

Friday_g = ['https://goodlooker.ru/wp-content/uploads/2021/03/Podemу_kolen_boksirovanie.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/05/Shirokij_prised_kasanie_stopy.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/05/Lastochka_ruki_vpered.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/02/Planka_vityagivanie_ruki_vpered-1.gif',
            'https://goodlooker.ru/wp-content/uploads/2020/08/Razvedenie_loktej_sidya_na_kolenyah.gif',
            'https://goodlooker.ru/wp-content/uploads/2020/08/Superman.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/03/Bokovoj_vypad_new.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/05/Koleno_lokot_stopa_2.gif',
            'https://goodlooker.ru/wp-content/uploads/2021/05/Skruchivanie_ruki_mezhdu_nog.gif',
            'https://goodlooker.ru/wp-content/uploads/2020/11/Mah_nogoj_vverh_pryamoj_nogoj.gif']

weekdays_slimming = {'Mon': [Monday_slimming, Monday_g],
                     'Tue': [Tuesday_slimming, Tuesday_g],
                     'Wed': [Wednesday_slimming,Wednesday_g],
                     'Thu': [Thursday_slimming,Thursday_g],
                     'Fri': [Friday_slimming,Friday_g],
                     'Sat': [Saturday_slimming,Saturday_g],
                     'Sun': [Sunday_slimming,Sunday_g]}

# weekdays_power = {'Mon': Monday_power,
#                      'Tue': Tuesday_power,
#                      'Wed': Wednesday_power,
#                      'Thu': Thursday_power,
#                      'Fri': Friday_power,
#                      'Sat': Saturday_power,
#                      'Sun': Sunday_power}
print(weekdays_slimming[t])