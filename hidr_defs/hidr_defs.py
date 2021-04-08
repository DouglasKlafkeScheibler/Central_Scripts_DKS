import struct, datetime
from functools import partial

#Esse script tem como função conseguir adquirir as informações do HIDR e formatar as mesmas

COMPANY = {
11:'11 - Escelsa',
13:'13 - ELTNORTE-SE',
15:'15 - Eletropaulo',
16:'16 - CESP',
17:'17 - Light',
18:'18 - Cemig',
19:'19 - Furnas',
20:'20 - Celesc',
22:'22 - CEEE',
23:'23 - Copel',
24:'24 - Eletrosul',
33:'33 - CHESF',
34:'34 - Celpa',
37:'37 - Eletronorte',
40:'40 - Itaipu',
42:'42 - CDSA',
51:'51 - Externas SE',
52:'52 - Externas Sul',
53:'53 - Externas NE',
54:'54 - Externas Norte'}

CONVBOOL = ['No','Yes']

SYSTEM = {1:'1 - Sudeste',2:'2 - Sul',3:'3 - Nordeste',4:'4 - Norte'}

TURBINE = {0:'0 - NÃO HÁ',1:'1 - Francis', 2:'2 - Kaplan/Propeller',3:'3 - Pelton'}

SETREPR = {0:'0 - Aprox.',1:'1 - Det.',2:'2 - Simpl.'}

LOSS = {1:'1 - %',2:'2 - m',3:'3 - K'}

REGULATION = {'D':'Diária','S':'Semanal','M':'Mensal'}

class hidroPlant:

    def __init__(self, index):
        self.index = index
        self.name = ''
        self.stationId = 0
        self.bdhStationId = ''
        self.system = 0
        self.company = 0
        self.downstream = 0
        self.detour = 0
        self.minVol = 0
        self.maxVol = 0
        self.spillVol = 0
        self.detourVol = 0
        self.maxQuota = 0
        self.minQuota = 0
        self.quotaVolPoly = []
        self.areaQuotaPoly = []
        self.evaporation = []
        self.genGroups = 0
        self.numGenPerGroup = []
        self.potEfPerGroup = []
        self.QHTPolyPerGroup = []
        self.QHGPolyPerGroup = []
        self.PHPolyPerGroup = []
        self.hEfPerGroup = []
        self.qEfPerGroup = []
        self.specificProduct = 0
        self.lossValue = 0
        self.numDownstreamPoly = 0
        self.downstreamPolynomials = []
        self.downstreamPolyRef = []
        self.averageTailrace = 0
        self.influenceTailrace = 0
        self.maxLoadFactor = 0
        self.minLoadFactor = 0
        self.minHistFlow = 0
        self.baseUnit = 0
        self.turbineType = 0
        self.setModeling = 0
        self.teif = 0
        self.ip = 0
        self.lossType = 0
        self.date = ''
        self.note = ''
        self.refVol = 0
        self.regulation = ''
        
    def display(self):
        print('Plant: ',self.name,', Index: ', self.index,', Station: ',self.stationId)

