from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# ag2 calculator:
def get_ag2_details(
    partner_gemeinschaft=False,
    schwangerschaft=False,
    spezielle_nahrungsmittel=False,
    kind_1="---",
    kind_2="---",
    kind_3="---",
    kind_4="---",
    kindergeld=0.0,
    kaltmiete=0.0,
    heizkosten=0.0,
    warmwasser=False,
    bruttoeinkommen=0.0,
    nettoeinkommen=0.0,
    bruttoeinkommen_partner=0.0,
    nettoeinkommen_partner=0.0,
):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    ag2_input_dict = {
    "partner_gemeinschaft"    : partner_gemeinschaft,
    "schwangerschaft"         : schwangerschaft,
    "spezielle_nahrungsmittel": spezielle_nahrungsmittel,
    "kind_1"                  : kind_1,
    "kind_2"                  : kind_2,
    "kind_3"                  : kind_3,
    "kind_4"                  : kind_4,
    "kindergeld"              : kindergeld,
    "kaltmiete"               : kaltmiete,
    "heizkosten"              : heizkosten,
    "warmwasser"              : warmwasser,
    "bruttoeinkommen"         : bruttoeinkommen,
    "nettoeinkommen"          : nettoeinkommen,
    "bruttoeinkommen_partner" : bruttoeinkommen_partner,
    "nettoeinkommen_partner"  : nettoeinkommen_partner,
    }

    url = "https://www.brutto-netto-rechner.eu/partner/rechner/partner_arbeitslosengeld_2_rechner.php"
    driver.get(url)


    # input: ---------------------------------------------------------------------------------------------------
    boolean_inputs = [
        "partner_gemeinschaft",
        "schwangerschaft",
        "spezielle_nahrungsmittel",
        "warmwasser",
    ]

    for bi_i in boolean_inputs:
        assert isinstance(ag2_input_dict[bi_i], bool), f"Error: {bi_i} is not of type bool"
        checkbox = driver.find_element(by=By.NAME, value=bi_i)
        # set checkbox to negative first no matter how it was encountered (probably already negative)
        if checkbox.is_selected():
            checkbox.click()
        # set checkbox to value of bi_i
        if ag2_input_dict[bi_i]:
            checkbox.click()

    list_element_inputs = [
        "kind_1",
        "kind_2",
        "kind_3",
        "kind_4",
    ]

    for li_i in list_element_inputs:
        if ag2_input_dict[li_i] == "---":
            li_i_value = ag2_input_dict[li_i]    
        else:
            if isinstance(ag2_input_dict[li_i], int):
                assert 1 <= ag2_input_dict[li_i] and ag2_input_dict[li_i] <= 24, f'Error: {li_i} is not between 1 and 24'
                li_i_value = str(ag2_input_dict[li_i])
            else:
                assert isinstance(ag2_input_dict[li_i], str), f'Error: {li_i} is not an int, nor a string'
                assert 1 <= int(ag2_input_dict[li_i]) and int(ag2_input_dict[li_i]) <= 24, f'Error: {li_i} is not between 1 and 24'
                li_i_value = ag2_input_dict[li_i]
        inputlist = driver.find_element(by=By.NAME, value=li_i)
        select = Select(inputlist)
        select.select_by_visible_text(li_i_value)

    numeric_inputs_base = [
    "kaltmiete",
    "heizkosten",
    "bruttoeinkommen",
    "nettoeinkommen",
    "kindergeld",    
    ]
    numeric_inputs_partner = [
        "bruttoeinkommen_partner",
        "nettoeinkommen_partner",
    ]

    if ag2_input_dict["partner_gemeinschaft"]:
        numeric_inputs = numeric_inputs_base + numeric_inputs_partner
    else:
        numeric_inputs = numeric_inputs_base

    for ni_i in numeric_inputs:
        assert isinstance(ag2_input_dict[ni_i], (int, float)), f"Error: {ni_i} is not of type int or float"
        assert ag2_input_dict[ni_i] >= 0, f"Error: {ni_i} is not >= 0"
        inputbox = driver.find_element(by=By.NAME, value=ni_i)
        inputbox.clear()
        inputbox.send_keys(str(ag2_input_dict[ni_i]).replace(".",","))



    # calculate: -----------------------------------------------------------------------------------------------
    button_berechnen = driver.find_element_by_name("berechnen")
    button_berechnen.click()

    # output: --------------------------------------------------------------------------------------------------
    numeric_outputs = [
    "bedarf_antragsteller",
    "mehrbedarf_alleinerziehend",
    "bedarf_lebenspartner",
    "bedarf_schwanger",
    "bedarf_spezielle_nahrungsmittel",    
    "bedarf_kind_1",    
    "bedarf_kind_2",    
    "bedarf_kind_3",    
    "bedarf_kind_4",    
    "bedarf_unterkunft",    
    "summe_gesamtbedarf",    
    "netto_einkommen",    
    "grundfreibetrag_insgesamt",    
    "arbeitslosen_geld",    
    ]

    ag2_output_dict = dict()
    for no_i in numeric_outputs:
        inputbox = driver.find_element_by_name(no_i)
        ag2_output_dict[no_i] = float(inputbox.get_attribute('value').replace(".","").replace(",","."))

    return ag2_input_dict, ag2_output_dict

