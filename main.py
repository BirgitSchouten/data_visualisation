import matplotlib.pyplot as plt
import pandas as pd
import geopandas

from code.read_data import get_series, get_data

if __name__ == "__main__":

    series = [(1, 'AG.LND.EL5M.ZS', 'Land area below 5m (% of land area)'), (2, 'AG.LND.IRIG.AG.ZS', 'Agricultural land under irrigation (% of total ag. land)'), (3, 'AG.YLD.CREL.KG', 'Cereal yield (kg per hectare)'), (4, 'BX.KLT.DINV.WD.GD.ZS', 'Foreign direct investment, net inflows (% of GDP)'), (5, 'EG.ELC.ACCS.ZS', 'Access to electricity (% of total population)'), (6, 'EG.USE.COMM.GD.PP.KD', 'Energy use per units of GDP (kg oil eq./$1,000 of 2005 PPP $)'), (7, 'EG.USE.PCAP.KG.OE', 'Energy use per capita (kilograms of oil equivalent)'), (8, 'EN.ATM.CO2E.KT', 'CO2 emissions, total (KtCO2)'), (9, 'EN.ATM.CO2E.PC', 'CO2 emissions per capita (metric tons)'), (10, 'EN.ATM.CO2E.PP.GD.KD', 'CO2 emissions per units of GDP (kg/$1,000 of 2005 PPP $)'), (11, 'EN.ATM.GHGO.KT.CE', 'Other GHG emissions, total (KtCO2e)'), (12, 'EN.ATM.METH.KT.CE', 'Methane (CH4) emissions, total (KtCO2e)'), (13, 'EN.ATM.NOXE.KT.CE', 'Nitrous oxide (N2O) emissions, total (KtCO2e)'), (14, 'EN.CLC.AERT', 'Annex-I emissions reduction target'), (15, 'EN.CLC.DRSK.XQ', 'Disaster risk reduction progress score (1-5 scale; 5=best)'), (16, 'EN.CLC.GHGR.MT.CE', 'GHG net emissions/removals by LUCF (MtCO2e)'), (17, 'EN.CLC.HCDM', 'Hosted Clean Development Mechanism (CDM) projects'), (18, 'EN.CLC.HJIP', 'Hosted Joint Implementation (JI) projects'), (19, 'EN.CLC.HPPT.MM', 'Average annual precipitation (1961-1990, mm)'), (20, 'EN.CLC.ICER', 'Issued Certified Emission Reductions (CERs) from CDM (thousands)'), (21, 'EN.CLC.IERU', 'Issued Emission Reduction Units (ERUs) from JI (thousands)'), (22, 'EN.CLC.MDAT.ZS', 'Droughts, floods, extreme temps (% pop. avg. 1990-2009)'), (23, 'EN.CLC.MMDT.C', 'Average daily min/max temperature (1961-1990, Celsius)'), (24, 'EN.CLC.NAMA', 'NAMA submission'), (25, 'EN.CLC.NAPA', 'NAPA submission'), (26, 'EN.CLC.NCOM', 'Latest UNFCCC national communication'), (27, 'EN.CLC.PCAT.C', 'Projected annual temperature change (2045-2065, Celsius)'), (28, 'EN.CLC.PCCC', 'Projected change in annual cool days/cold nights'), (29, 'EN.CLC.PCHW', 'Projected change in annual hot days/warm nights'), (30, 'EN.CLC.PCPT.MM', 'Projected annual precipitation change (2045-2065, mm)'), (31, 'EN.CLC.RNET', 'Renewable energy target'), (32, 'EN.POP.EL5M.ZS', 'Population below 5m (% of total)'), (33, 'EN.URB.MCTY.TL.ZS', 'Population in urban agglomerations >1million (%)'), (34, 'ER.H2O.FWTL.ZS', 'Annual freshwater withdrawals (% of internal resources)'), (35, 'ER.LND.PTLD.ZS', 'Nationally terrestrial protected areas (% of total land area)'), (36, 'IC.BUS.EASE.XQ', 'Ease of doing business (ranking 1-183; 1=best)'), (37, 'IE.PPI.ENGY.CD', 'Invest. in energy w/ private participation ($)'), (38, 'IE.PPI.TELE.CD', 'Invest. in telecoms w/ private participation ($)'), (39, 'IE.PPI.TRAN.CD', 'Invest. in transport w/ private participation ($)'), (40, 'IE.PPI.WATR.CD', 'Invest. in water/sanit. w/ private participation ($)'), (41, 'IQ.CPA.PUBS.XQ', 'Public sector mgmt & institutions avg. (1-6 scale; 6=best)'), (42, 'IS.ROD.PAVE.ZS', 'Paved roads (% of total roads)'), (43, 'NY.GDP.MKTP.CD', 'GDP ($)'), (44, 'NY.GNP.PCAP.CD', 'GNI per capita (Atlas $)'), (45, 'SE.ENR.PRSC.FM.ZS', 'Ratio of girls to boys in primary & secondary school (%)'), (46, 'SE.PRM.CMPT.ZS', 'Primary completion rate, total (% of relevant age group)'), (47, 'SH.DYN.MORT', 'Under-five mortality rate (per 1,000)'), (48, 'SH.H2O.SAFE.ZS', 'Access to improved water source (% of total pop.)'), (49, 'SH.MED.NUMW.P3', 'Nurses and midwives (per 1,000 people)'), (50, 'SH.MED.PHYS.ZS', 'Physicians (per 1,000 people)'), (51, 'SH.MLR.INCD', 'Malaria incidence rate (per 100,000 people)'), (52, 'SH.STA.ACSN', 'Access to improved sanitation (% of total pop.)'), (53, 'SH.STA.MALN.ZS', 'Child malnutrition, underweight (% of under age 5)'), (54, 'SI.POV.DDAY', 'Population living below $1.25 a day (% of total)'), (55, 'SP.POP.GROW', 'Population growth (annual %)'), (56, 'SP.POP.TOTL', 'Population'), (57, 'SP.URB.GROW', 'Urban population growth (annual %)'), (58, 'SP.URB.TOTL', 'Urban population')]
    for part in series:
        print(part[0], part[2])
    
    choice = 100
    while choice < 1 or choice > 58:
        choice = int(input("Type the number of the topic you'd like to visualize.\n"))

    year = 0
    while year < 1990 or year > 2011:
        year = int(input("Type the year you'd like to visualize.\n"))
    year = str(year)

    # set values for visualisation
    code = series[choice - 1][1]
    year = year

    # retrieve panda dataframe
    data = get_data("data/Worldwide_climate_change_(Worldbank, 2011).csv", code)

    # get countries for visualisation and fix wrong codes
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    world.columns=['pop_est', 'continent', 'name', 'Country code', 'gdp_md_est', 'geometry']

    world.at[11, 'Country code'] = 'ZAR'
    world.at[21, 'Country code'] = 'NOR'
    world.at[24, 'Country code'] = 'TMP'
    world.at[43, 'Country code'] =  'FRA'
    world.at[117, 'Country code'] = 'ROM'
    world.at[160, 'Country code'] = 'CYP'
    world.at[167, 'Country code'] = 'SOM'
    world.at[174, 'Country code'] = 'KSV'
    world.at[176, 'Country code'] = 'SDN'

    # merge location dataframe with data we want to display
    merge = pd.merge_ordered(world, data, on = 'Country code')

    # create plot
    fig, ax = plt.subplots(1, 1)

    merge.plot(column = year, legend = True, legend_kwds = {"orientation": "horizontal"}, missing_kwds = {"color": "lightgrey", "label": "Missing values"}, cmap='viridis')
    plt.savefig("./visualisation/world.png")