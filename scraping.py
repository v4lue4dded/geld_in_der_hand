from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=chrome_options)

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

    return ag2_output_dict

get_ag2_details(kind_1="24",kind_2=5)

############################ get image of current stage #########################################
from PIL import Image
from io import BytesIO
png = driver.get_screenshot_as_png()
im = Image.open(BytesIO(png)) 
im
