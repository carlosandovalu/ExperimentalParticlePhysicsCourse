config = {
#"Luminosity": 547, #period A
#"Luminosity": 1949, #period B
#"Luminosity": 2884, #period C
#"Luminosity": 4684, #period D
"Luminosity": 10064, #period A-D
"InputDirectory": "resultsZ",

"Histograms" : {
    "invMassZ"       : {"rebin" : 3},
    "lep_n"           : {"y_margin" : 0.4},
    "lep_pt"          : {"y_margin" : 0.4, "rebin" : 4},
    "lep_eta"         : {"y_margin" : 0.5, "rebin" : 3},
    "lep_E"           : {"rebin" : 3},
    "lep_phi"         : {"y_margin" : 0.6, "rebin" : 4,},
    "lep_charge"      : {"y_margin" : 0.6},
    "lep_type"        : {"y_margin" : 0.5,},
    "lep_ptconerel30" : {"y_margin" : 0.3, "rebin" : 4},
    "lep_etconerel20" : {"y_margin" : 0.3, "rebin" : 4},

},

"Paintables": {
    "Stack": {
  "Order": ["Diboson", "Z", "stop", "ttbar"],
   "Processes" : {
       "Diboson" : {
           "Color"         : "#fa7921",
           "Contributions" : ["ZqqZll", "WqqZll", "llll", "lllv", "llvv"]},

       
       "stop": {
           "Color"         : "#fde74c",
           "Contributions" : ["single_top_tchan", "single_antitop_tchan" , "single_antitop_schan", "single_top_wtchan", "single_antitop_wtchan"]},

       "ttbar": {
           "Color"         : "#9bc53d",
           "Contributions" : ["ttbar_lep"]},

       "Z": {
           "Color"         : "#086788",
           "Contributions" : ["Zee", "Zmumu", "Ztautau"]},

        }
    },

    "data" : {
        "Contributions": ["data_A", "data_B", "data_C", "data_D"]}
},

"Depictions": {
    "Order": ["Main", "Data/MC"],
    "Definitions" : {
        "Data/MC": {
            "type"       : "Agreement",
            "Paintables" : ["data", "Stack"]
        },
        
        "Main": {
            "type"      : "Main",
            "Paintables": ["Stack", "data"]
        },
    }
},
}