def hidroFromBytes(index, rawData):
    plant = hidroPlant(index)
    
    tmp = struct.unpack('12s',rawData[0:12])[0].decode('utf-8')
    
    if tmp == '            ':
        return None
    
    plant.name = tmp

    # We constantly add 0 to all the floats because python follows IEEE standard for floating point numbers which includes the -0.0 (negative zero).
    # Adding 0 to all floats guarantees that this negative zero becomes the positive zero and output remains the same as the original hydroEdit.
    tmp = struct.unpack('i8s4i6f',rawData[12:64])
    plant.stationId = tmp[0]
    plant.bdhStationId = tmp[1].decode('utf-8')
    plant.system = tmp[2]
    plant.company = tmp[3]
    plant.downstream = tmp[4]
    plant.detour = tmp[5]
    plant.minVol = tmp[6] + 0
    plant.maxVol = tmp[7] + 0
    plant.spillVol = tmp[8] + 0
    plant.detourVol = tmp[9] + 0
    plant.minQuota = tmp[10] + 0
    plant.maxQuota = tmp[11] + 0
    plant.quotaVolPoly = [x+0 for x in list(struct.unpack('5f',rawData[64:84]))]
    plant.areaQuotaPoly = [x+0 for x in list(struct.unpack('5f',rawData[84:104]))]
    plant.evaporation = list(struct.unpack('12i',rawData[104:152]))
    plant.genGroups = struct.unpack('i',rawData[152:156])[0]
    plant.numGenPerGroup = list(struct.unpack('5i',rawData[156:176]))
    plant.potEfPerGroup = [x+0 for x in list(struct.unpack('5f',rawData[176:196]))]
    
    plant.QHTPolyPerGroup.append([x+0 for x in list(struct.unpack('5f',rawData[196:216]))])
    plant.QHTPolyPerGroup.append([x+0 for x in list(struct.unpack('5f',rawData[216:236]))])
    plant.QHTPolyPerGroup.append([x+0 for x in list(struct.unpack('5f',rawData[236:256]))])
    plant.QHTPolyPerGroup.append([x+0 for x in list(struct.unpack('5f',rawData[256:276]))])
    plant.QHTPolyPerGroup.append([x+0 for x in list(struct.unpack('5f',rawData[276:296]))])
    
    plant.QHGPolyPerGroup.append([x+0 for x in list(struct.unpack('5f',rawData[296:316]))])
    plant.QHGPolyPerGroup.append([x+0 for x in list(struct.unpack('5f',rawData[316:336]))])
    plant.QHGPolyPerGroup.append([x+0 for x in list(struct.unpack('5f',rawData[336:356]))])
    plant.QHGPolyPerGroup.append([x+0 for x in list(struct.unpack('5f',rawData[356:376]))])
    plant.QHGPolyPerGroup.append([x+0 for x in list(struct.unpack('5f',rawData[376:396]))])
    
    plant.PHPolyPerGroup.append([x+0 for x in list(struct.unpack('5f',rawData[396:416]))])
    plant.PHPolyPerGroup.append([x+0 for x in list(struct.unpack('5f',rawData[416:436]))])
    plant.PHPolyPerGroup.append([x+0 for x in list(struct.unpack('5f',rawData[436:456]))])
    plant.PHPolyPerGroup.append([x+0 for x in list(struct.unpack('5f',rawData[456:476]))])
    plant.PHPolyPerGroup.append([x+0 for x in list(struct.unpack('5f',rawData[476:496]))])
    
    plant.hEfPerGroup = [x+0 for x in list(struct.unpack('5f',rawData[496:516]))]
    plant.qEfPerGroup = list(struct.unpack('5i',rawData[516:536]))
    
    tmp = struct.unpack('2fi',rawData[536:548])
    
    plant.specificProduct = tmp[0] + 0
    plant.lossValue = tmp[1] + 0
    plant.numDownstreamPoly = tmp[2]
    
    plant.downstreamPolynomials.append([x+0 for x in list(struct.unpack('5f',rawData[548:568]))])    # PJ 1
    plant.downstreamPolynomials.append([x+0 for x in list(struct.unpack('5f',rawData[568:588]))])    # PJ 2
    plant.downstreamPolynomials.append([x+0 for x in list(struct.unpack('5f',rawData[588:608]))])    # PJ 3
    plant.downstreamPolynomials.append([x+0 for x in list(struct.unpack('5f',rawData[608:628]))])    # PJ 4
    plant.downstreamPolynomials.append([x+0 for x in list(struct.unpack('5f',rawData[628:648]))])    # PJ 5
    plant.downstreamPolynomials.append([x+0 for x in list(struct.unpack('5f',rawData[648:668]))])    # PJ 6 ??

    plant.downstreamPolyRef = [x+0 for x in list(struct.unpack('6f',rawData[668:692]))]
   
    tmp = struct.unpack('fi2f4i2fi8s',rawData[692:744])
    plant.averageTailrace = tmp[0] + 0
    plant.influenceTailrace = tmp[1]
    plant.maxLoadFactor = tmp[2] + 0
    plant.minLoadFactor = tmp[3] + 0
    plant.minHistFlow = tmp[4]
    plant.baseUnit = tmp[5]
    plant.turbineType = tmp[6]
    plant.setModeling = tmp[7]
    plant.teif = tmp[8] + 0
    plant.ip = tmp[9] + 0
    plant.lossType = tmp[10]
    plant.date = datetime.datetime.strptime(tmp[11].decode('utf-8'), '%d/%m/%y')
        
    plant.note = struct.unpack('43s',rawData[744:787])[0].decode('utf-8')
    tmp = struct.unpack('f1s',rawData[744+43:744+43+4+1])
    plant.refVol = tmp[0] + 0
    plant.regulation = tmp[1].decode('utf-8')
    
    
    return plant

