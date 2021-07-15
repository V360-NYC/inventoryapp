__all__ = ['columnMapping']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['colorsG', 'clarityG', 'getColumnMapping_', 'polishG', 'cutG', 'shapeG', 'getActualShape_', 'flourG', 'actualFlour', 'getActualFlour_', 'userFlour', 'actualShape', 'symG', 'userShape', 'certG'])
@Js
def PyJsHoisted_getColumnMapping__(firstRow, companyIndex, this, arguments, var=var):
    var = Scope({'firstRow':firstRow, 'companyIndex':companyIndex, 'this':this, 'arguments':arguments}, var)
    var.registers(['firstRow', 'companyIndex'])
    while 1:
        SWITCHED = False
        CONDITION = (var.get('companyIndex'))
        if SWITCHED or PyJsStrictEq(CONDITION, var.get('dharamIndex')):
            SWITCHED = True
            return Js([Js(0.0), Js(1.0), Js(2.0), Js(3.0), Js(4.0), Js(5.0), Js(6.0), Js(7.0), Js(8.0), Js(9.0), Js(10.0), Js(11.0), Js(12.0), Js(13.0), Js(14.0), Js(15.0), Js(16.0), Js(17.0), Js(18.0), Js(19.0), Js(20.0)])
        if SWITCHED or PyJsStrictEq(CONDITION, var.get('kiranIndex')):
            SWITCHED = True
            return Js([Js(2.0), Js(3.0), Js(4.0), Js(5.0), Js(6.0), Js(7.0), Js(8.0), Js(9.0), Js(16.0), Js(17.0), Js(18.0), Js(20.0), Js(19.0), Js(1.0), Js(10.0), Js(26.0), Js(10.0), Js(12.0), Js(13.0), Js(15.0), Js(42.0)])
        if SWITCHED or PyJsStrictEq(CONDITION, var.get('rkIndex')):
            SWITCHED = True
            return Js([Js(2.0), Js(3.0), Js(4.0), Js(5.0), Js(6.0), Js(7.0), Js(8.0), Js(9.0), Js(11.0), Js(11.0), Js(11.0), Js(20.0), Js(21.0), Js(0.0), Js(13.0), Js(40.0), Js(12.0), Js(14.0), Js(15.0), Js(16.0), Js(13.0)])
        if SWITCHED or PyJsStrictEq(CONDITION, var.get('srkIndex')):
            SWITCHED = True
            return Js([Js(6.0), Js(9.0), Js(8.0), Js(7.0), Js(12.0), Js(13.0), Js(14.0), Js(15.0), Js(17.0), Js(17.0), Js(17.0), Js(18.0), Js(19.0), Js(4.0), Js(38.0), Js(20.0), Js(7.0), (-Js(1.0)), Js(11.0), (-Js(1.0)), Js(38.0)])
        SWITCHED = True
        break
    return var.get(u"null")
PyJsHoisted_getColumnMapping__.func_name = 'getColumnMapping_'
var.put('getColumnMapping_', PyJsHoisted_getColumnMapping__)
@Js
def PyJsHoisted_getActualShape__(inputShape, this, arguments, var=var):
    var = Scope({'inputShape':inputShape, 'this':this, 'arguments':arguments}, var)
    var.registers(['j', 'inputShape'])
    #for JS loop
    var.put('j', Js(0.0))
    while (var.get('j')<var.get('userShape').get('length')):
        try:
            if (var.get('userShape').get(var.get('j')).callprop('toLowerCase')==var.get('inputShape').callprop('trim').callprop('toLowerCase')):
                return var.get('actualShape').get(var.get('j'))
        finally:
                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
    return var.get(u"null")
PyJsHoisted_getActualShape__.func_name = 'getActualShape_'
var.put('getActualShape_', PyJsHoisted_getActualShape__)
@Js
def PyJsHoisted_getActualFlour__(inputFlour, this, arguments, var=var):
    var = Scope({'inputFlour':inputFlour, 'this':this, 'arguments':arguments}, var)
    var.registers(['inputFlour', 'j'])
    #for JS loop
    var.put('j', Js(0.0))
    while (var.get('j')<var.get('userFlour').get('length')):
        try:
            if (var.get('userFlour').get(var.get('j')).callprop('toLowerCase')==var.get('inputFlour').callprop('trim').callprop('toLowerCase')):
                return var.get('actualFlour').get(var.get('j'))
        finally:
                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
    return var.get(u"null")
