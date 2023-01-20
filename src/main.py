import pandas as pd
import numpy as np
from scraping_functions import get_ag2_details, get_bn_details
from itertools import chain
from matplotlib import pyplot as plt
plt.rcParams["figure.dpi"] = 1080


pd.set_option("display.max_rows"   ,  50)
pd.set_option("display.max_columns",  500)
pd.set_option("display.width"      , 1000)



info_dict_list = [
# Paar mit 2 Kindern
{
"name" : "Paar mit 2 Kindern",
"bn_base_dict" : {
    "f_abrechnungszeitraum":"Monat",
    "f_geld_werter_vorteil":0,
    "f_steuerfreibetrag":0,
    "f_abrechnungsjahr":"2022",
    "f_steuerklasse":"Klasse 3",
    "f_kirche":"ja",
    "f_bundesland":"Nordrhein-Westfalen",
    "f_kinder":"ja",
    "f_kinderfreibetrag":"2",
    "f_alter":"30",
    "f_krankenversicherung":"gesetzlich pflichtversichert",
    "f_KVZ":1.6,
    "f_rentenversicherung":"gesetzlich pflichtversichert",
    "f_arbeitslosenversicherung":"gesetzlich pflichtversichert",
    "return_monthly":True,
},
"ag2_base_dict" : {
    "partner_gemeinschaft":True,
    "schwangerschaft":False,
    "spezielle_nahrungsmittel":False,
    "kind_1":6,
    "kind_2":3,
    "kind_3":"---",
    "kind_4":"---",
    "kindergeld":219+219,
    "kaltmiete": 600,
    "heizkosten": 100,
    "warmwasser":False,
    "bruttoeinkommen_partner":0.0,
    "nettoeinkommen_partner":0.0,
    }
},
# Einzelperson
{
"name" : "Einzelperson",
"bn_base_dict" : {
    "f_abrechnungszeitraum":"Monat",
    "f_geld_werter_vorteil":0,
    "f_steuerfreibetrag":0,
    "f_abrechnungsjahr":"2022",
    "f_steuerklasse":"Klasse 1",
    "f_kirche":"ja",
    "f_bundesland":"Nordrhein-Westfalen",
    "f_kinder":"nein",
    "f_kinderfreibetrag":"0",
    "f_alter":"30",
    "f_krankenversicherung":"gesetzlich pflichtversichert",
    "f_KVZ":1.6,
    "f_rentenversicherung":"gesetzlich pflichtversichert",
    "f_arbeitslosenversicherung":"gesetzlich pflichtversichert",
    "return_monthly":True
},
"ag2_base_dict" : {
    "partner_gemeinschaft":False,
    "schwangerschaft":False,
    "spezielle_nahrungsmittel":False,
    "kind_1":"---",
    "kind_2":"---",
    "kind_3":"---",
    "kind_4":"---",
    "kindergeld":0.0,
    "kaltmiete": 400,
    "heizkosten": 100,
    "warmwasser":False,
    "bruttoeinkommen_partner":0.0,
    "nettoeinkommen_partner":0.0,
    }
},
]