def getPlantOrIndex(plant, index):
    if plant != None:
        return str(plant.index) + ' - ' + plant.name
    if index == 0:
        return '0 - NÃO HÁ'
    return str(index) + ' - '

def getCompanyFromCode(code):
    if code in COMPANY:
        return COMPANY[code]
    else:
        return str(code) + ' - '

def getHydroEditString(plant,downstreamPlant = None,detourPlant = None,separator = ';'):

    template = '{:.2f};{:.2f}'';{:.2f};{:.2f};{:.2f}'
    template = template + ';{:.2f};{};{};{};{:.6f};{:.2f};{:.3f};{:.3f};{};{};{}'
    template = template + ';{:.2f};{:.2f};{};{:.2f};{};{};{};{};{};{};{};{};{};{}'

    tmp = template.format(

    plant.maxVol,
    plant.minVol,
    plant.maxQuota,
    plant.minQuota,
    plant.spillVol,
    plant.detourVol,
    ';'.join(["{:.6E}".format(x) for x in plant.quotaVolPoly]),
    ';'.join(["{:.6E}".format(x) for x in plant.areaQuotaPoly]),
    ';'.join(["{}".format(x) for x in plant.evaporation]),
    plant.specificProduct,
    plant.averageTailrace,
    plant.teif,
    plant.ip,
    TURBINE[plant.turbineType],
    plant.genGroups,
    plant.numDownstreamPoly,
    plant.maxLoadFactor,
    plant.minLoadFactor,
    plant.lossType,
    plant.lossValue,
    plant.minHistFlow,
    plant.baseUnit,
    CONVBOOL[plant.influenceTailrace],
    plant.setModeling,
    ';'.join(["{};{:.1f};{};{:.2f}".format(
    plant.numGenPerGroup[i],
    plant.potEfPerGroup[i] + 1e-9, # We add 1e-9 because hydroEdit always rounds .#5 up
    plant.qEfPerGroup[i],
    plant.hEfPerGroup[i]) for i in range(5)]),
    ';'.join(';'.join(["{:.6E}".format(x) for x in poly]) for poly in plant.QHTPolyPerGroup),
    ';'.join(';'.join(["{:.6E}".format(x) for x in poly]) for poly in plant.QHGPolyPerGroup),
    ';'.join(';'.join(["{:.6E}".format(x) for x in poly]) for poly in plant.PHPolyPerGroup),
    ';'.join(';'.join(["{:.6E}".format(x) for x in plant.downstreamPolynomials[i]]+['{:.2f}'.format(plant.downstreamPolyRef[i])]) for i in range(5)),
    plant.date
    )
    
    return '{};{};{};{};{};{};{};{};{};{};{};{};'.format(
    plant.index,plant.name,
    SYSTEM[plant.system],
    getCompanyFromCode(plant.company),
    plant.stationId,
    plant.bdhStationId,
    getPlantOrIndex(downstreamPlant, plant.downstream),
    getPlantOrIndex(detourPlant, plant.detour),
    tmp,
    plant.note,'{:.2f}'.format(plant.refVol),plant.regulation)


