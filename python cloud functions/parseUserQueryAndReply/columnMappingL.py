actual_weight_dict = {}
actual_shape_dict = {'ROUND':'RD', 'RD':'RD', 'R':'RD', 'BR':'RD', 'RB':'RD',
          'ROUND BRILLIANT':'RD','ROUNDBRILLIANT':'RD', 'BRILLIANT':'RD',
          'BRILLIANT CUT':'RD', 'BRILLIANTCUT':'RD', 
          'OVAL':'OV',  'OV':'OV', 'OC':'OV',  'OVEL':'OV', 'OL':'OV', 
          'EMERALD':'EM', 'EM':'EM', 'EMRD':'EM', 'EC':'EM', 
          'CUSHION MODIFIED':'CU', 'CMB':'CU','CM':'CU', 'CS':'CU', 'CUSHIONMODIFIED':'CU',
          'CUSHION':'CU', 'CUS':'CU','CU':'CU',
          'PRINCESS':'PR','PR':'PR','PC':'PR',
          'PEAR':'PS','PAER':'PS', 'PER':'PS', 'PS':'PS',
          'RADIANT':'RA', 'RAD':'RA', 'RA':'RA',          
          'MARQUISE':'MQ', 'MR':'MQ', 'MQ':'MQ', 'MAR':'MQ',
          'ASHCHER':'AS', 'AS':'AS', 'ASSCHER': 'AS',
          'HEART':'HS','HRT':'HS', 'LOVE':'HS', 'HS':'HS', 'HR':'HS', 'HC':'HS',
          'TRIANGLE':'TR', 'TRI': 'TR', 'TR':'TR'}

# Shape Count 10 
shape_list = ['RD', 'OV', 'EM', 'CU', 'PR', 'PS', 'RA', 'MQ', 'AS', 'HS']
rare_shape_list = ['TR']
# shape_classes = ['RD','OV','EM','CMB','PR','PS','RA','AS','MQ','BR','HS']  # 11 classes
# # class_not_dealing = ['PE','SEM','TRI']  # 3 classes

def getActualShape(input_shape):
  if type(input_shape) == str:
    try: 
      return actual_shape_dict[input_shape.strip().upper()]
    except KeyError:
      return input_shape
  else: 
    return input_shape


actual_color_dict = {'D':'D', 'E':'E', 'F':'F', 'D-':'D', 'E-':'E', 'F-':'F','D+':'D', 'E+':'E', 'F+':'F',
                     'G':'G', 'H':'H', 'I':'I', 'G-':'G', 'H-':'H', 'I-':'I', 'G+':'G', 'H+':'H', 'I+':'I',
                     'J':'J', 'K':'K', 'L':'L', 'J-':'J', 'K-':'K', 'L-':'L', 'J+':'J', 'K+':'K', 'L+':'L',
                     'M':'M', 'N':'N', 'O':'O', 'M-':'M', 'N-':'N', 'O-':'O', 'M+':'M', 'N+':'N', 'O+':'O',
                     'P':'P', 'Q':'Q', 'P-':'P', 'Q-':'Q', 'Q+':'Q', 'P+':'P',
                     'Q':'Q', 'R':'R', 'S':'S', 'T':'T', 'U':'U', 'V':'V',
                     'W':'W', 'X':'X', 'Y':'Y', 'Z':'Z'}
# Color Count 23
color_list = ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
rare_color_list = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def getActualColor(input_color):
  if type(input_color) == str:
    try: 
      return actual_color_dict[input_color.strip().upper()]
    except KeyError:
      return input_color
  else: 
    return input_color


actual_fluor_dict = {
    'NONE':'N', 'NON':'N', 'N':'N', 'NO':'N', 'NAN':'N',
    'FAINT':'F','FNT':'F', 'FAINT':'F', 'F': 'F',
    'MEDIUM':'M','MED':'M', 'M':'M', 'MEDIUMYELLOW': 'M',
    'STRONG':'S', 'STG':'S', 'S':'S', 'ST':'S', 'STRONGYELLOW':'S',
    'VERY STRONG':'VS', 'VST':'VS', 'VSTG':'VS', 'VS':'VS', 'VERYSTRONG':'VS', 'VERYSTRONGBL': 'VS',
    }
# Fluor Count 5
fluor_list = ['N', 'F', 'M', 'S', 'VS'] 
rare_fluor_list = []

def getActualFluor(input_fluor): 
  if type(input_fluor) == str:
    try: 
      return actual_fluor_dict[input_fluor.strip().upper()]
    except KeyError:
      return input_fluor
  else: 
    return input_fluor