for info_dict in info_dict_list:
    name=info_dict["name"]
    bn_base_dict=info_dict["bn_base_dict"]
    ag2_base_dict=info_dict["ag2_base_dict"]
    print(name)

    brutto_range = chain(
        range(0,14010,10),
    )

    brutto_range = chain(
        range(0,200,20),
        range(200,1000,50),
        range(1000,14000, 100),
    )


    data_list = []
    for i_brutto_lohn in brutto_range:
        print(i_brutto_lohn)
        bn_input_dict, bn_output_dict = get_bn_details(**bn_base_dict, f_bruttolohn =i_brutto_lohn)
        ag2_brutto_netto_dict = {
            "bruttoeinkommen": bn_output_dict["ihr_bruttoeinkommen"],
            "nettoeinkommen": bn_output_dict["ihr_nettoeinkommen"],
        }
        ag2_input_dict, ag2_output_dict = get_ag2_details(**ag2_base_dict, **ag2_brutto_netto_dict)

        collecting_dict = {
            **{"bn_in__" + k: v for k, v in bn_input_dict.items()}, 
            **{"bn_out__" + k: v for k, v in bn_output_dict.items()}, 
            **{"ag2_in__" + k: v for k, v in ag2_input_dict.items()}, 
            **{"ag2_out__" + k: v for k, v in ag2_output_dict.items()},
            }


        data_list.append(collecting_dict)



    df_complete = pd.DataFrame(data_list)

    rename_dict = {
    "ag2_in__kindergeld": "kindergeld",
    "ag2_out__arbeitslosen_geld": "arbeitslosen_geld",
    "bn_in__f_bruttolohn": "bruttolohn",
    "bn_out__ihr_nettoeinkommen": "nettolohn",
    "bn_out__lohnsteuer": "lohnsteuer",
    "bn_out__kirchensteuer": "kirchensteuer",
    "bn_out__solidaritätszuschlag": "solidaritätszuschlag",
    "bn_out__rentenversicherung": "rentenversicherung",
    "bn_out__arbeitslosenversicherung": "arbeitslosenversicherung",
    "bn_out__krankenversicherung": "krankenversicherung",
    "bn_out__pflegeversicherung": "pflegeversicherung",
    }

    df_vis_basis = df_complete.loc[:, rename_dict.keys()].rename(columns=rename_dict)

    df_vis_total = (
        df_vis_basis.assign(
            Kindergeld               = lambda x: x.kindergeld,
            Bruttomonatslohn         = lambda x: x.bruttolohn,
            Nettolohn                = lambda x: x.nettolohn,
            Arbeitslosen_Geld        = lambda x: x.arbeitslosen_geld,
            Lohnsteuer               = lambda x: x.lohnsteuer,
            Kirchensteuer            = lambda x: x.kirchensteuer,
            Solidaritätszuschlag     = lambda x: x.solidaritätszuschlag,
            Rentenversicherung       = lambda x: x.rentenversicherung,
            Arbeitslosenversicherung = lambda x: x.arbeitslosenversicherung,
            Krankenversicherung      = lambda x: x.krankenversicherung,
            Pflegeversicherung       = lambda x: x.pflegeversicherung,
        )
        .set_index("Bruttomonatslohn")
        .round(2)
        .loc[:,
           ["Kindergeld", "Nettolohn","Arbeitslosen_Geld","Lohnsteuer","Kirchensteuer","Solidaritätszuschlag","Rentenversicherung","Arbeitslosenversicherung","Krankenversicherung","Pflegeversicherung",
        ]]
    )

    for i_col in df_vis_basis.columns:
        df_vis_basis[f"diff__{i_col}"] = df_vis_basis[i_col] - df_vis_basis.sort_values(by=['bruttolohn'], ascending=True)[i_col].shift(1).fillna(0)

    df_vis_diff = (
        df_vis_basis
        .loc[1:,lambda x: ["bruttolohn"] + [i for i in x.columns if i[:6]=="diff__"] ]
        .assign(
            Kindergeld                                        = lambda x:  x.diff__kindergeld,
            Bruttomonatslohn                                  = lambda x:  x.bruttolohn,
            Arbeitslosen_Geld_Reduktion                       = lambda x:(-x.diff__arbeitslosen_geld).clip(lower=0).clip(upper=x.diff__nettolohn),
            Arbeitslosen_Geld_Zuwachs                         = lambda x:  x.diff__arbeitslosen_geld.clip(lower=0),
            Nettolohn_minus_Arbeitslosen_Geld_Reduktion       = lambda x:  (x.diff__nettolohn - x.Arbeitslosen_Geld_Reduktion).clip(lower=0),
            Arbeitslosen_Geld_Reduktion_über_Nettolohn_hinaus = lambda x:  (-x.diff__arbeitslosen_geld - x.diff__nettolohn ).clip(lower=0),
            Lohnsteuer                                        = lambda x:  x.diff__lohnsteuer,
            Kirchensteuer                                     = lambda x:  x.diff__kirchensteuer,
            Solidaritätszuschlag                              = lambda x:  x.diff__solidaritätszuschlag,
            Rentenversicherung                                = lambda x:  x.diff__rentenversicherung,
            Arbeitslosenversicherung                          = lambda x:  x.diff__arbeitslosenversicherung,
            Krankenversicherung                               = lambda x:  x.diff__krankenversicherung,
            Pflegeversicherung                                = lambda x:  x.diff__pflegeversicherung,
        ).set_index("Bruttomonatslohn")
    ).round(2)

    df_vis_diff_percent = (
        df_vis_diff.div(df_vis_diff["diff__bruttolohn"]*0.01, axis=0)    
        .loc[:,
           ["Kindergeld","Nettolohn_minus_Arbeitslosen_Geld_Reduktion","Arbeitslosen_Geld_Reduktion","Lohnsteuer","Kirchensteuer","Solidaritätszuschlag","Rentenversicherung","Arbeitslosenversicherung","Krankenversicherung","Pflegeversicherung","Arbeitslosen_Geld_Zuwachs","Arbeitslosen_Geld_Reduktion_über_Nettolohn_hinaus"
        ]]
    )

    fig, axes = plt.subplots(nrows=2)
    fig.set_size_inches(15, 12, forward=True)
    fig.set_facecolor("w")
    df_vis_total.plot.area(ax=axes[0],
        title="Gesamtverteilung",
        linewidth=0,
        color={
            "Kindergeld": "#449A90",
            "Nettolohn": "#63BE7B",
            "Arbeitslosen_Geld": "#8DCF9E",
            "Lohnsteuer": "#F8696B",
            "Kirchensteuer": "#C062AC",
            "Solidaritätszuschlag": "#DC6AC4",
            "Rentenversicherung": "#717DD5",
            "Arbeitslosenversicherung": "#899DBD",
            "Krankenversicherung": "#56CBF0",
            "Pflegeversicherung": "#16B3D8",
        },
        ylabel="Euro",
    ).legend(loc='center left',bbox_to_anchor=(1.0, 0.5), prop={'size': 12})


    df_vis_diff_percent.plot.area(ax=axes[1],
        title="Verteilung pro extra Euro",
        linewidth=0,
        color={
            "Arbeitslosen_Geld_Zuwachs": "#8DCF9E",
            "Kindergeld": "#449A90",
            "Nettolohn_minus_Arbeitslosen_Geld_Reduktion": "#63BE7B",
            "Arbeitslosen_Geld_Reduktion_über_Nettolohn_hinaus": "black",
            "Arbeitslosen_Geld_Reduktion": "#FA989A",        
            "Lohnsteuer": "#F8696B",
            "Kirchensteuer": "#C062AC",
            "Solidaritätszuschlag": "#DC6AC4",
            "Rentenversicherung": "#717DD5",
            "Arbeitslosenversicherung": "#899DBD",
            "Krankenversicherung": "#56CBF0",
            "Pflegeversicherung": "#16B3D8",
        },
        ylabel="Prozent",
    ).legend(loc='center left',bbox_to_anchor=(1.0, 0.5), prop={'size': 12})

    fig.subplots_adjust(right=0.5)
    fig.savefig(f"result {name}.png", format="png")
