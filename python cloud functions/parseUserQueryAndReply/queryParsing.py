__all__ = ['queryParsing']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['polishKeywordValue', 'validDecimal_', 'cutTypo', 'dryRun', 'getSizeClause_', 'kiranIndex', 'queryParser_', 'shapeTypo', 'multiValueKeyword', 'createSimpleQuery_', 'columnNameC', 'shapeRange', 'priceKeyword', 'symRange', 'getActualFlour', 'numberRegex', 'priceKeywordValue', 'cutKeywordValue', 'backTypo', 'percentRegex', 'sizeKeywordValue', 'parseEntityKeyword_', 'rate_usTypo', 'getShapeClause_', 'tableTypo', 'labelName', 'createWhereClause_', 'cutKeyword', 'getBackClause_', 'getActualShape', 'colorRange', 'parsePercent', 'projectId', 'sizeKeyword', 'getReportNoClause_', 'colorTypo', 'clarityTypo', 'matchAndReplace', 'srkIndex', 'actualShape', 'rkIndex', 'userShape', 'userFlour', 'clarityKeyword', 'symTypo', 'multiValueKeywordValue', 'polishRange', 'QueryMode', 'depthTypo', 'getRangeClause_', 'setQueryMode', 'parsePointer', 'certTypo', 'actualFlour', 'flourTypo', 'replaceHotKeyword_', 'rapRateTypo', 'getRateClause_', 'sizeTypo', 'dharamIndex', 'polishTypo', 'companyDir', 'helpStr', 'cutRange', 'testcreateWhereClause_', 'parseNumberEntityKeyword_', 'polishKeyword', 'datasetId2', 'parseUserRequest', 'parseQueryToText', 'sizeRange', 'hiddenColumnNameC', 'companyCode', 'clarityKeywordValue', 'clarityRange', 'certRange', 'flourRange', 'companydatasetId', 'reportNoTypo', 'replaceHotKeywordSplit_', 'columnName', 'percentCharRegex', 'parseCPSKeyword_', 'pointerRegex'])
@Js
def PyJsHoisted_createSimpleQuery__(whereClause, parsedQuery, this, arguments, var=var):
    var = Scope({'whereClause':whereClause, 'parsedQuery':parsedQuery, 'this':this, 'arguments':arguments}, var)
    var.registers(['parsedQuery', 'btQueryStr', 'rateMultiplier', 'limit', 'whereClause', 'btQuery'])
    var.put('rateMultiplier', (Js(1.0)+(var.get('parsedQuery').get('percent')/Js(100.0))))
    var.put('limit', var.get('parsedQuery').get('limit'))
    var.get('parsedQuery').put('columnName', var.get('columnNameC'))
    var.get('parsedQuery').put('hiddenColumnName', var.get('hiddenColumnNameC'))
    def PyJs_LONG_8_(var=var):
        return ((((((((((((((((((Js('SELECT ')+Js('Shape, '))+Js('Size,  '))+Js('Color, '))+Js('Clarity, '))+Js('Cut, '))+Js('Polish, '))+Js('Sym, '))+Js('Flour, '))+Js('ROUND(Rate_US*'))+var.get('rateMultiplier'))+Js(') Rate_US, '))+Js('ROUND((Rate_US*'))+var.get('rateMultiplier'))+Js(')/Size)  USDPerCT, '))+Js('SUBSTR(STRING(100 - '))+var.get('rateMultiplier'))+Js('*(100 - Back)),0, 5) Back, '))+Js('ReportNo, '))
    var.put('btQueryStr', ((((((((((((((((PyJs_LONG_8_()+Js('M1, '))+Js('M2, '))+Js('M3, '))+Js('Depth, '))+Js('[Table], '))+Js('Ref, '))+Js('CertNo, '))+Js('Detail, '))+Js('cert, '))+Js('CompanyCode '))+Js('FROM Diamond_Inv.latest '))+Js(' WHERE Rate_US != 0 AND '))+var.get('whereClause').callprop('join', Js(' AND \n')))+Js(' ORDER BY USDPerCT '))+Js('LIMIT '))+var.get('limit')))
    var.put('btQuery', Js({'query':var.get('btQueryStr')}))
    return var.get('btQuery')
PyJsHoisted_createSimpleQuery__.func_name = 'createSimpleQuery_'
var.put('createSimpleQuery_', PyJsHoisted_createSimpleQuery__)
@Js
def PyJsHoisted_testcreateWhereClause__(userMessage, this, arguments, var=var):
    var = Scope({'userMessage':userMessage, 'this':this, 'arguments':arguments}, var)
    var.registers(['whereClause', 'userMessage'])
    var.put('whereClause', var.get('createWhereClause_')(var.get('queryParser_')(var.get('userMessage'))))