def hidroHeader():
    

    return ['CodUsina' , 'Usina' , 'Sistema' , 'Empresa' , 'Posto' , 'Posto_BDH' , 'Jusante' , 'Desvio' , 'Vol_Max_hm3' , 'Vol_min_hm3' , 'Cota_Máx_m',
        'Cota_min_m' , 'Vol_Vert_hm3' , 'Vol_Desv_hm3' , 'PCV_0', 'PCV_1', 'PCV_2', 'PCV_3', 'PCV_4', 'PAC_0', 'PAC_1', 'PAC_2', 'PAC_3', 'PAC_4', 'Evap_Men_1', 
        'Evap_Men_2' , 'Evap_Men_3' , 'Evap_Men_4' , 'Evap_Men_5' , 'Evap_Men_6' , 'Evap_Men_7' , 'Evap_Men_8' , 'Evap_Men_9' , 'Evap_Men_10' , 'Evap_Men_11', 
        'Evap_Men_12' , 'Prod_Esp_MW_m3_s_m', 'Canal_Fuga_Médio_m' , 'TEIF' , 'IP' , 'Tipo_Turbina' , 'Num_Conj_Máq' , 'Num_Pols_Jus' ,'Fat_Carga_Máx', 
        'Fat_Carga_mín' , 'Tipo_Perdas' , 'Valor_Perdas' , 'Vazão_Mín_Hist_m3_s' , 'Num_Unid_Base' , 'Infl_Vert_Canal_de_Fuga', 'Rep_Conj' , 'Maq_1' , 'PotEf_1' , 
        'QEf_1' , 'HEf_1' , 'Maq_2' , 'PotEf_2' , 'QEf_2' , 'HEf_2','Maq_3' , 'PotEf_3' , 'QEf_3' , 'HEf_3' , 'Maq_4' , 'PotEf_4' , 'QEf_4' , 'HEf_4' , 'Maq_5' , 'PotEf_5' , 'QEf_5' , 'HEf_5' , 'QHTA0_1', 
        'QHTA1_1', 'QHTA2_1', 'QHTA3_1', 'QHTA4_1', 'QHTA0_2', 'QHTA1_2', 'QHTA2_2', 'QHTA3_2', 'QHTA4_2', 'QHTA0_3', 'QHTA1_3', 'QHTA2_3', 'QHTA3_3', 'QHTA4_3', 'QHTA0_4', 
        'QHTA1_4', 'QHTA2_4', 'QHTA3_4', 'QHTA4_4', 'QHTA0_5', 'QHTA1_5', 'QHTA2_5', 'QHTA3_5', 'QHTA4_5', 'QHGA0_1', 'QHGA1_1', 'QHGA2_1', 'QHGA3_1', 'QHGA4_1', 'QHGA0_2', 
        'QHGA1_2', 'QHGA2_2', 'QHGA3_2', 'QHGA4_2', 'QHGA0_3', 'QHGA1_3', 'QHGA2_3', 'QHGA3_3', 'QHGA4_3', 'QHGA0_4', 'QHGA1_4', 'QHGA2_4', 'QHGA3_4', 'QHGA4_4', 'QHGA0_5', 
        'QHGA1_5', 'QHGA2_5', 'QHGA3_5', 'QHGA4_5', 'PHA0_1', 'PHA1_1', 'PHA2_1', 'PHA3_1', 'PHA4_1', 'PHA0_2', 'PHA1_2', 'PHA2_2', 'PHA3_2', 'PHA4_2', 'PHA0_3', 'PHA1_3', 
        'PHA2_3', 'PHA3_3', 'PHA4_3', 'PHA0_4', 'PHA1_4', 'PHA2_4', 'PHA3_4', 'PHA4_4', 'PHA0_5', 'PHA1_5', 'PHA2_5', 'PHA3_5', 'PHA4_5', 'PJA0_1', 'PJA1_1', 'PJA2_1', 'PJA3_1',
        'PJA4_1', 'PJRM_1', 'PJA0_2', 'PJA1_2', 'PJA2_2', 'PJA3_2', 'PJA4_2', 'PJRM_2', 'PJA0_3', 'PJA1_3', 'PJA2_3', 'PJA3_3', 'PJA4_3', 'PJRM_3', 'PJA0_4', 'PJA1_4', 'PJA2_4',
        'PJA3_4', 'PJA4_4', 'PJRM_4', 'PJA0_5', 'PJA1_5', 'PJA2_5', 'PJA3_5', 'PJA4_5', 'PJRM_5', 'deck_date', 'Obs', 'Vol_Ref' , 'Reg']
    
def readFile(file):

    data = {0:None}
    index = 1;
    
    with open(file,'rb') as f:
        for measurement in iter(partial(f.read, 792), b''):
        
            data[index] = hidroFromBytes(index, measurement)
            index = index + 1
            
    return data