# brutto_netto calculator:

def get_bn_details(
    f_bruttolohn=3000,
    f_abrechnungszeitraum="Monat",
    f_geld_werter_vorteil=0,
    f_abrechnungsjahr="2023",
    f_steuerfreibetrag=0,
    f_steuerklasse="Klasse 3",
    f_kirche="ja",
    f_bundesland="Baden-Württemberg",
    f_kinder="nein",
    f_kinderfreibetrag="0",
    f_alter="25",
    f_krankenversicherung="gesetzlich pflichtversichert",
    f_KVZ=1.6,
    f_private_kv=0,
    f_arbeitgeberzuschuss_pkv="ja",
    f_rentenversicherung="gesetzlich pflichtversichert",
    f_arbeitslosenversicherung="gesetzlich pflichtversichert",
    return_monthly=True,
):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)


    bn_input_dict = {
    "f_bruttolohn"               : f_bruttolohn,
    "f_abrechnungszeitraum"      : f_abrechnungszeitraum,
    "f_geld_werter_vorteil"      : f_geld_werter_vorteil,
    "f_abrechnungsjahr"          : f_abrechnungsjahr,
    "f_steuerfreibetrag"         : f_steuerfreibetrag,
    "f_steuerklasse"             : f_steuerklasse,
    "f_kirche"                   : f_kirche,
    "f_bundesland"               : f_bundesland,
    "f_kinder"                   : f_kinder,
    "f_kinderfreibetrag"         : f_kinderfreibetrag,
    "f_alter"                    : f_alter,
    "f_krankenversicherung"      : f_krankenversicherung,
    "f_KVZ"                      : f_KVZ,
    "f_private_kv"               : f_private_kv,
    "f_arbeitgeberzuschuss_pkv"  : f_arbeitgeberzuschuss_pkv,
    "f_rentenversicherung"       : f_rentenversicherung,
    "f_arbeitslosenversicherung" : f_arbeitslosenversicherung,
    "return_monthly"             : return_monthly,
    }

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
        option_visible_text_list = [i.text for i in inputlist.find_elements(by=By.TAG_NAME, value="option")]
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
            radio = driver.find_element(by=By.XPATH, value=f"//input[@type='radio' and @name='{ri_i}' and @value='{bn_input_dict[ri_i].lower()}']")
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

    # locate the table element
    table = driver.find_element_by_class_name("rechner")

    # extract the data from the table
    data = []
    for row in table.find_elements(by=By.XPATH, value=".//tr"):
        data.append([cell.text for cell in row.find_elements(by=By.XPATH, value=".//td")])

    bn_output_dict = dict() 
    for row_i in data:
        if len(row_i) == 3 and ":" in row_i[0]:
            item_name_raw = row_i[0]
            item_name = item_name_raw.strip().replace(":","").replace(" ","_").lower()
            if bn_input_dict["return_monthly"]:
                value_raw = row_i[1]
            else:
                value_raw = row_i[2]
            if "€" in value_raw:
                value = float(value_raw.replace("€","").replace(".","").replace(",",".")) 
            else:
                value = value_raw.strip()
            bn_output_dict[item_name] = value

    return bn_input_dict, bn_output_dict


# ############################ get image of current stage #########################################
# from PIL import Image
# from io import BytesIO
# png = driver.get_screenshot_as_png()
# im = Image.open(BytesIO(png)) 
# im
