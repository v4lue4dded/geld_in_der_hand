
button = driver.find_element_by_css_selector('a.cmplazybtnlink.cmpboxbtn.cmpboxbtnyes')
button.location
button.click()
driver.execute_script("arguments[0].click();", button)

import re 

re.findall("button",driver.page_source)

re.search("berechnen",driver.page_source)


driver.page_source[26161-30:26170+30]

driver.page_source[2866-5:2872+5]


from selenium.webdriver.common.action_chains import ActionChains
ac = ActionChains(driver)
ac.move_to_element(button).move_by_offset(5, 5).click().perform()


driver.get_attribute('innerHTML')


# url = "https://www.hartz4.org/hartz-4-rechner/#Hartz-4-Rechner_Jetzt_Ansprueche_kostenlos_berechnen"


# button_cookies_akzeptieren = driver.find_element_by_css_selector('a.cmpboxbtn.cmpboxbtnyes.cmptxt_btn_yes')
# button_cookies_akzeptieren.click()

calculator_area = driver.find_element_by_class_name("calculator_area")

inputbox_kaltmiete = driver.find_element_by_name("kaltmiete")
inputbox_heizkosten = driver.find_element_by_name("heizkosten")
inputbox_bruttoeinkommen = driver.find_element_by_name("bruttoeinkommen")
inputbox_nettoeinkommen = driver.find_element_by_name("nettoeinkommen")
inputbox_nettoeinkommen = driver.find_element_by_name("nettoeinkommen")
inputbox_kaltmiete.clear()
inputbox_heizkosten.clear()
inputbox_bruttoeinkommen.clear()
inputbox_nettoeinkommen.clear()
inputbox_nettoeinkommen.clear()
inputbox_kaltmiete.send_keys(str(ag2_input_dict["kaltmiete"]).replace(".",","))
inputbox_heizkosten.send_keys(str(ag2_input_dict["heizkosten"]).replace(".",","))
inputbox_bruttoeinkommen.send_keys(str(ag2_input_dict["bruttoeinkommen"]).replace(".",","))
inputbox_nettoeinkommen.send_keys(str(ag2_input_dict["nettoeinkommen"]).replace(".",","))
inputbox_nettoeinkommen.send_keys(str(ag2_input_dict["nettoeinkommen"]).replace(".",","))
inputbox_mehrbedarf_alleinerziehend = driver.find_element_by_name("mehrbedarf_alleinerziehend")
inputbox_bedarf_lebenspartner = driver.find_element_by_name("bedarf_lebenspartner")
inputbox_bedarf_schwanger = driver.find_element_by_name("bedarf_schwanger")
inputbox_bedarf_spezielle_nahrungsmittel = driver.find_element_by_name("bedarf_spezielle_nahrungsmittel")
inputbox_bedarf_kind_1 = driver.find_element_by_name("bedarf_kind_1")
inputbox_bedarf_kind_2 = driver.find_element_by_name("bedarf_kind_2")
inputbox_bedarf_kind_3 = driver.find_element_by_name("bedarf_kind_3")
inputbox_bedarf_kind_4 = driver.find_element_by_name("bedarf_kind_4")
inputbox_bedarf_unterkunft = driver.find_element_by_name("bedarf_unterkunft")
inputbox_summe_gesamtbedarf = driver.find_element_by_name("summe_gesamtbedarf")
inputbox_netto_einkommen = driver.find_element_by_name("netto_einkommen")
inputbox_grundfreibetrag_insgesamt = driver.find_element_by_name("grundfreibetrag_insgesamt")
inputbox_arbeitslosen_geld = driver.find_element_by_name("arbeitslosen_geld")

bn_input_dict = {
# inputbox
"f_bruttolohn": 0,
"f_geld_werter_vorteil": 0,
"f_steuerfreibetrag": 0,
"f_private_kv": 0,
"f_KVZ": 0,

# inputlist
"f_abrechnungsjahr" : "2021",
"f_steuerklasse" : "Klasse 3",
"f_bundesland" : "Berlin",
"f_kinderfreibetrag" : "1.5",
"f_alter" : "30",
"f_krankenversicherung" : "privatversichert",
"f_rentenversicherung" : "nicht gesetzlich versichert",
"f_arbeitslosenversicherung" : "gesetzlich pflichtversichert",

# radio
"f_abrechnungszeitraum": "Jahr",
"f_kirche": "nein",
"f_kinder": "nein",
"f_arbeitgeberzuschuss_pkv": "nein",
}


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)