PyJsHoisted_getActualFlour__.func_name = 'getActualFlour_'
var.put('getActualFlour_', PyJsHoisted_getActualFlour__)
pass
var.put('colorsG', Js([Js('D'), Js('E'), Js('F'), Js('G'), Js('H'), Js('I'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('O'), Js('P'), Js('Q')]))
var.put('clarityG', Js([Js('FL'), Js('IF'), Js('VVS1'), Js('VVS2'), Js('VS1'), Js('VS2'), Js('SI1'), Js('SI2'), Js('I1'), Js('I2'), Js('I3')]))
var.put('polishG', Js([Js('EX'), Js('VG')]))
var.put('symG', Js([Js('EX'), Js('VG')]))
var.put('cutG', Js([Js('EX'), Js('VG')]))
var.put('flourG', Js([Js('NONE'), Js('FAINT'), Js('MEDIUM'), Js('STRONG'), Js('VERY STRONG')]))
var.put('shapeG', Js([Js('ROUND'), Js('MARQUISE'), Js('PRINCESS'), Js('PEAR'), Js('OVAL'), Js('HEART'), Js('CUSHION MODIFIED'), Js('CUSHION'), Js('ASHCHER'), Js('RADIANT')]))
var.put('certG', Js([Js('gia'), Js('hrd'), Js('igi'), Js('fm')]))
var.put('userShape', Js([Js('Round'), Js('RD'), Js('R'), Js('BR'), Js('RB'), Js('Marquise'), Js('MR'), Js('MQ'), Js('MAR'), Js('Princess'), Js('PR'), Js('PC'), Js('Pear'), Js('Paer'), Js('Per'), Js('PS'), Js('Oval'), Js('Ov'), Js('Heart'), Js('Hrt'), Js('Love'), Js('Cushion Modified'), Js('CMB'), Js('CM'), Js('Cushion'), Js('Cus'), Js('CU'), Js('Ashcher'), Js('AS'), Js('Radiant'), Js('RAD'), Js('EMERALD'), Js('EM'), Js('EMRD')]))
var.put('actualShape', Js([Js('ROUND'), Js('ROUND'), Js('ROUND'), Js('ROUND'), Js('ROUND'), Js('MARQUISE'), Js('MARQUISE'), Js('MARQUISE'), Js('MARQUISE'), Js('PRINCESS'), Js('PRINCESS'), Js('PRINCESS'), Js('PEAR'), Js('PEAR'), Js('PEAR'), Js('PEAR'), Js('OVAL'), Js('OVAL'), Js('HEART'), Js('HEART'), Js('HEART'), Js('CUSHION MODIFIED'), Js('CUSHION MODIFIED'), Js('CUSHION MODIFIED'), Js('CUSHION'), Js('CUSHION'), Js('CUSHION'), Js('ASHCHER'), Js('ASHCHER'), Js('RADIANT'), Js('RADIANT'), Js('EMERALD'), Js('EMERALD'), Js('EMERALD')]))
pass
var.put('userFlour', Js([Js('None'), Js('Non'), Js('N'), Js('NO'), Js('Nan'), Js('strong'), Js('STG'), Js('Very Strong'), Js('VST'), Js('VSTG'), Js('MEDIUM'), Js('MED'), Js('FAINT'), Js('FNT'), Js('FAINT')]))
var.put('actualFlour', Js([Js('NONE'), Js('NONE'), Js('NONE'), Js('NONE'), Js('NONE'), Js('STRONG'), Js('STRONG'), Js('VERY STRONG'), Js('VERY STRONG'), Js('VERY STRONG'), Js('MEDIUM'), Js('MEDIUM'), Js('FAINT'), Js('FAINT'), Js('FAINT')]))
pass
pass


# Add lib to the module scope
columnMapping = var.to_python()