actual_clarity_dict = {
    'FL':'FL', 'IF':'IF', 'VVS1':'VVS1', 'VVS2':'VVS2', 'VS1':'VS1',
    'FL-':'IF', 'IF-':'IF', 'VVS1-':'VVS1', 'VVS2-':'VVS2', 'VS1-':'VS1',
    'FL+':'IF', 'IF+':'IF', 'VVS1+':'VVS1', 'VVS2+':'VVS2', 'VS1+':'VS1',
    'VS2':'VS2', 'SI1':'SI1', 'SI2':'SI2', 'I1':'', 'I2':'', 'I3':'I3',
    'VS2-':'VS2', 'SI1-':'SI1', 'SI2-':'SI2', 'I1-':'I1', 'I2-':'I2', 'I3-':'I3',
    'VS2+':'VS2', 'SI1+':'SI1', 'SI2+':'SI2', 'I1+':'I1', 'I2+':'I2', 'I3+':'I3'}
# Clarity Count 12
clarity_list = ['FL', 'IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1', 'I2', 'I3']
rare_clarity_list = ['PK']

def getActualClarity(input_clarity, default_value): 
  if type(input_clarity) == str:
    try: 
      return actual_clarity_dict[input_clarity.strip().upper()]
    except KeyError:
      return default_value
  else: 
    return default_value


def getBNCLarity(actual_clarity) :
  if actual_clarity == 'FL':
    return 'IF'
  if actual_clarity in ['I1', 'I2', 'I3']:
    return 'SI2'
  return actual_clarity


actual_cut_dict = {'EX':'X', 'VG':'VG', 'G': 'G', 'X':'X',
                   'EX-':'X', 'VG-':'VG', 'G-': 'G',
                   'EX+':'X', 'VG+':'VG', 'G+': 'G',
                   'EXCELLENT':'X', 'VERY GOOD': 'VG', 'VERYGOOD': 'VG', 'GOOD': 'G',
                   'F':'F','FAIR':'F','P':'P','POOR':'P',}
# Cut Count 5
cut_list = ['X', 'VG', 'G']
rare_cut_list = ['F', 'P']

def getActualCut(input_cut, default_value, shape):
  if not shape == "RD":
    return default_value # Default is VG for all the shapes  
  if type(input_cut) == str:
    try: 
      return actual_cut_dict[input_cut.strip().upper()]
    except KeyError:
      return default_value
  else: 
    return default_value

actual_polish_dict = {'EX':'X', 'VG':'VG', 'G': 'G', 'X':'X',
                   'EX-':'X', 'VG-':'VG', 'G-': 'G',
                   'EX+':'X', 'VG+':'VG', 'G+': 'G',
                   'EXCELLENT':'X', 'VERY GOOD': 'VG', 'VERYGOOD': 'VG', 'GOOD': 'G',
                   'F':'F','FAIR':'F','P':'P','POOR':'P',}
# Polish Count 5
polish_list = ['X', 'VG', 'G']
rare_polish_list = ['F', 'P']
def getActualPolish(input_polish, default_value): 
  if type(input_polish) == str:
    try: 
      return actual_polish_dict[input_polish.strip().upper()]
    except KeyError:
      return default_value
  else: 
    return default_value


actual_sym_dict = {'EX':'X', 'VG':'VG', 'G': 'G', 'X':'X',
                   'EX-':'X', 'VG-':'VG', 'G-': 'G',
                   'EX+':'X', 'VG+':'VG', 'G+': 'G',
                   'EXCELLENT':'X', 'VERY GOOD': 'VG', 'VERYGOOD': 'VG', 'GOOD': 'G',
                   'F':'F','FAIR':'F','P':'P','POOR':'P',}
# Symmetry Count 5
sym_list = ['X', 'VG', 'G']
rare_sym_list = ['F', 'P']

def getActualSym(input_sym, default_value): 
  if type(input_sym) == str:
    try: 
      return actual_sym_dict[input_sym.strip().upper()]
    except KeyError:
      return default_value
  else: 
    return default_value

# Weight Count 28
#weight_list = [0.23, 0.30, 0.38, 0.46, 0.50, 0.55, 0.60, 0.70, 0.75, 0.80, 0.90, 0.95,
#               1.00, 1.05, 1.10, 1.20, 1.30, 1.40, 1.50, 1.70, 1.80, 2.00, 2.20, 2.40,
#               2.70, 3.00, 4.00, 5.00, 45.00]
weight_list = [0.23, 0.29, 0.37, 0.45, 0.49, 0.54, 0.59, 0.69, 0.74, 0.79, 0.89, 0.94,
               0.99, 1.04, 1.09, 1.19, 1.29, 1.39, 1.49, 1.69, 1.79, 1.99, 2.19, 2.39,
               2.69, 2.99, 3.99, 5.00, 45.00]
rare_weight_list = [10.00, 15.00, 20.00, 25.00, 30.00, 40.00, 50.00]

