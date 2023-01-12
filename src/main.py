from scraping_functions import get_ag2_details, get_bn_details




bn_base_dict = {
    "f_abrechnungszeitraum":"Monat",
    "f_steuerklasse":"Klasse 1",
    "f_kirche":"ja",
    "f_bundesland":"Baden-Württemberg",
    "f_kinder":"nein",
    "f_kinderfreibetrag":"0",
    "f_alter":"30",
    "f_krankenversicherung":"gesetzlich pflichtversichert",
    "f_KVZ":1.6,
    "f_rentenversicherung":"gesetzlich pflichtversichert",
    "f_arbeitslosenversicherung":"gesetzlich pflichtversichert",
    "return_monthly":True,
}

ag2_base_dict = {
    "kaltmiete"               : 400,
    "heizkosten"              : 100,
    }

data_list = []
for i_brutto_lohn in range(0,100001,100):
    print(i_brutto_lohn)
    bn_input_dict, bn_output_dict = get_bn_details(**bn_base_dict, f_bruttolohn =i_brutto_lohn)
    ag2_brutto_netto_dict = {
        "bruttoeinkommen": bn_output_dict["ihr_bruttoeinkommen"],
        "nettoeinkommen": bn_output_dict["ihr_nettoeinkommen"],
    }
    ag2_input_dict, ag2_output_dict = get_ag2_details(**ag2_base_dict, **ag2_brutto_netto_dict)

    collecting_dict = {**bn_input_dict, **bn_output_dict, **ag2_input_dict, **ag2_output_dict}

    data_list.append(collecting_dict)
    