Job = {
    "Batch"           : True,
    "Analysis"        : "ZAnalysis",
    "Fraction"        : 1,
    "MaxEvents"       : 1234567890,
    "OutputDirectory" : "resultsZ/"
}

prefix = "https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/4lep/" # online
#prefix = "Input/4lep/" # local if you've downloaded the data

Processes = {

    # H -> ZZ -> 4lep processes
  #  "ZH125_ZZ4lep"          : prefix+"MC/mc_341947.ZH125_ZZ4lep.4lep.root",
  #  "WH125_ZZ4lep"          : prefix+"MC/mc_341964.WH125_ZZ4lep.4lep.root",
  #  "VBFH125_ZZ4lep"        : prefix+"MC/mc_344235.VBFH125_ZZ4lep.4lep.root",
  #  "ggH125_ZZ4lep"         : prefix+"MC/mc_345060.ggH125_ZZ4lep.4lep.root",

    # Z + jets processes
    "Zee"                   : prefix+"MC/mc_361106.Zee.4lep.root",
    "Zmumu"                 : prefix+"MC/mc_361107.Zmumu.4lep.root",
    "Ztautau"                 : prefix+"MC/mc_361108.Ztautau.4lep.root",

    # Diboson processes
    "ZqqZll"                : prefix+"MC/mc_363356.ZqqZll.4lep.root",
    "WqqZll"                : prefix+"MC/mc_363358.WqqZll.4lep.root",
    #"WpqqWmlv"              : prefix+"MC/mc_363359.WpqqWmlv.4lep.root",
    #"WplvWmqq"              : prefix+"MC/mc_363360.WplvWmqq.4lep.root",
    #"WlvZqq"                : prefix+"MC/mc_363489.WlvZqq.4lep.root",

   
    "llll"                  : prefix+"MC/mc_363490.llll.4lep.root",
    "lllv"                  : prefix+"MC/mc_363491.lllv.4lep.root",
    "llvv"                  : prefix+"MC/mc_363492.llvv.4lep.root",
    #"lvvv"                  : prefix+"MC/mc_363493.lvvv.4lep.root",

    # top pair and single top processes
    "ttbar_lep"             : prefix+"MC/mc_410000.ttbar_lep.4lep.root",
    "single_top_tchan"      : prefix+"MC/mc_410011.single_top_tchan.4lep.root",
    "single_antitop_tchan"  : prefix+"MC/mc_410012.single_antitop_tchan.4lep.root",
    #"single_top_schan"      : prefix+"MC/mc_410025.single_top_schan.root",
    "single_antitop_schan"  : prefix+"MC/mc_410026.single_antitop_schan.4lep.root",
    "single_top_wtchan"     : prefix+"MC/mc_410013.single_top_wtchan.4lep.root",
    "single_antitop_wtchan" : prefix+"MC/mc_410014.single_antitop_wtchan.4lep.root",

    # W + jets processes
    #"Wplusenu"              : prefix+"MC/mc_361100.Wplusenu.4lep.root",
    #"Wplusmunu"             : prefix+"MC/mc_361101.Wplusmunu.4lep.root",
#    "Wplustaunu"            : prefix+"MC/mc_361102.Wplustaunu.4lep.root",
#    "Wminusenu"             : prefix+"MC/mc_361103.Wminusenu.4lep.root",
#    "Wminusmunu"            : prefix+"MC/mc_361104.Wminusmunu.4lep.root",
#    "Wminustaunu"           : prefix+"MC/mc_361105.Wminustaunu.4lep.root",
 

    # Data
    "data_A"                : prefix+"Data/data_A.4lep.root",
    "data_B"                : prefix+"Data/data_B.4lep.root",
    "data_C"                : prefix+"Data/data_C.4lep.root",
    "data_D"                : prefix+"Data/data_D.4lep.root",

}
