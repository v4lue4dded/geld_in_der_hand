
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