""" Weight for given stone will be represented by upper end of the range. 
    If the weight of diamond is '0.25', then it will be in the range '0.30'
    For diamond with weight '0.10', it will be under '0.23'
"""
def get_d360_weight(input_weight_str):
    if type(input_weight_str) == int or type(input_weight_str) == float:
      input_weight = input_weight_str
    else:
      input_weight = float(input_weight_str)
    for weight_temp in weight_list: 
      if input_weight < (weight_temp + 0.001):
        return str(weight_temp)

actual_shape_heading_dict={'SHAPE':'SHAPE','SHP':'SHAPE'}

def getActualShapeHeading(input_shape_heading):
    if type(input_shape_heading) == str:
        try: 
            return actual_shape_heading_dict[input_shape_heading.strip().upper()]
        except KeyError:
            return input_shape_heading
    else: 
        return input_shape_heading

actual_color_heading_dict={'COLOR':'COLOR','COL':'COLOR','COLOUR':'COLOR','CLR':'COLOR'}

def getActualColorHeading(input_color_heading):
    if type(input_color_heading) == str:
        try: 
            return actual_color_heading_dict[input_color_heading.strip().upper()]
        except KeyError:
            return input_color_heading
    else: 
        return input_color_heading

actual_cut_heading_dict={'CUT GRADE':'CUT','CUT':'CUT'}

def getActualCutHeading(input_cut_heading):
    if type(input_cut_heading) == str:
        try: 
            return actual_cut_heading_dict[input_cut_heading.strip().upper()]
        except KeyError:
            return input_cut_heading
    else: 
        return input_cut_heading

actual_fluor_heading_dict={'FLUORESCENCE INTENSITY':'FLUORESCENCE','FLUORESCENCE':'FLUORESCENCE','FLUOR':'FLUORESCENCE','FLOUR':'FLOUORESCENCE'}

def getActualFluorHeading(input_fluor_heading):
    if type(input_fluor_heading) == str:
        try: 
            return actual_fluor_heading_dict[input_fluor_heading.strip().upper()]
        except KeyError:
            return input_fluor_heading
    else: 
        return input_fluor_heading

actual_clarity_heading_dict={'CLARITY':'CLARITY','CLR':'CLARITY','PURITY':'CLARITY'}

def getActualClarityHeading(input_clarity_heading):
    if type(input_clarity_heading) == str:
        try:
            return actual_clarity_heading_dict[input_clarity_heading.strip().upper()]
        except KeyError:
            return input_clarity_heading
    else:
        return input_clarity_heading

actual_sym_heading_dict={'SYMMETRY':'SYMMETRY','SYM':'SYMMETRY'}

def getActualSymHeading(input_sym_heading):
    if type(input_sym_heading) == str:
        try: 
            return actual_sym_heading_dict[input_sym_heading.strip().upper()]
        except KeyError:
            return input_sym_heading
    else: 
        return input_sym_heading

actual_polish_heading_dict={'POLISH':'POLISH','POL':'POLISH'}

def getActualPolishHeading(input_polish_heading):
    if type(input_polish_heading) == str:
        try: 
            return actual_polish_heading_dict[input_polish_heading.strip().upper()]
        except KeyError:
            return input_polish_heading
    else: 
        return input_polish_heading

# actual_polish_heading_dict={'CUT GRADE':'CUT','CUT':'CUT'}

def getActualWeightHeading(input_fluor_heading):
    if type(input_fluor_heading) == str:
        try: 
            return actual_fluor_heading_dict[input_fluor_heading.strip().upper()]
        except KeyError:
            return input_fluor_heading
    else: 
        return input_fluor_heading

# actual_polish_heading_dict={'CUT GRADE':'CUT','CUT':'CUT'}

def getActualRapHeading(input_fluor_heading):
    if type(input_fluor_heading) == str:
        try: 
            return actual_fluor_heading_dict[input_fluor_heading.strip().upper()]
        except KeyError:
            return input_fluor_heading
    else: 
        return input_fluor_heading

# It will generate key by joining all properties by ',' and return it.
def dict_key(weight, shape, color, clarity, fluor, cut, polish, sym): #WSCCFCPS
  return ','.join([get_d360_weight(weight), shape, color, clarity, fluor, cut, polish, sym]).strip().upper()


def user_value_dict_key(weight, shape, color, clarity, fluor, cut, polish, sym) :
  weight = weight
  shape = actual_shape_dict[shape.strip().upper()]
  color = actual_color_dict[color.strip().upper()]
  clarity = actual_clarity_dict[clarity.strip().upper()]
  fluor = actual_fluor_dict[fluor.strip().upper()]
  cut = actual_cut_dict[cut.strip().upper()]
  polish = actual_polish_dict[polish.strip().upper()]
  sym = actual_sym_dict[sym.strip().upper()]
  return dict_key(weight, shape, color, clarity, fluor, cut, polish, sym)