# bn_input_dict = {
# "f_bruttolohn"               : f_bruttolohn,
# "f_abrechnungszeitraum"      : f_abrechnungszeitraum,
# "f_geld_werter_vorteil"      : f_geld_werter_vorteil,
# "f_abrechnungsjahr"          : f_abrechnungsjahr,
# "f_steuerfreibetrag"         : f_steuerfreibetrag,
# "f_steuerklasse"             : f_steuerklasse,
# "f_kirche"                   : f_kirche,
# "f_bundesland"               : f_bundesland,
# "f_kinder"                   : f_kinder,
# "f_kinderfreibetrag"         : f_kinderfreibetrag,
# "f_alter"                    : f_alter,
# "f_krankenversicherung"      : f_krankenversicherung,
# "f_KVZ"                      : f_KVZ,
# "f_private_kv"               : f_private_kv,
# "f_arbeitgeberzuschuss_pkv"  : f_arbeitgeberzuschuss_pkv,
# "f_rentenversicherung"       : f_rentenversicherung,
# "f_arbeitslosenversicherung" : f_arbeitslosenversicherung,
# }

url = "https://www.brutto-netto-rechner.eu/partner/rechner/partner_bnr.php"
driver.get(url)


# input: ---------------------------------------------------------------------------------------------------

list_element_inputs = [
    "f_abrechnungsjahr",
    "f_steuerklasse",
    "f_bundesland",
    "f_kinderfreibetrag",
    "f_alter",
    "f_krankenversicherung",
    "f_rentenversicherung",
    "f_arbeitslosenversicherung",
]

for li_i in list_element_inputs:
    inputlist = driver.find_element(by=By.NAME, value=li_i)
    option_visible_text_list = [i.text for i in inputlist.find_elements_by_tag_name("option")]
    assert bn_input_dict[li_i] in option_visible_text_list, f"Error: {bn_input_dict[li_i]} for {li_i} isn't one of the following options: {str(option_visible_text_list)}"
    select = Select(inputlist)
    select.select_by_visible_text(bn_input_dict[li_i])

radio_inputs = [
    "f_abrechnungszeitraum",
    "f_kirche",
    "f_kinder",
    "f_arbeitgeberzuschuss_pkv",
]

for ri_i in radio_inputs:
    if (ri_i in ["f_abrechnungszeitraum", "f_kirche", "f_kinder"]
    or bn_input_dict["f_krankenversicherung"] == "privatversichert" and ri_i == "f_arbeitgeberzuschuss_pkv" ):
        radio = driver.find_element_by_xpath(f"//input[@type='radio' and @name='{ri_i}' and @value='{bn_input_dict[ri_i].lower()}']")
        radio.click()

numeric_inputs = [
"f_bruttolohn",
"f_geld_werter_vorteil",
"f_steuerfreibetrag",
"f_private_kv",
"f_KVZ",    
]


for ni_i in numeric_inputs:
    if (ni_i in ["f_bruttolohn", "f_geld_werter_vorteil", "f_steuerfreibetrag"]
    or bn_input_dict["f_krankenversicherung"] == "gesetzlich pflichtversichert" and ni_i == "f_KVZ"        
    or bn_input_dict["f_krankenversicherung"] == "privatversichert"             and ni_i == "f_private_kv" ):
        assert isinstance(bn_input_dict[ni_i], (int, float)), f"Error: {ni_i} is not of type int or float"
        assert bn_input_dict[ni_i] >= 0, f"Error: {ni_i} is not >= 0"
        inputbox = driver.find_element(by=By.NAME, value=ni_i)
        inputbox.clear()
        inputbox.send_keys(str(bn_input_dict[ni_i]))


# calculate: -----------------------------------------------------------------------------------------------
button_berechnen = driver.find_element_by_class_name("button")
button_berechnen.click()

# output: --------------------------------------------------------------------------------------------------

bn_output_dict = dict()
for no_i in numeric_outputs:
    inputbox = driver.find_element_by_name(no_i)
    bn_output_dict[no_i] = float(inputbox.get_attribute('value').replace(".","").replace(",","."))


import pandas as pd

# locate the table element
table = driver.find_element_by_class_name("rechner")

# extract the data from the table
data = []
for row in table.find_elements_by_xpath(".//tr"):
    data.append([cell.text for cell in row.find_elements_by_xpath(".//td")])

response_dict = dict()
for row_i in data:
    if len(row_i) == 3 and ":" in row_i[0]:
        item_name_raw = row_i[0]
        item_name = item_name_raw.strip().replace(":","").replace(" ","_").lower()
        monthly_value_raw = row_i[2]
        if "€" in monthly_value_raw:
            monthly_value = float(monthly_value_raw.replace("€","").replace(".","").replace(",",".")) 
        else:
            monthly_value = monthly_value_raw.strip()
        response_dict[item_name] = monthly_value



############################ get image of current stage #########################################
from PIL import Image
from io import BytesIO
png = driver.get_screenshot_as_png()
im = Image.open(BytesIO(png)) 
im