PyJsHoisted_testcreateWhereClause__.func_name = 'testcreateWhereClause_'
var.put('testcreateWhereClause_', PyJsHoisted_testcreateWhereClause__)
@Js
def PyJsHoisted_createWhereClause__(parsedQuery, this, arguments, var=var):
    var = Scope({'parsedQuery':parsedQuery, 'this':this, 'arguments':arguments}, var)
    var.registers(['rateClause', 'parsedQuery', 'BackClause', 'reportNoClause', 'shapeClause', 'clause', 'i', 'whereClause', 'exactMode', 'sizeClause'])
    var.put('whereClause', Js([]))
    var.put('exactMode', Js(False))
    if (var.get('parsedQuery').get('queryMode')==Js('exact')):
        var.put('exactMode', Js(True))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('parsedQuery').get('entityName').get('length')):
        try:
            while 1:
                SWITCHED = False
                CONDITION = (var.get('parsedQuery').get('entityName').get(var.get('i')))
                if SWITCHED or PyJsStrictEq(CONDITION, Js('color')):
                    SWITCHED = True
                    var.put('clause', var.get('getRangeClause_')(Js('color'), var.get('parsedQuery').get('entityValue').get(var.get('i')), var.get('colorRange'), var.get('exactMode')))
                    var.get('whereClause').callprop('push', var.get('clause'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('clarity')):
                    SWITCHED = True
                    var.put('clause', var.get('getRangeClause_')(Js('clarity'), var.get('parsedQuery').get('entityValue').get(var.get('i')), var.get('clarityRange'), var.get('exactMode')))
                    var.get('whereClause').callprop('push', var.get('clause'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('polish')):
                    SWITCHED = True
                    var.put('clause', var.get('getRangeClause_')(Js('polish'), var.get('parsedQuery').get('entityValue').get(var.get('i')), var.get('polishRange'), var.get('exactMode')))
                    var.get('whereClause').callprop('push', var.get('clause'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('sym')):
                    SWITCHED = True
                    var.put('clause', var.get('getRangeClause_')(Js('sym'), var.get('parsedQuery').get('entityValue').get(var.get('i')), var.get('symRange'), var.get('exactMode')))
                    var.get('whereClause').callprop('push', var.get('clause'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('cut')):
                    SWITCHED = True
                    var.put('clause', var.get('getRangeClause_')(Js('cut'), var.get('parsedQuery').get('entityValue').get(var.get('i')), var.get('cutRange'), var.get('exactMode')))
                    var.get('whereClause').callprop('push', var.get('clause'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('flour')):
                    SWITCHED = True
                    var.put('clause', var.get('getRangeClause_')(Js('flour'), var.get('parsedQuery').get('entityValue').get(var.get('i')), var.get('flourRange'), var.get('exactMode')))
                    var.get('whereClause').callprop('push', var.get('clause'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('size')):
                    SWITCHED = True
                    var.put('sizeClause', var.get('getSizeClause_')(var.get('parsedQuery').get('entityValue').get(var.get('i'))))
                    var.get('whereClause').callprop('push', var.get('sizeClause'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('shape')):
                    SWITCHED = True
                    var.put('shapeClause', var.get('getShapeClause_')(var.get('parsedQuery').get('entityValue').get(var.get('i'))))
                    var.get('whereClause').callprop('push', var.get('shapeClause'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('rate_us')):
                    SWITCHED = True
                    var.put('rateClause', var.get('getRateClause_')(var.get('parsedQuery').get('entityValue').get(var.get('i'))))
                    var.get('whereClause').callprop('push', var.get('rateClause'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('back')):
                    SWITCHED = True
                    var.put('BackClause', var.get('getBackClause_')(var.get('parsedQuery').get('entityValue').get(var.get('i'))))
                    var.get('whereClause').callprop('push', var.get('BackClause'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('reportno')):
                    SWITCHED = True
                    var.put('reportNoClause', var.get('getReportNoClause_')(var.get('parsedQuery').get('entityValue').get(var.get('i'))))
                    var.get('whereClause').callprop('push', var.get('reportNoClause'))
                    break
                if True:
                    SWITCHED = True
                    pass
                SWITCHED = True
                break
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('whereClause')
PyJsHoisted_createWhereClause__.func_name = 'createWhereClause_'
var.put('createWhereClause_', PyJsHoisted_createWhereClause__)
@Js
def PyJsHoisted_getRangeClause__(property, valueArray, range, exactMode, this, arguments, var=var):
    var = Scope({'property':property, 'valueArray':valueArray, 'range':range, 'exactMode':exactMode, 'this':this, 'arguments':arguments}, var)
    var.registers(['j', 'valueArray', 'lowerRange', 'range', 'betterRange', 'property', 'exactMode', 'k'])
    var.put('betterRange', (-Js(1.0)))
    var.put('lowerRange', (-Js(1.0)))
    #for JS loop
    var.put('j', Js(0.0))
    while (var.get('j')<var.get('valueArray').get('length')):
        try:
            #for JS loop
            var.put('k', Js(0.0))
            while (var.get('k')<var.get('range').get('length')):
                try:
                    if (var.get('valueArray').get(var.get('j'))==var.get('range').get(var.get('k'))):
                        if (var.get('betterRange')==(-Js(1.0))):
                            var.put('betterRange', var.get('k'))
                        else:
                            var.put('lowerRange', var.get('k'))
                        break
                finally:
                        (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
        finally:
                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
    if (var.get('betterRange')!=(-Js(1.0))):
        var.put('retStr', Js([]))
        if (var.get('lowerRange')==(-Js(1.0))):
            if var.get('exactMode'):
                var.get('retStr').callprop('push', (((var.get('property')+Js(" = '"))+var.get('range').get(var.get('betterRange')).callprop('toUpperCase'))+Js("'")))
            else:
                #for JS loop
                var.put('k', Js(0.0))
                while (var.get('k')<=var.get('betterRange')):
                    try:
                        var.get('retStr').callprop('push', (((var.get('property')+Js(" = '"))+var.get('range').get(var.get('k')).callprop('toUpperCase'))+Js("'")))
                    finally:
                            (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
        else:
            #for JS loop
            var.put('k', var.get('betterRange'))
            while (var.get('k')<=var.get('lowerRange')):
                try:
                    var.get('retStr').callprop('push', (((var.get('property')+Js(" = '"))+var.get('range').get(var.get('k')).callprop('toUpperCase'))+Js("'")))
                finally:
                        (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
        return ((Js('(')+var.get('retStr').callprop('join', Js(' OR ')))+Js(') '))
    return Js('(true)')
PyJsHoisted_getRangeClause__.func_name = 'getRangeClause_'
var.put('getRangeClause_', PyJsHoisted_getRangeClause__)
@Js
def PyJsHoisted_getShapeClause__(valueArray, this, arguments, var=var):
    var = Scope({'valueArray':valueArray, 'this':this, 'arguments':arguments}, var)
    var.registers(['retStr', 'actualShape', 'valueArray', 'i'])
    if (var.get('valueArray').get('length')>Js(0.0)):
        var.put('retStr', Js([]))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('valueArray').get('length')):
            try:
                var.put('actualShape', var.get('getActualShape')(var.get('valueArray').get(var.get('i'))))
                if var.get('actualShape'):
                    var.get('retStr').callprop('push', ((Js("Shape = '")+var.get('actualShape').callprop('toUpperCase'))+Js("'")))
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        return ((Js('(')+var.get('retStr').callprop('join', Js(' OR ')))+Js(')'))
    return Js('(true)')
PyJsHoisted_getShapeClause__.func_name = 'getShapeClause_'
var.put('getShapeClause_', PyJsHoisted_getShapeClause__)
@Js
def PyJsHoisted_getReportNoClause__(valueArray, this, arguments, var=var):
    var = Scope({'valueArray':valueArray, 'this':this, 'arguments':arguments}, var)
    var.registers(['retStr', 'valueArray', 'i'])
    if (var.get('valueArray').get('length')>Js(0.0)):
        var.put('retStr', Js([]))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('valueArray').get('length')):
            try:
                var.get('retStr').callprop('push', ((Js("reportno = '")+var.get('valueArray').get(var.get('i')))+Js("'")))
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        return ((Js('(')+var.get('retStr').callprop('join', Js(' OR ')))+Js(')'))
    return Js('(true)')
PyJsHoisted_getReportNoClause__.func_name = 'getReportNoClause_'
var.put('getReportNoClause_', PyJsHoisted_getReportNoClause__)
@Js
def PyJsHoisted_getSizeClause__(valueArray, this, arguments, var=var):
    var = Scope({'valueArray':valueArray, 'this':this, 'arguments':arguments}, var)
    var.registers(['j', 'secondSize', 'firstSize', 'valueArray'])
    var.put('firstSize', (-Js(1.0)))
    var.put('secondSize', (-Js(1.0)))
    #for JS loop
    var.put('j', Js(0.0))
    while (var.get('j')<var.get('valueArray').get('length')):
        try:
            if var.get('validDecimal_')(var.get('valueArray').get(var.get('j'))):
                if (var.get('firstSize')<Js(0.0)):
                    var.put('firstSize', var.get('valueArray').get(var.get('j')))
                else:
                    var.put('secondSize', var.get('valueArray').get(var.get('j')))
        finally:
                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
    if (var.get('firstSize')>Js(0.0)):
        if (var.get('secondSize')<Js(0.0)):
            return ((Js('(Size = ')+var.get('firstSize'))+Js(')'))
        else:
            if (var.get('firstSize')>var.get('secondSize')):
                return ((((Js('( Size < ')+var.get('firstSize'))+Js(' AND size > '))+var.get('secondSize'))+Js(')'))
            else:
                return ((((Js(' (Size < ')+var.get('secondSize'))+Js(' AND size > '))+var.get('firstSize'))+Js(')'))
    return var.get(u"null")
PyJsHoisted_getSizeClause__.func_name = 'getSizeClause_'
var.put('getSizeClause_', PyJsHoisted_getSizeClause__)
@Js
def PyJsHoisted_getRateClause__(valueArray, this, arguments, var=var):
    var = Scope({'valueArray':valueArray, 'this':this, 'arguments':arguments}, var)
    var.registers(['secondSize', 'firstSize', 'valueArray'])
    if (var.get('valueArray').get('length')==Js(1.0)):
        return ((Js('(Rate_US <= ')+var.get('valueArray').get('0'))+Js(')'))
    else:
        if (var.get('valueArray').get('length')==Js(2.0)):
            var.put('firstSize', var.get('valueArray').get('0'))
            var.put('secondSize', var.get('valueArray').get('1'))
            if (var.get('firstSize')>var.get('secondSize')):
                return ((((Js('(Rate_US <= ')+var.get('firstSize'))+Js(' AND Rate_US >= '))+var.get('secondSize'))+Js(')'))
            else:
                return ((((Js('(Rate_US <= ')+var.get('secondSize'))+Js(' AND Rate_US >= '))+var.get('firstSize'))+Js(')'))
        else:
            return Js('(true)')
PyJsHoisted_getRateClause__.func_name = 'getRateClause_'
var.put('getRateClause_', PyJsHoisted_getRateClause__)
@Js
def PyJsHoisted_getBackClause__(valueArray, this, arguments, var=var):
    var = Scope({'valueArray':valueArray, 'this':this, 'arguments':arguments}, var)
    var.registers(['j', 'secondSize', 'firstSize', 'valueArray'])
    var.put('firstSize', (-Js(1.0)))
    var.put('secondSize', (-Js(1.0)))
    #for JS loop
    var.put('j', Js(0.0))
    while (var.get('j')<var.get('valueArray').get('length')):
        try:
            if var.get('validDecimal_')(var.get('valueArray').get(var.get('j'))):
                if (var.get('firstSize')<Js(0.0)):
                    var.put('firstSize', var.get('valueArray').get(var.get('j')))
                else:
                    var.put('secondSize', var.get('valueArray').get(var.get('j')))
        finally:
                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
    if (var.get('firstSize')>Js(0.0)):
        if (var.get('secondSize')<Js(0.0)):
            return ((Js('(Back > ABS(')+var.get('firstSize'))+Js('))'))
        else:
            if (var.get('firstSize')>var.get('secondSize')):
                return ((((Js('(Back < ABS(')+var.get('firstSize'))+Js(') AND Back > ABS('))+var.get('secondSize'))+Js('))'))
            else:
                return ((((Js('(Back < ABS(')+var.get('secondSize'))+Js(') AND Back > ABS('))+var.get('firstSize'))+Js('))'))
    return var.get(u"null")
PyJsHoisted_getBackClause__.func_name = 'getBackClause_'
var.put('getBackClause_', PyJsHoisted_getBackClause__)
@Js
def PyJsHoisted_validDecimal__(value, this, arguments, var=var):
    var = Scope({'value':value, 'this':this, 'arguments':arguments}, var)
    var.registers(['value'])
    return var.get('isNaN')(var.get('parseFloat')(var.get('value'))).neg()
PyJsHoisted_validDecimal__.func_name = 'validDecimal_'
var.put('validDecimal_', PyJsHoisted_validDecimal__)
@Js
def PyJsHoisted_parseQueryToText_(parsedResult, this, arguments, var=var):
    var = Scope({'parsedResult':parsedResult, 'this':this, 'arguments':arguments}, var)
    var.registers(['j', 'parsedQuery', 'parsedResult', 'entityValue', 'entityValueStr', 'i'])
    var.put('parsedQuery', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('parsedResult').get('entityName').get('length')):
        try:
            var.put('entityValue', var.get('parsedResult').get('entityValue').get(var.get('i')))
            var.put('entityValueStr', Js(''))
            if (var.get('entityValue').get('length')>Js(0.0)):
                #for JS loop
                var.put('j', Js(0.0))
                while (var.get('j')<var.get('entityValue').get('length')):
                    try:
                        var.put('entityValueStr', ((var.get('entityValueStr')+var.get('entityValue').get(var.get('j')))+Js(' ')))
                    finally:
                            (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                var.put('parsedQuery', ((((Js('\n')+var.get('parsedResult').get('entityName').get(var.get('i')))+Js(' = '))+var.get('entityValueStr'))+Js('\t')), '+')
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('parsedQuery')
PyJsHoisted_parseQueryToText_.func_name = 'parseQueryToText'
var.put('parseQueryToText', PyJsHoisted_parseQueryToText_)
@Js
def PyJsHoisted_queryParser__(userMessage, this, arguments, var=var):
    var = Scope({'userMessage':userMessage, 'this':this, 'arguments':arguments}, var)
    var.registers(['parsedResult', 'userMessage'])
    var.put('parsedResult', Js({'userMessage':var.get('userMessage'),'entityName':Js([]),'entityValue':Js([]),'queryMode':Js(''),'unknown':Js(''),'percent':Js(0.0),'limit':Js(30.0)}))
    var.get('console').callprop('log', (Js('0th parse query is:')+var.get('parsedResult').get('userMessage')))
    var.get('setQueryMode')(var.get('parsedResult'))
    while 1:
        SWITCHED = False
        CONDITION = (var.get('parsedResult').get('queryMode'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js('hide')):
            SWITCHED = True
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('show')):
            SWITCHED = True
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('email')):
            SWITCHED = True
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('pdf')):
            SWITCHED = True
            pass
        if SWITCHED or PyJsStrictEq(CONDITION, Js('image')):
            SWITCHED = True
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('video')):
            SWITCHED = True
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('quick-search')):
            SWITCHED = True
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('exact')):
            SWITCHED = True
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('contact')):
            SWITCHED = True
            pass
        if True:
            SWITCHED = True
            pass
        SWITCHED = True
        break
    var.get('parsePointer')(var.get('parsedResult'))
    var.get('replaceHotKeyword_')(var.get('parsedResult'), var.get('sizeKeyword'), var.get('sizeKeywordValue'))
    var.get('replaceHotKeyword_')(var.get('parsedResult'), var.get('multiValueKeyword'), var.get('multiValueKeywordValue'))
    var.get('replaceHotKeyword_')(var.get('parsedResult'), var.get('priceKeyword'), var.get('priceKeywordValue'))
    var.get('replaceHotKeyword_')(var.get('parsedResult'), var.get('clarityKeyword'), var.get('clarityKeywordValue'))
    var.get('replaceHotKeywordSplit_')(var.get('parsedResult'), var.get('sizeKeyword'), var.get('sizeKeywordValue'))
    var.get('replaceHotKeywordSplit_')(var.get('parsedResult'), var.get('multiValueKeyword'), var.get('multiValueKeywordValue'))
    var.get('replaceHotKeywordSplit_')(var.get('parsedResult'), var.get('priceKeyword'), var.get('priceKeywordValue'))
    var.get('replaceHotKeywordSplit_')(var.get('parsedResult'), var.get('clarityKeyword'), var.get('clarityKeywordValue'))
    var.get('parsedResult').put('userMessage', var.get('parsedResult').get('userMessage').callprop('replace', JsRegExp('/(?:\\r\\n|\\r|\\n|<br>)/g'), Js(' ')).callprop('replace', JsRegExp('/\\s\\s+/g'), Js(' ')).callprop('replace', JsRegExp('/[^a-zA-Z\\.0-9\\-+%\\\\ ]/g'), Js(' ')).callprop('replace', JsRegExp('/\\s\\s+/g'), Js(' ')))
    var.get('parseEntityKeyword_')(var.get('parsedResult'), var.get('shapeTypo'), var.get('userShape'))
    var.get('parseEntityKeyword_')(var.get('parsedResult'), var.get('clarityTypo'), var.get('clarityRange'))
    var.get('parseEntityKeyword_')(var.get('parsedResult'), var.get('flourTypo'), var.get('userFlour'))
    var.get('parseEntityKeyword_')(var.get('parsedResult'), var.get('certTypo'), var.get('certRange'))
    var.get('parseEntityKeyword_')(var.get('parsedResult'), var.get('colorTypo'), var.get('colorRange'))
    var.get('parseCPSKeyword_')(var.get('parsedResult'), var.get('cutTypo'))
    var.get('parseCPSKeyword_')(var.get('parsedResult'), var.get('polishTypo'))
    var.get('parseCPSKeyword_')(var.get('parsedResult'), var.get('symTypo'))
    var.get('parsePercent')(var.get('parsedResult'))
    var.get('parseNumberEntityKeyword_')(var.get('parsedResult'), var.get('sizeTypo'))
    var.get('parseNumberEntityKeyword_')(var.get('parsedResult'), var.get('rate_usTypo'))
    var.get('parseNumberEntityKeyword_')(var.get('parsedResult'), var.get('backTypo'))
    var.get('parseNumberEntityKeyword_')(var.get('parsedResult'), var.get('reportNoTypo'))
    var.get('console').callprop('log', (Js('7th parse query is:')+var.get('parsedResult').get('userMessage')))
    return var.get('parsedResult')
PyJsHoisted_queryParser__.func_name = 'queryParser_'
var.put('queryParser_', PyJsHoisted_queryParser__)
@Js
def PyJsHoisted_setQueryMode_(parsedResult, this, arguments, var=var):
    var = Scope({'parsedResult':parsedResult, 'this':this, 'arguments':arguments}, var)
    var.registers(['mode', 'parsedResult', 'userMessage'])
    var.put('userMessage', var.get('parsedResult').get('userMessage'))
    for PyJsTemp in var.get('QueryMode'):
        var.put('mode', PyJsTemp)
        if (var.get('userMessage').callprop('indexOf', var.get('mode'))!=(-Js(1.0))):
            var.get('userMessage').callprop('replace', var.get('mode'), Js(''))
            var.get('parsedResult').put('queryMode', var.get('QueryMode').get(var.get('mode')))
            return var.get('undefined')
    return var.get('undefined')
PyJsHoisted_setQueryMode_.func_name = 'setQueryMode'
var.put('setQueryMode', PyJsHoisted_setQueryMode_)
@Js
def PyJsHoisted_parsePercent_(parsedResult, this, arguments, var=var):
    var = Scope({'parsedResult':parsedResult, 'this':this, 'arguments':arguments}, var)
    var.registers(['percentage', 'parsedResult', 'strNValue'])
    var.put('strNValue', var.get('matchAndReplace')(var.get('parsedResult').get('userMessage'), var.get('percentRegex')))
    if (var.get('strNValue').get('1')==Js('')):
        var.put('strNValue', var.get('matchAndReplace')(var.get('parsedResult').get('userMessage'), var.get('percentCharRegex')))
    if (var.get('strNValue').get('1')!=Js('')):
        var.put('percentage', var.get('Number')(var.get('strNValue').get('1').callprop('slice', Js(0.0), (-Js(1.0)))))
        var.get('parsedResult').put('userMessage', var.get('strNValue').get('0'))
        var.get('parsedResult').put('percent', var.get('percentage'))
PyJsHoisted_parsePercent_.func_name = 'parsePercent'
var.put('parsePercent', PyJsHoisted_parsePercent_)
@Js
def PyJsHoisted_parsePointer_(parsedResult, this, arguments, var=var):
    var = Scope({'parsedResult':parsedResult, 'this':this, 'arguments':arguments}, var)
    var.registers(['parsedResult', 'ptrValue', 'numStr', 'strNValue'])
    var.put('strNValue', var.get('matchAndReplace')(var.get('parsedResult').get('userMessage'), var.get('pointerRegex')))
    if (var.get('strNValue').get('1')!=Js('')):
        var.get('console').callprop('log', (Js('Value:')+var.get('strNValue').get('1')))
        var.put('numStr', var.get('matchAndReplace')(var.get('strNValue').get('1'), var.get('numberRegex')))
        if (var.get('numStr').get('1')!=Js('')):
            var.put('ptrValue', var.get('Number')(var.get('numStr').get('1')))
            if var.get('isNaN')(var.get('ptrValue')).neg():
                if (var.get('ptrValue')>Js(0.9999)):
                    var.put('ptrValue', (var.get('ptrValue')/Js(100.0)))
                var.get('parsedResult').put('userMessage', ((((var.get('strNValue').get('0')+Js(' '))+(var.get('ptrValue')*Js(0.97)))+Js(' '))+(var.get('ptrValue')*Js(1.03))))
PyJsHoisted_parsePointer_.func_name = 'parsePointer'
var.put('parsePointer', PyJsHoisted_parsePointer_)
@Js
def PyJsHoisted_matchAndReplace_(str, pattern, this, arguments, var=var):
    var = Scope({'str':str, 'pattern':pattern, 'this':this, 'arguments':arguments}, var)
    var.registers(['results', 'str', 'result', 'pattern'])
    var.put('results', var.get('str').callprop('match', var.get('pattern')))
    var.put('result', Js(''))
    if (var.get('results')!=var.get(u"null")):
        var.put('result', var.get('results').get('0').callprop('trim'))
        var.put('str', var.get('str').callprop('replace', var.get('result'), Js('')))
    return Js([var.get('str'), var.get('result')])
PyJsHoisted_matchAndReplace_.func_name = 'matchAndReplace'
var.put('matchAndReplace', PyJsHoisted_matchAndReplace_)
@Js
def PyJsHoisted_replaceHotKeyword__(parsedResult, keywords, keywordValues, this, arguments, var=var):
    var = Scope({'parsedResult':parsedResult, 'keywords':keywords, 'keywordValues':keywordValues, 'this':this, 'arguments':arguments}, var)
    var.registers(['keywordValues', 'parsedResult', 'keywords', 'i', 'userMessage'])
    var.put('userMessage', var.get('parsedResult').get('userMessage'))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('keywords').get('length')):
        try:
            if (var.get('userMessage').callprop('indexOf', var.get('keywords').get(var.get('i')))!=(-Js(1.0))):
                var.get('userMessage').callprop('replace', var.get('keywords').get(var.get('i')), var.get('keywordValues').get(var.get('i')))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('undefined')
PyJsHoisted_replaceHotKeyword__.func_name = 'replaceHotKeyword_'
var.put('replaceHotKeyword_', PyJsHoisted_replaceHotKeyword__)
@Js
def PyJsHoisted_replaceHotKeywordSplit__(parsedResult, keywords, keywordValues, this, arguments, var=var):
    var = Scope({'parsedResult':parsedResult, 'keywords':keywords, 'keywordValues':keywordValues, 'this':this, 'arguments':arguments}, var)
    var.registers(['j', 'keywordValues', 'parsedResult', 'keywords', 'i', 'splitQuery', 'userMessage'])
    var.put('userMessage', var.get('parsedResult').get('userMessage'))
    var.put('splitQuery', var.get('userMessage').callprop('split', Js(' ')))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('keywords').get('length')):
        try:
            #for JS loop
            var.put('j', Js(0.0))
            while (var.get('j')<var.get('splitQuery').get('length')):
                try:
                    if (var.get('keywords').get(var.get('i'))==var.get('splitQuery').get(var.get('j'))):
                        var.get('splitQuery').put(var.get('j'), var.get('keywordValues').get(var.get('i')))
                finally:
                        (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.get('parsedResult').put('userMessage', var.get('splitQuery').callprop('join', Js(' ')))
    return var.get('undefined')
PyJsHoisted_replaceHotKeywordSplit__.func_name = 'replaceHotKeywordSplit_'
var.put('replaceHotKeywordSplit_', PyJsHoisted_replaceHotKeywordSplit__)
@Js
def PyJsHoisted_parseEntityKeyword__(parsedResult, typoArray, userValues, this, arguments, var=var):
    var = Scope({'parsedResult':parsedResult, 'typoArray':typoArray, 'userValues':userValues, 'this':this, 'arguments':arguments}, var)
    var.registers(['j', 'parsedResult', 'returnClause', 'splitQuery', 'values', 'typoArray', 'userValue', 'keywordReplace', 'userMessage', 'userValues', 'correctSpell', 'i', 'typo', 'valueReplace'])
    var.put('userMessage', var.get('parsedResult').get('userMessage'))
    var.put('keywordReplace', Js(False))
    var.put('valueReplace', Js(False))
    var.put('values', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('typoArray').get('length')):
        try:
            var.put('typo', var.get('typoArray').get(var.get('i')))
            if (var.get('userMessage').callprop('indexOf', var.get('typo'))!=(-Js(1.0))):
                var.put('correctSpell', var.get('typoArray').get('0'))
                var.put('userMessage', var.get('userMessage').callprop('replace', (var.get('typo')+Js('= ')), Js('')))
                var.put('userMessage', var.get('userMessage').callprop('replace', (var.get('typo')+Js(': ')), Js(' ')))
                var.put('userMessage', var.get('userMessage').callprop('replace', (var.get('typo')+Js(' ')), Js(' ')))
                var.put('keywordReplace', Js(True))
                break
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('returnClause', Js(''))
    if var.get('userValues'):
        var.put('splitQuery', var.get('userMessage').callprop('split', Js(' ')))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('userValues').get('length')):
            try:
                var.put('userValue', var.get('userValues').get(var.get('i')))
                #for JS loop
                var.put('j', Js(0.0))
                while (var.get('j')<var.get('splitQuery').get('length')):
                    try:
                        if (var.get('userValue')==var.get('splitQuery').get(var.get('j'))):
                            var.get('splitQuery').put(var.get('j'), Js(' '))
                            var.get('values').callprop('push', var.get('userValue'))
                            var.put('valueReplace', Js(True))
                    finally:
                            (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    if var.get('valueReplace'):
        var.get('parsedResult').put('userMessage', var.get('splitQuery').callprop('join', Js(' ')))
        var.get('parsedResult').get('entityName').callprop('push', var.get('typoArray').get('0'))
        var.get('parsedResult').get('entityValue').callprop('push', var.get('values'))
    return var.get('undefined')
PyJsHoisted_parseEntityKeyword__.func_name = 'parseEntityKeyword_'
var.put('parseEntityKeyword_', PyJsHoisted_parseEntityKeyword__)
@Js
def PyJsHoisted_parseCPSKeyword__(parsedResult, typoArray, this, arguments, var=var):
    var = Scope({'parsedResult':parsedResult, 'typoArray':typoArray, 'this':this, 'arguments':arguments}, var)
    var.registers(['j', 'parsedResult', 'returnClause', 'splitQuery', 'values', 'typoArray', 'userValue', 'userValues', 'userMessage', 'i', 'typo', 'valueReplace'])
    var.put('userValues', Js([Js('ex'), Js('vg'), Js('g')]))
    var.put('userMessage', var.get('parsedResult').get('userMessage'))
    var.put('valueReplace', Js(False))
    var.put('values', Js([]))
    #for JS loop
    var.put('j', Js(0.0))
    while (var.get('j')<var.get('userValues').get('length')):
        try:
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('typoArray').get('length')):
                try:
                    var.put('typo', var.get('typoArray').get(var.get('i')))
                    if (var.get('userMessage').callprop('indexOf', ((var.get('typo')+Js(' '))+var.get('userValues').get(var.get('j'))))!=(-Js(1.0))):
                        var.put('userMessage', var.get('userMessage').callprop('replace', ((var.get('typo')+Js(' '))+var.get('userValues').get(var.get('j'))), Js(' ')))
                        var.get('parsedResult').put('userMessage', var.get('userMessage'))
                        var.get('parsedResult').get('entityName').callprop('push', var.get('typoArray').get('0'))
                        var.get('parsedResult').get('entityValue').callprop('push', Js([var.get('userValues').get(var.get('j'))]))
                        return var.get('undefined')
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        finally:
                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
    var.put('returnClause', Js(''))
    var.put('splitQuery', var.get('userMessage').callprop('split', Js(' ')))
    #for JS loop
    var.put('i', Js(0.0))
    while ((var.get('i')<var.get('userValues').get('length')) and (var.get('valueReplace')==Js(False))):
        try:
            var.put('userValue', var.get('userValues').get(var.get('i')))
            #for JS loop
            var.put('j', Js(0.0))
            while (var.get('j')<var.get('splitQuery').get('length')):
                try:
                    if (var.get('userValue')==var.get('splitQuery').get(var.get('j'))):
                        var.get('splitQuery').put(var.get('j'), Js(' '))
                        var.get('values').callprop('push', var.get('userValue'))
                        var.put('valueReplace', Js(True))
                        break
                finally:
                        (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    if var.get('valueReplace'):
        var.get('parsedResult').put('userMessage', var.get('splitQuery').callprop('join', Js(' ')))
        var.get('parsedResult').get('entityName').callprop('push', var.get('typoArray').get('0'))
        var.get('parsedResult').get('entityValue').callprop('push', var.get('values'))
    return var.get('undefined')
PyJsHoisted_parseCPSKeyword__.func_name = 'parseCPSKeyword_'
var.put('parseCPSKeyword_', PyJsHoisted_parseCPSKeyword__)
@Js
def PyJsHoisted_parseNumberEntityKeyword__(parsedResult, typoArray, this, arguments, var=var):
    var = Scope({'parsedResult':parsedResult, 'typoArray':typoArray, 'this':this, 'arguments':arguments}, var)
    var.registers(['parsedResult', 'strNumZeroK', 'values', 'splituserMessage', 'typoArray', 'keywordReplace', 'userMessage', 'strQuery', 'strNumK', 'i', 'typo', 'strNum', 'valueReplace', 'parsedNumber'])
    var.put('userMessage', var.get('parsedResult').get('userMessage').callprop('replace', JsRegExp('/\\s+/g'), Js(' ')))
    var.put('keywordReplace', Js(False))
    var.put('valueReplace', Js(False))
    var.put('values', Js([]))
    var.put('splituserMessage', var.get('userMessage').callprop('split', Js(' ')))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('splituserMessage').get('length')):
        try:
            var.put('strQuery', var.get('splituserMessage').get(var.get('i')))
            var.put('parsedNumber', var.get('Number')(var.get('strQuery').callprop('replace', JsRegExp('/[^0-9\\.]+/g'), Js(''))))
            var.put('strNum', (var.get('parsedNumber')+Js('')))
            var.put('strNumK', (var.get('parsedNumber')+Js('k')))
            var.put('strNumZeroK', (var.get('parsedNumber')+Js('0k')))
            if ((var.get('parsedNumber')<Js(0.0001)) and (var.get('parsedNumber')>(-Js(0.0001)))):
                continue
            if ((var.get('strQuery')==var.get('strNumK')) or (var.get('strQuery')==var.get('strNumZeroK'))):
                var.put('parsedNumber', (var.get('parsedNumber')*Js(1000.0)))
            else:
                if (((((var.get('strQuery')==var.get('strNum')) or (var.get('strQuery')==(var.get('strNum')+Js('0')))) or ((Js('0')+var.get('strQuery'))==var.get('strNum'))) or (var.get('strQuery')==(var.get('strNum')+Js('.0')))) or (var.get('strQuery')==(var.get('strNum')+Js('.00')))):
                    pass
                else:
                    continue
            if ((var.get('typoArray').get('0')==Js('size')) and (var.get('parsedNumber')<Js(15.0))):
                var.put('userMessage', var.get('userMessage').callprop('replace', var.get('strNum'), Js(' ')))
                var.get('values').callprop('push', var.get('parsedNumber'))
                var.put('valueReplace', Js(True))
            if (((var.get('typoArray').get('0')==Js('back')) and (var.get('parsedNumber')>Js(15.0))) and (var.get('parsedNumber')<Js(80.0))):
                var.put('userMessage', var.get('userMessage').callprop('replace', var.get('strNum'), Js(' ')))
                var.get('values').callprop('push', var.get('parsedNumber'))
                var.put('valueReplace', Js(True))
            if (((var.get('typoArray').get('0')==Js('rate_us')) and (var.get('parsedNumber')>Js(200.0))) and (var.get('parsedNumber')<Js(900000.0))):
                var.put('userMessage', var.get('userMessage').callprop('replace', var.get('strNum'), Js(' ')))
                var.put('userMessage', var.get('userMessage').callprop('replace', var.get('strNumK'), Js(' ')))
                var.put('userMessage', var.get('userMessage').callprop('replace', var.get('strNumZeroK'), Js(' ')))
                if (var.get('parsedNumber')>Js(250.0)):
                    var.get('values').callprop('push', var.get('parsedNumber'))
                    var.put('valueReplace', Js(True))
            if (((var.get('typoArray').get('0')==Js('reportno')) and (var.get('parsedNumber')>Js(100000000.0))) and (var.get('parsedNumber')<Js(10000000000.0))):
                var.put('userMessage', var.get('userMessage').callprop('replace', var.get('strNum'), Js(' ')))
                var.get('values').callprop('push', var.get('parsedNumber'))
                var.put('valueReplace', Js(True))
            else:
                var.get('parsedResult').put('unknown', (Js(' ')+var.get('parsedNumber')), '+')
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    if var.get('valueReplace'):
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('typoArray').get('length')):
            try:
                var.put('typo', var.get('typoArray').get(var.get('i')))
                if (var.get('userMessage').callprop('indexOf', var.get('typo'))!=(-Js(1.0))):
                    var.put('userMessage', var.get('userMessage').callprop('replace', (var.get('typo')+Js(' ')), Js(' ')))
                    var.put('keywordReplace', Js(True))
                    break
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        var.get('parsedResult').put('userMessage', var.get('userMessage'))
        var.get('parsedResult').get('entityName').callprop('push', var.get('typoArray').get('0'))
        var.get('parsedResult').get('entityValue').callprop('push', var.get('values'))
    return var.get('undefined')
PyJsHoisted_parseNumberEntityKeyword__.func_name = 'parseNumberEntityKeyword_'
var.put('parseNumberEntityKeyword_', PyJsHoisted_parseNumberEntityKeyword__)
var.put('projectId', Js('cloudstoragehelloworld'))
var.put('labelName', Js('AddedToBigQuery'))
var.put('dryRun', Js(False))
var.put('datasetId2', Js('dharam_test'))
var.put('companyDir', Js([Js('dharam'), Js('kiran'), Js('rk'), Js('srk')]))
var.put('dharamIndex', Js(0.0))
var.put('kiranIndex', Js(1.0))
var.put('rkIndex', Js(2.0))
var.put('srkIndex', Js(3.0))
var.put('companydatasetId', Js([Js('Dharam_Inv'), Js('Kiran_Inv'), Js('RK_Inv'), Js('SRK_Inv')]))
var.put('companyCode', Js([Js('DHM'), Js('KIRAN'), Js('RK'), Js('SRK')]))
var.put('percentRegex', JsRegExp('/[\\+\\-]?[0-9\\.]+(%|p)/g'))
var.put('percentCharRegex', JsRegExp('/[\\+\\-]?[0-9\\.]+\\s+(pct|percent)/g'))
var.put('pointerRegex', JsRegExp('/[0-9\\.]+\\s+(pointers|ptr|pointer|pt|point)/g'))
var.put('numberRegex', JsRegExp('/[0-9\\.]+/g'))
var.put('columnNameC', Js([Js('Shape'), Js('Size'), Js('Color'), Js('Clarity'), Js('Cut'), Js('Polish'), Js('Sym'), Js('Flour'), Js('Rate_US'), Js('USDPerCT'), Js('Back')]))
var.put('hiddenColumnNameC', Js([Js('ReportNo'), Js('M1'), Js('M2'), Js('M3'), Js('Depth'), Js('Table'), Js('Ref'), Js('CertNo'), Js('Detail'), Js('cert'), Js('CompanyCode')]))
var.put('colorRange', Js([Js('d'), Js('e'), Js('f'), Js('g'), Js('h'), Js('i'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('o'), Js('p'), Js('q')]))
var.put('clarityRange', Js([Js('fl'), Js('if'), Js('vvs1'), Js('vvs2'), Js('vs1'), Js('vs2'), Js('si1'), Js('si2'), Js('i1'), Js('i2'), Js('i3')]))
var.put('polishRange', Js([Js('ex'), Js('vg')]))
var.put('symRange', Js([Js('ex'), Js('vg')]))
var.put('cutRange', Js([Js('ex'), Js('vg')]))
var.put('flourRange', Js([Js('none'), Js('faint'), Js('medium'), Js('strong'), Js('very strong')]))
var.put('shapeRange', Js([Js('round'), Js('marquise'), Js('princess'), Js('pear'), Js('oval'), Js('heart'), Js('cushion modified'), Js('cushion'), Js('ashcher'), Js('radiant')]))
var.put('certRange', Js([Js('gia'), Js('hrd'), Js('igi'), Js('fm')]))
var.put('userShape', Js([Js('round'), Js('rd'), Js('r'), Js('br'), Js('rb'), Js('rbb'), Js('marquise'), Js('mr'), Js('mq'), Js('mar'), Js('princess'), Js('pr'), Js('pc'), Js('pear'), Js('paer'), Js('per'), Js('ps'), Js('oval'), Js('ov'), Js('heart'), Js('hrt'), Js('love'), Js('cushion modified'), Js('cmb'), Js('cm'), Js('cushion'), Js('cus'), Js('cu'), Js('ashcher'), Js('as'), Js('radiant'), Js('rad'), Js('emerald'), Js('em'), Js('emrd')]))
var.put('actualShape', Js([Js('round'), Js('round'), Js('round'), Js('round'), Js('round'), Js('round'), Js('marquise'), Js('marquise'), Js('marquise'), Js('marquise'), Js('princess'), Js('princess'), Js('princess'), Js('pear'), Js('pear'), Js('pear'), Js('pear'), Js('oval'), Js('oval'), Js('heart'), Js('heart'), Js('heart'), Js('cushion modified'), Js('cushion modified'), Js('cushion modified'), Js('cushion'), Js('cushion'), Js('cushion'), Js('ashcher'), Js('ashcher'), Js('radiant'), Js('radiant'), Js('emerald'), Js('emerald'), Js('emerald')]))
var.put('userFlour', Js([Js('none'), Js('non'), Js('no'), Js('nan'), Js('strong'), Js('stg'), Js('very strong'), Js('vst'), Js('vstg'), Js('medium'), Js('med'), Js('faint'), Js('fnt'), Js('faint')]))
var.put('actualFlour', Js([Js('none'), Js('none'), Js('none'), Js('none'), Js('none'), Js('strong'), Js('strong'), Js('very strong'), Js('very strong'), Js('very strong'), Js('medium'), Js('medium'), Js('faint'), Js('faint'), Js('faint')]))
var.put('sizeKeyword', Js([Js('quaters'), Js('quater'), Js('quarters'), Js('quarter'), Js('1/4'), Js('forth'), Js('4th'), Js('thirds'), Js('third'), Js('1/3'), Js('3rd'), Js('3/8'), Js('halfs'), Js('half'), Js('1/2'), Js('fifth'), Js('fifths'), Js('1/5'), Js('1/6')]))
var.put('sizeKeywordValue', Js([Js('size 0.23 0.27'), Js('size 0.23 0.27'), Js('size 0.23 0.27'), Js('size 0.23 0.27'), Js('size 0.23 0.27'), Js('size 0.23 0.27'), Js('size 0.23 0.27'), Js('size 0.32 0.35'), Js('size 0.32 0.35'), Js('size 0.32 0.35'), Js('size 0.32 0.35'), Js('size 0.36 0.39'), Js('size 0.48 0.52'), Js('size 0.48 0.52'), Js('size 0.48 0.52'), Js('size 0.19 0.21'), Js('size 0.19 0.21'), Js('size 0.19 0.21'), Js('size 0.16 0.18')]))
var.put('sizeRange', Js([Js(0.01), Js(0.18), Js(0.23), Js(0.3), Js(0.37), Js(0.45), Js(0.52), Js(0.6), Js(0.66), Js(0.75), Js(0.83), Js(0.96), Js(1.1), Js(1.37), Js(1.7), Js(2.0), Js(10.0)]))
var.put('multiValueKeyword', Js([Js('xxx'), Js('3x'), Js('3ex'), Js('2x'), Js('2ex'), Js('xx'), Js('3vg'), Js('3vg+')]))
var.put('multiValueKeywordValue', Js([Js('cut ex polish ex sym ex'), Js('cut ex polish ex sym ex'), Js('cut ex polish ex sym ex'), Js('cut ex polish ex'), Js('cut ex polish ex'), Js('cut ex polish ex'), Js('cut vg polish vg sym vg'), Js('cut vg polish vg sym vg')]))
var.put('priceKeyword', Js([Js('1 grand'), Js('2 grand'), Js('3 grand'), Js('4 grand'), Js('5 grand'), Js('6 grand'), Js('7 grand'), Js('8 grand'), Js('9 grand'), Js('10 grand')]))
var.put('priceKeywordValue', Js([Js('1000'), Js('2000'), Js('3000'), Js('4000'), Js('5000'), Js('6000'), Js('7000'), Js('8000'), Js('9000'), Js('10000')]))
var.put('cutKeyword', Js([Js('quarter')]))
var.put('cutKeywordValue', Js([Js('0.23 0.25')]))
var.put('polishKeyword', Js([Js('quarter')]))
var.put('polishKeywordValue', Js([Js('0.23 0.25')]))
var.put('clarityKeyword', Js([Js('eye clean'), Js('eyeclean'), Js('vvs'), Js('vs'), Js('si'), Js('pk'), Js('pique')]))
var.put('clarityKeywordValue', Js([Js('clarity vs1'), Js('clarity vs1'), Js('clarity vvs1 vvs2'), Js('clarity vs2 vs1'), Js('clarity si1 si2'), Js('i1 i2 i3'), Js('i1 i2 i3')]))
var.put('QueryMode', Js({'remove':Js('hide'),'delete':Js('hide'),'hide':Js('hide'),'add':Js('show'),'unhide':Js('show'),'show':Js('show'),'sort':Js('sort'),'order':Js('sort'),'limit':Js('limit'),'rows':Js('limit'),'rows':Js('limit'),'count':Js('limit'),'more':Js('more'),'next':Js('more'),'email':Js('email'),'mail':Js('email'),'csv':Js('csv'),'attach':Js('csv'),'attachment':Js('csv'),'image':Js('image'),'video':Js('video'),'exact':Js('exact'),'match':Js('exact'),'exat':Js('exact'),'same':Js('exact'),'specific':Js('exact'),'ditto':Js('exact'),'equal':Js('exact'),'like':Js('exact'),'qs':Js('quick-search'),'fs':Js('quick-search'),'quickSearch':Js('quick-search'),'fastSearch':Js('quick-search')}))
var.put('columnName', Js({'shape':Js('Shape'),'size':Js('Size'),'color':Js('Color'),'clarity':Js('Clarity'),'cut':Js('Cut'),'polish':Js('Polish'),'sym':Js('Sym'),'flour':Js('Flour'),'m1':Js('M1'),'m2':Js('M2'),'m3':Js('M3'),'depth':Js('Depth'),'table':Js('Table'),'ref':Js('Ref'),'certno':Js('CertNo'),'detail':Js('Detail'),'cert':Js('cert'),'raprate':Js('RapRate'),'back':Js('Back'),'rate_us':Js('Rate_US'),'USDPerCT':Js('USDPerCT'),'reportno':Js('ReportNo'),'companyCode':Js('CompanyCode')}))
@Js
def PyJs_anonymous_0_(inputShape, this, arguments, var=var):
    var = Scope({'inputShape':inputShape, 'this':this, 'arguments':arguments}, var)
    var.registers(['j', 'inputShape'])
    #for JS loop
    var.put('j', Js(0.0))
    while (var.get('j')<var.get('userShape').get('length')):
        try:
            if (var.get('userShape').get(var.get('j'))==var.get('inputShape').callprop('trim')):
                return var.get('actualShape').get(var.get('j'))
        finally:
                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
    return var.get(u"null")
PyJs_anonymous_0_._set_name('anonymous')
var.put('getActualShape', PyJs_anonymous_0_)
@Js
def PyJs_anonymous_1_(inputFlour, this, arguments, var=var):
    var = Scope({'inputFlour':inputFlour, 'this':this, 'arguments':arguments}, var)
    var.registers(['j', 'inputFlour'])
    #for JS loop
    var.put('j', Js(0.0))
    while (var.get('j')<var.get('userFlour').get('length')):
        try:
            if (var.get('userFlour').get(var.get('j'))==var.get('inputFlour').callprop('trim')):
                return var.get('actualFlour').get(var.get('j'))
        finally:
                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
    return var.get(u"null")
PyJs_anonymous_1_._set_name('anonymous')
var.put('getActualFlour', PyJs_anonymous_1_)
var.put('sizeTypo', Js([Js('size'), Js('weight'), Js('weigh'), Js('wieght'), Js('wiegh'), Js('ize'), Js('sz'), Js('sioze'), Js('sized'), Js('sizse'), Js('sizes')]))
var.put('colorTypo', Js([Js('color'), Js('olor'), Js('clor'), Js('coor'), Js('colr'), Js('colo'), Js('ccolor'), Js('coolor'), Js('collor'), Js('coloor'), Js('colorr'), Js('oclor'), Js('cloor'), Js('coolr'), Js('colro')]))
var.put('clarityTypo', Js([Js('clarity'), Js('larity'), Js('carity'), Js('clrity'), Js('claity'), Js('clarty'), Js('clariy'), Js('clarit'), Js('cclarity'), Js('cllarity'), Js('claarity'), Js('clarrity'), Js('clariity'), Js('claritty'), Js('clarityy'), Js('lcarity'), Js('clarityrange')]))
var.put('cutTypo', Js([Js('cut'), Js('ut'), Js('ct'), Js('cu'), Js('ccut'), Js('cuut'), Js('cutt'), Js('uct'), Js('ctu'), Js('cyt')]))
var.put('polishTypo', Js([Js('polish')]))
var.put('symTypo', Js([Js('sym'), Js('symmetry'), Js('symetry'), Js('simmetry'), Js('ym'), Js('sm'), Js('sy'), Js('ssym'), Js('syym'), Js('symm'), Js('syymmetry'), Js('symmmetry'), Js('symmmetry')]))
var.put('flourTypo', Js([Js('flour'), Js('fluor'), Js('fluorescent'), Js('lour'), Js('four'), Js('flur'), Js('flor'), Js('flou'), Js('fflour'), Js('fllour'), Js('flpour')]))
var.put('depthTypo', Js([Js('depth'), Js('epth'), Js('dpth'), Js('deth'), Js('deph'), Js('dept'), Js('ddepth'), Js('deepth'), Js('ddept'), Js('dedpt'), Js('dsept'), Js('despt'), Js('deopt'), Js('depot'), Js('de0pt'), Js('dep0t'), Js('delpt'), Js('deplt'), Js('deprt'), Js('deptr'), Js('dep5t'), Js('dept5'), Js('dep6t'), Js('dept6'), Js('depyt'), Js('depty'), Js('depht'), Js('depth'), Js('depgt'), Js('deptg'), Js('depft')]))
var.put('tableTypo', Js([Js('table'), Js('able'), Js('tble'), Js('tale'), Js('tabe'), Js('tabl')]))
var.put('certTypo', Js([Js('cert'), Js('certificate'), Js('ert'), Js('ert'), Js('crt'), Js('cerrt'), Js('cfert'), Js('cefrt'), Js('cdert'), Js('cedrt'), Js('csert'), Js('cesrt'), Js('ceert'), Js('ceret'), Js('ce4rt'), Js('cer4t'), Js('ce5rt'), Js('cer5t'), Js('cetrt'), Js('certt'), Js('cegrt'), Js('cergt'), Js('cefrt'), Js('cerft'), Js('cedrt'), Js('cerdt'), Js('cerrt'), Js('certr'), Js('cer5t'), Js('cert5'), Js('cer6t'), Js('cert6'), Js('ceryt'), Js('certy'), Js('cerht'), Js('certh'), Js('cergt'), Js('certrange'), Js('cerft'), Js('certf'), Js('ertificate'), Js('crtificate'), Js('cetificate'), Js('cerificate'), Js('certficate'), Js('certiicate'), Js('certifcate'), Js('certifiate'), Js('certificte'), Js('certificae'), Js('certificat'), Js('ccertificate'), Js('ceertificate'), Js('cerrtificate'), Js('certtificate'), Js('certiificate'), Js('certifficate'), Js('certifiicate'), Js('certificcate'), Js('certificaate'), Js('certificatte'), Js('certificatee'), Js('ecrtificate'), Js('cretificate'), Js('cetrificate'), Js('ceritficate'), Js('certfiicate'), Js('certiifcate'), Js('certifciate'), Js('certifiacte'), Js('certifictae'), Js('certificaet'), Js('xertificate'), Js('dertificate'), Js('fertificate'), Js('vertificate'), Js('cwrtificate'), Js('certeficated'), Js('certeficatse'), Js('certeficates')]))
var.put('rapRateTypo', Js([Js('raprate'), Js('aprate'), Js('aprate'), Js('rprate'), Js('rarate'), Js('rapate'), Js('raprte'), Js('raprae'), Js('rates'), Js('rate')]))
var.put('backTypo', Js([Js('back'), Js('discount'), Js('off'), Js('%'), Js('ack'), Js('ack'), Js('bck'), Js('bak')]))
var.put('rate_usTypo', Js([Js('rate_us'), Js('price'), Js('prise'), Js('value'), Js('cost'), Js('dollar'), Js('rate'), Js('rate us'), Js('raste us'), Js('rxate us'), Js('raxte us'), Js('rzate us'), Js('razte us'), Js('rarte us'), Js('ratre us'), Js('ra5te us'), Js('rat5e us'), Js('ra6te us'), Js('rat6e us'), Js('rayte us'), Js('ratye us'), Js('rahte us'), Js('rathe us'), Js('ragte us'), Js('ratge us'), Js('rafte us'), Js('ratfe us'), Js('ratwe us'), Js('ratew us'), Js('rat3e us'), Js('rate3 us'), Js('rat4e us'), Js('rate4 us'), Js('ratre us'), Js('rater us'), Js('ratfe us'), Js('ratef us'), Js('ratde us'), Js('rated us'), Js('ratse us'), Js('rates us'), Js('price'), Js('rice'), Js('pice'), Js('prce'), Js('prie'), Js('pric'), Js('pprice'), Js('dollar'), Js('dopllar'), Js('dlollar'), Js('dolllar'), Js('dkollar'), Js('dokllar'), Js('dokllar'), Js('dolklar'), Js('doollar'), Js('dololar'), Js('dopllar'), Js('dolplar'), Js('dolklar'), Js('dollkar'), Js('dololar'), Js('dolloar'), Js('dolplar'), Js('dollpar'), Js('dollqar'), Js('dollaqr'), Js('dollwar'), Js('dollawr'), Js('dollsar'), Js('dollasr'), Js('dollxar'), Js('dollaxr'), Js('dollzar'), Js('dollazr'), Js('dollaer'), Js('dollare'), Js('dolla4r'), Js('dollar4'), Js('dolla5r'), Js('dollar5'), Js('dollatr'), Js('dollart'), Js('dollagr'), Js('dollarg'), Js('dollafr'), Js('dollarf'), Js('dolladr'), Js('dollard'), Js('value'), Js('valued'), Js('valuse'), Js('values')]))
var.put('reportNoTypo', Js([Js('reportno')]))
var.put('shapeTypo', Js([Js('shape'), Js('shepe'), Js('shapw')]))
def PyJs_LONG_5_(var=var):
    def PyJs_LONG_4_(var=var):
        def PyJs_LONG_3_(var=var):
            def PyJs_LONG_2_(var=var):
                return (((((((((Js('How To:\n\n')+Js('Search:\n You can input search string '))+Js('by specifying values of 4Cs of diamond '))+Js('you are looking for seperated by space.\n'))+Js('On top of that you can also add different '))+Js('values for fluorescence, price in USD, one or more '))+Js('GIA report number.\n'))+Js(' Some of the example queries are:\n'))+Js('"rd 6k xxx E F 1.0"\n'))+Js('"si1 vs1 0.98 1.05 D H 3x none rd"\n'))
            return (((((((PyJs_LONG_2_()+Js('"Round Princess xxx  si 1/2  I 3x medium 3000 4000"\n'))+Js('"I2 pk 75 pointer D H 3vg medium 2.7k"\n'))+Js('Note: Each of the Diamond result shown will have parameter '))+Js('either equal or better than what you asked for in search.\n'))+Js('If you looking for exact search, you can add "exact" keyword to search query.\n'))+Js('Example: "exact vvs1 g h rd"\n\n'))+Js('Quick-Search:\n You can also do quick search messaging "quick-search" or just "qs"\n'))
        return (((((PyJs_LONG_3_()+Js('It will show you table with broad catagories and corresponding count for \n'))+Js('each stone as well as minimum price and maximum price for that category.\n\n'))+Js('Show/Hide Columns:\n On quick-search table you can click on any cell to perform corresponding search.\n'))+Js('Once you get search result in table you add show/hide additional column. \n'))+Js('Example: "show m1 m2 m3" (this will show additional columns with measurements for stone)\n'))
    return ((((((PyJs_LONG_4_()+Js('Similarly you can hide column by specifying column names.\n\n'))+Js('Change Price:\n You just specify percentage after the search result, and it will add/decreae \n'))+Js('that percent from USD rate and update the back and cost per carat column\n'))+Js('Example: "5%" or "-2%"\n\n'))+Js('Email:\n'))+Js('Just enter any email address and it will send last search result in email.\n'))
var.put('helpStr', (PyJs_LONG_5_()+Js('Example: "sales@anikadiamond.com" \n')))
@Js
def PyJs_anonymous_6_(userRequest, this, arguments, var=var):
    var = Scope({'userRequest':userRequest, 'this':this, 'arguments':arguments}, var)
    var.registers(['emailAddr', 'parsedQuery', 'simpleQuery', 'userRequest', 'columnNames', 'splittedUserRequest', 'i', 'whereClause', 'userMessage'])
    var.put('userRequest', var.get('userRequest').callprop('toLowerCase').callprop('replace', JsRegExp('/\\s\\s+/g'), Js(' ')).callprop('trim'))
    if (var.get('userRequest')==Js('help')):
        return Js({'userMessage':var.get('helpStr'),'queryMode':Js('help')})
    if (var.get('userRequest')==Js('cache')):
        return Js({'userMessage':Js('cache object is'),'queryMode':Js('cache')})
    if ((((((var.get('userRequest')==Js('quick search')) or (var.get('userRequest')==Js('fast search'))) or (var.get('userRequest')==Js('quick-search'))) or (var.get('userRequest')==Js('fast-search'))) or (var.get('userRequest')==Js('qs'))) or (var.get('userRequest')==Js('fs'))):
        return Js({'queryMode':Js('quick-search')})
    def PyJs_LONG_7_(var=var):
        return ((((var.get('userRequest').callprop('indexOf', Js('hide'))!=(-Js(1.0))) or (var.get('userRequest').callprop('indexOf', Js('remove'))!=(-Js(1.0)))) or (var.get('userRequest').callprop('indexOf', Js('delete'))!=(-Js(1.0)))) or (((var.get('userRequest').callprop('indexOf', Js('show'))!=(-Js(1.0))) or (var.get('userRequest').callprop('indexOf', Js('add'))!=(-Js(1.0)))) or (var.get('userRequest').callprop('indexOf', Js('unhide'))!=(-Js(1.0)))))
    if PyJs_LONG_7_():
        var.put('columnNames', Js([]))
        var.put('splittedUserRequest', var.get('userRequest').callprop('split', Js(' ')))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('columnNameC').get('length')):
            try:
                if (var.get('splittedUserRequest').callprop('indexOf', var.get('columnNameC').get(var.get('i')).callprop('toLowerCase'))!=(-Js(1.0))):
                    var.get('columnNames').callprop('push', var.get('columnNameC').get(var.get('i')))
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('hiddenColumnNameC').get('length')):
            try:
                if (var.get('splittedUserRequest').callprop('indexOf', var.get('hiddenColumnNameC').get(var.get('i')).callprop('toLowerCase'))!=(-Js(1.0))):
                    var.get('columnNames').callprop('push', var.get('hiddenColumnNameC').get(var.get('i')))
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        if (((var.get('userRequest').callprop('indexOf', Js('show'))!=(-Js(1.0))) or (var.get('userRequest').callprop('indexOf', Js('add'))!=(-Js(1.0)))) or (var.get('userRequest').callprop('indexOf', Js('unhide'))!=(-Js(1.0)))):
            return Js({'columnNameArray':var.get('columnNames'),'queryMode':Js('show')})
        else:
            return Js({'columnNameArray':var.get('columnNames'),'queryMode':Js('hide')})
    var.put('parsedQuery', var.get('queryParser_')(var.get('userRequest')))
    if (var.get('parsedQuery').get('entityName').get('length')==Js(0.0)):
        var.put('emailAddr', var.get('userRequest').callprop('match', JsRegExp('/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\\.[a-zA-Z0-9._-]+)/gi')))
        if ((var.get('userRequest').callprop('indexOf', Js('mail'))!=(-Js(1.0))) or var.get('emailAddr')):
            var.put('userMessage', Js(''))
            if (var.get('emailAddr')==Js('')):
                var.put('userMessage', Js('Please provide valid email ID'))
            return Js({'email':var.get('emailAddr'),'userMessage':var.get('userMessage'),'queryMode':Js('email')})
        if var.get('parsedQuery').get('percent'):
            return Js({'percent':var.get('parsedQuery').get('percent'),'constUsd':Js(0.0),'queryMode':Js('changeRate')})
        return Js({'userMessage':Js('Your Query is invalid, message/search "help" for usage instructions.'),'queryMode':Js('help')})
    var.put('whereClause', var.get('createWhereClause_')(var.get('parsedQuery')))
    var.put('simpleQuery', var.get('createSimpleQuery_')(var.get('whereClause'), var.get('parsedQuery')))
    return Js({'condition':var.get('parseQueryToText')(var.get('parsedQuery')),'parsedQuery':var.get('parsedQuery'),'query':var.get('simpleQuery').get('query'),'queryMode':Js('btQuery')})
PyJs_anonymous_6_._set_name('anonymous')
var.put('parseUserRequest', PyJs_anonymous_6_)
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
queryParsing = var.to_python()