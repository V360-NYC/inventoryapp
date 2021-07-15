__all__ = ['index']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
from js2py import require
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['admin', 'sendSearchResultEmail', 'fs', 'cloudconvert', 'quickSearchRespond', 'cors', 'queryAndSendBQResult', 'quickSearchMemCache', 'csv', 'firestoreUtil', '_require', 'xlsx', 'projectId', 'bigquery', 'gmailEmail', 'gConst', 'firestoreDb', 'replyUserFn_', '_require2', 'Storage', 'gmailPassword', 'queryProcessing', 'replyUser_', 'QuickSearchQuery', 'quickSearchReply', 'memCacheUserLastResult', 'nodemailer', 'arrayToJson', 'storage', 'mailTransport', 'sendMailResponse', 'quickSearchResponse', 'getLastResult', 'changeColumnVisibility', 'saveLastResult_', 'functions', 'parse', 'BigQuery', 'gcs', 'changeRateLastResult_', 'NodeCache', 'util'])
@Js
def PyJsHoisted_replyUserFn__(uid, queryMode, ts, botName, textMessage, searchResultTable, qsr, statsArray, this, arguments, var=var):
    var = Scope({'uid':uid, 'queryMode':queryMode, 'ts':ts, 'botName':botName, 'textMessage':textMessage, 'searchResultTable':searchResultTable, 'qsr':qsr, 'statsArray':statsArray, 'this':this, 'arguments':arguments}, var)
    var.registers(['botName', 'qsr', 'statsArray', 'queryMode', 'uid', 'textMessage', 'searchResultTable', 'ts'])
    return var.get('replyUser_')(var.get('uid'), (var.get('queryMode')+Js('/fn')), var.get('ts'), var.get('botName'), var.get('textMessage'), var.get('searchResultTable'), var.get('qsr'), var.get('statsArray'))
PyJsHoisted_replyUserFn__.func_name = 'replyUserFn_'
var.put('replyUserFn_', PyJsHoisted_replyUserFn__)
@Js
def PyJsHoisted_replyUser__(uid, queryMode, ts, botName, textMessage, searchResultTable, qsr, statsArray, this, arguments, var=var):
    var = Scope({'uid':uid, 'queryMode':queryMode, 'ts':ts, 'botName':botName, 'textMessage':textMessage, 'searchResultTable':searchResultTable, 'qsr':qsr, 'statsArray':statsArray, 'this':this, 'arguments':arguments}, var)
    var.registers(['botName', 'quickSearch', 'qsr', 'statsArray', 'queryMode', 'stats', 'uid', 'textMessage', 'searchResultTable', 'ts'])
    var.put('quickSearch', Js(''))
    var.put('stats', Js(''))
    if var.get('qsr'):
        var.put('quickSearch', var.get('qsr'))
        var.put('stats', var.get('statsArray'))
    var.get('admin').callprop('database').callprop('ref', (Js('messages/')+var.get('uid'))).callprop('push', Js({'name':var.get('botName'),'queryMode':var.get('queryMode'),'timeStamp':var.get('ts'),'photoUrl':Js('/images/logo.png'),'text':var.get('textMessage'),'botReply':Js('true'),'searchResult':var.get('searchResultTable'),'quickSearch':var.get('quickSearch'),'stats':var.get('stats')}))
    return var.get('undefined')
PyJsHoisted_replyUser__.func_name = 'replyUser_'
var.put('replyUser_', PyJsHoisted_replyUser__)
@Js
def PyJsHoisted_saveLastResult__(uid, queryMode, ts, searchResult, entityName, entityValue, columnName, hiddenColumnName, this, arguments, var=var):
    var = Scope({'uid':uid, 'queryMode':queryMode, 'ts':ts, 'searchResult':searchResult, 'entityName':entityName, 'entityValue':entityValue, 'columnName':columnName, 'hiddenColumnName':hiddenColumnName, 'this':this, 'arguments':arguments}, var)
    var.registers(['entityValue', 'entityName', 'queryMode', 'searchResult', 'uid', 'hiddenColumnName', 'ts', 'columnName', 'dataObj'])
    var.put('dataObj', Js({'queryMode':var.get('queryMode'),'timeStamp':var.get('ts'),'searchResult':var.get('searchResult'),'entityName':var.get('entityName'),'entityValue':var.get('entityValue'),'columnName':var.get('columnName'),'hiddenColumnName':var.get('hiddenColumnName')}))
    var.get('memCacheUserLastResult').callprop('set', var.get('uid'), var.get('dataObj'))
    return var.get('admin').callprop('database').callprop('ref', (Js('LastResult/')+var.get('uid'))).callprop('push', var.get('dataObj'))
PyJsHoisted_saveLastResult__.func_name = 'saveLastResult_'
var.put('saveLastResult_', PyJsHoisted_saveLastResult__)
@Js
def PyJsHoisted_getLastResult_(uid, callBackFn, this, arguments, var=var):
    var = Scope({'uid':uid, 'callBackFn':callBackFn, 'this':this, 'arguments':arguments}, var)
    var.registers(['value', 'messagesRef', 'callBackFn', 'uid'])
    var.put('value', var.get('memCacheUserLastResult').callprop('get', var.get('uid')))
    if (var.get('value')!=var.get('undefined')):
        var.get('callBackFn')(var.get('value'))
        return var.get('undefined')
    var.get('console').callprop('log', ((Js('key ')+var.get('uid'))+Js(' not found')))
    var.put('messagesRef', var.get('admin').callprop('database').callprop('ref', (Js('LastResult/')+var.get('uid'))))
    @Js
    def PyJs_anonymous_0_(snapshot, this, arguments, var=var):
        var = Scope({'snapshot':snapshot, 'this':this, 'arguments':arguments}, var)
        var.registers(['snapshot'])
        @Js
        def PyJs_anonymous_1_(data, this, arguments, var=var):
            var = Scope({'data':data, 'this':this, 'arguments':arguments}, var)
            var.registers(['data'])
            var.get('callBackFn')(var.get('data').callprop('val'))
            var.get('memCacheUserLastResult').callprop('set', var.get('uid'), var.get('data').callprop('val'))
            return Js(True)
        PyJs_anonymous_1_._set_name('anonymous')
        var.get('snapshot').callprop('forEach', PyJs_anonymous_1_)
    PyJs_anonymous_0_._set_name('anonymous')
    var.get('messagesRef').callprop('orderByKey').callprop('limitToLast', Js(1.0)).callprop('once', Js('value'), PyJs_anonymous_0_)
PyJsHoisted_getLastResult_.func_name = 'getLastResult'
var.put('getLastResult', PyJsHoisted_getLastResult_)
@Js
def PyJsHoisted_quickSearchRespond_(uid, queryMode, ts, this, arguments, var=var):
    var = Scope({'uid':uid, 'queryMode':queryMode, 'ts':ts, 'this':this, 'arguments':arguments}, var)
    var.registers(['bqOptions', 'tempRows', 'queryMode', 'uid', 'ts'])
    var.put('tempRows', var.get('quickSearchMemCache').callprop('get', Js('quick-search')))
    if (var.get('tempRows')!=var.get('undefined')):
        var.get('quickSearchReply')(var.get('uid'), var.get('queryMode'), var.get('ts'), var.get('tempRows'))
        return var.get('undefined')
    var.put('bqOptions', Js({'query':var.get('QuickSearchQuery'),'useLegacySql':Js(True)}))
    var.get('console').callprop('log', (Js('Quick Search Query')+var.get('bqOptions').get('query')))
    @Js
    def PyJs_anonymous_6_(err, this, arguments, var=var):
        var = Scope({'err':err, 'this':this, 'arguments':arguments}, var)
        var.registers(['err'])
        var.get('console').callprop('error', Js('Quick Search BQ ERROR:'), var.get('err'))
    PyJs_anonymous_6_._set_name('anonymous')
    @Js
    def PyJs_anonymous_7_(results, this, arguments, var=var):
        var = Scope({'results':results, 'this':this, 'arguments':arguments}, var)
        var.registers(['rows', 'results'])
        var.put('rows', var.get('results').get('0'))
        var.get('quickSearchReply')(var.get('uid'), var.get('queryMode'), var.get('ts'), var.get('rows'))
        var.get('memCache').callprop('set', Js('quick-search'), var.get('rows'))
    PyJs_anonymous_7_._set_name('anonymous')
    var.get('bigquery').callprop('query', var.get('bqOptions')).callprop('then', PyJs_anonymous_7_).callprop('catch', PyJs_anonymous_6_)
    var.get('replyUserFn_')(var.get('uid'), var.get('queryMode'), var.get('ts'), Js('quick-search'), Js('We are working on your quick search request'), Js(''))
PyJsHoisted_quickSearchRespond_.func_name = 'quickSearchRespond'
var.put('quickSearchRespond', PyJsHoisted_quickSearchRespond_)
@Js
def PyJsHoisted_quickSearchReply_(uid, queryMode, ts, rows, cachedResult, this, arguments, var=var):
    var = Scope({'uid':uid, 'queryMode':queryMode, 'ts':ts, 'rows':rows, 'cachedResult':cachedResult, 'this':this, 'arguments':arguments}, var)
    var.registers(['qsr', 'queryMode', 'uid', 'ts', 'rows', 'cachedResult'])
    pass
    if (var.get('cachedResult')==var.get(u"null")):
        var.put('qsr', var.get('quickSearchResponse').callprop('createQuickSearchResponse', var.get('rows')))
        var.get('console').callprop('log', Js('FireStore: Setting value in FireStore'))
        try:
            var.get('firestoreDb').callprop('collection', Js('cache')).callprop('doc', Js('quick_search')).callprop('set', var.get('JSON').callprop('stringify', var.get('qsr')))
        except PyJsException as PyJsTempException:
            PyJsHolder_6572726f72_49129649 = var.own.get('error')
            var.force_own_put('error', PyExceptionToJs(PyJsTempException))
            try:
                var.get('console').callprop('error', Js('Firestore: Error setting document'), var.get('error'))
            finally:
                if PyJsHolder_6572726f72_49129649 is not None:
                    var.own['error'] = PyJsHolder_6572726f72_49129649
                else:
                    del var.own['error']
                del PyJsHolder_6572726f72_49129649
    else:
        var.put('qsr', var.get('cachedResult'))
    var.get('replyUser_')(var.get('uid'), var.get('queryMode'), var.get('ts'), Js('Message from system'), Js('Click on any cell to search'), Js(''), var.get('qsr').get('quickSearchArray'), var.get('qsr').get('stats'))
PyJsHoisted_quickSearchReply_.func_name = 'quickSearchReply'
var.put('quickSearchReply', PyJsHoisted_quickSearchReply_)
@Js
def PyJsHoisted_queryAndSendBQResult_(uid, queryMode, ts, parsesUserRequest, this, arguments, var=var):
    var = Scope({'uid':uid, 'queryMode':queryMode, 'ts':ts, 'parsesUserRequest':parsesUserRequest, 'this':this, 'arguments':arguments}, var)
    var.registers(['parsedQuery', 'bqOptions', 'queryMode', 'uid', 'parsesUserRequest', 'textReply', 'ts'])
    var.put('bqOptions', Js({'query':var.get('parsesUserRequest').get('query'),'useLegacySql':Js(True)}))
    var.put('parsedQuery', var.get('parsesUserRequest').get('parsedQuery'))
    var.put('textReply', (Js('We are getting result for your search request: ')+var.get('parsesUserRequest').get('condition')))
    @Js
    def PyJs_anonymous_8_(err, this, arguments, var=var):
        var = Scope({'err':err, 'this':this, 'arguments':arguments}, var)
        var.registers(['err'])
        var.get('console').callprop('error', Js('User Search BQ ERROR:'), var.get('err'))
    PyJs_anonymous_8_._set_name('anonymous')
    @Js
    def PyJs_anonymous_9_(results, this, arguments, var=var):
        var = Scope({'results':results, 'this':this, 'arguments':arguments}, var)
        var.registers(['rows', 'resultArray', 'results'])
        var.put('rows', var.get('results').get('0'))
        var.put('resultArray', var.get('util').callprop('ParseBQResultAndCreateArray', var.get('rows'), var.get('parsedQuery').get('columnName')))
        var.get('replyUser_')(var.get('uid'), var.get('queryMode'), var.get('ts'), Js('Search Result'), Js('Result is:'), var.get('resultArray'))
        var.get('saveLastResult_')(var.get('uid'), var.get('queryMode'), var.get('ts'), var.get('rows'), var.get('parsedQuery').get('entityName'), var.get('parsedQuery').get('entityValue'), var.get('parsedQuery').get('columnName'), var.get('parsedQuery').get('hiddenColumnName'))
    PyJs_anonymous_9_._set_name('anonymous')
    var.get('bigquery').callprop('query', var.get('bqOptions')).callprop('then', PyJs_anonymous_9_).callprop('catch', PyJs_anonymous_8_)
    var.get('replyUser_')(var.get('uid'), var.get('queryMode'), var.get('ts'), Js('Search Result'), var.get('textReply'), Js(''))
PyJsHoisted_queryAndSendBQResult_.func_name = 'queryAndSendBQResult'
var.put('queryAndSendBQResult', PyJsHoisted_queryAndSendBQResult_)
@Js
def PyJsHoisted_changeColumnVisibility_(uid, queryMode, ts, columnNameArray, showBool, this, arguments, var=var):
    var = Scope({'uid':uid, 'queryMode':queryMode, 'ts':ts, 'columnNameArray':columnNameArray, 'showBool':showBool, 'this':this, 'arguments':arguments}, var)
    var.registers(['columnNameArray', 'queryMode', 'uid', 'showBool', 'ts'])
    @Js
    def PyJs_anonymous_10_(lastResult, this, arguments, var=var):
        var = Scope({'lastResult':lastResult, 'this':this, 'arguments':arguments}, var)
        var.registers(['newHiddenColumnName', 'newShownColumnName', 'shownColumnName', 'i', 'lastResult', 'resultArray'])
        var.put('shownColumnName', var.get('lastResult').get('columnName'))
        var.put('newShownColumnName', Js([]))
        var.put('newHiddenColumnName', Js([]))
        if var.get('showBool'):
            var.put('newShownColumnName', var.get('shownColumnName'))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('lastResult').get('hiddenColumnName').get('length')):
                try:
                    if (var.get('columnNameArray').callprop('indexOf', var.get('lastResult').get('hiddenColumnName').get(var.get('i')))!=(-Js(1.0))):
                        var.get('newShownColumnName').callprop('push', var.get('lastResult').get('hiddenColumnName').get(var.get('i')))
                    else:
                        var.get('newHiddenColumnName').callprop('push', var.get('lastResult').get('hiddenColumnName').get(var.get('i')))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        else:
            var.put('newHiddenColumnName', var.get('lastResult').get('hiddenColumnName'))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('lastResult').get('columnName').get('length')):
                try:
                    if (var.get('columnNameArray').callprop('indexOf', var.get('lastResult').get('columnName').get(var.get('i')))!=(-Js(1.0))):
                        var.get('newHiddenColumnName').callprop('push', var.get('lastResult').get('columnName').get(var.get('i')))
                    else:
                        var.get('newShownColumnName').callprop('push', var.get('lastResult').get('columnName').get(var.get('i')))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        var.put('resultArray', var.get('util').callprop('ParseBQResultAndCreateArray', var.get('lastResult').get('searchResult'), var.get('newShownColumnName')))
        var.get('replyUser_')(var.get('uid'), var.get('queryMode'), var.get('ts'), Js('Search Result'), Js('Modified table is as follow:'), var.get('resultArray'))
        var.get('saveLastResult_')(var.get('uid'), var.get('queryMode'), var.get('ts'), var.get('lastResult').get('searchResult'), var.get('lastResult').get('entityName'), var.get('lastResult').get('entityValue'), var.get('newShownColumnName'), var.get('newHiddenColumnName'))
    PyJs_anonymous_10_._set_name('anonymous')
    var.get('getLastResult')(var.get('uid'), PyJs_anonymous_10_)
PyJsHoisted_changeColumnVisibility_.func_name = 'changeColumnVisibility'
var.put('changeColumnVisibility', PyJsHoisted_changeColumnVisibility_)
@Js
def PyJsHoisted_changeRateLastResult__(uid, queryMode, ts, percent, constDollar, this, arguments, var=var):
    var = Scope({'uid':uid, 'queryMode':queryMode, 'ts':ts, 'percent':percent, 'constDollar':constDollar, 'this':this, 'arguments':arguments}, var)
    var.registers(['constDollar', 'queryMode', 'uid', 'ts', 'percent'])
    @Js
    def PyJs_anonymous_11_(lastResult, this, arguments, var=var):
        var = Scope({'lastResult':lastResult, 'this':this, 'arguments':arguments}, var)
        var.registers(['changedRateData', 'resultArray', 'lastResult'])
        var.put('changedRateData', var.get('util').callprop('ChangeRateUS', var.get('lastResult').get('searchResult'), var.get('percent'), var.get('constDollar')))
        var.put('resultArray', var.get('util').callprop('ParseBQResultAndCreateArray', var.get('changedRateData'), var.get('lastResult').get('columnName')))
        var.get('replyUser_')(var.get('uid'), var.get('queryMode'), var.get('ts'), Js('Search Result'), Js('Modified table is as follow:'), var.get('resultArray'))
        var.get('saveLastResult_')(var.get('uid'), var.get('queryMode'), var.get('ts'), var.get('changedRateData'), var.get('lastResult').get('entityName'), var.get('lastResult').get('entityValue'), var.get('lastResult').get('columnName'), var.get('lastResult').get('hiddenColumnName'))
    PyJs_anonymous_11_._set_name('anonymous')
    var.get('getLastResult')(var.get('uid'), PyJs_anonymous_11_)
PyJsHoisted_changeRateLastResult__.func_name = 'changeRateLastResult_'
var.put('changeRateLastResult_', PyJsHoisted_changeRateLastResult__)
@Js
def PyJsHoisted_sendSearchResultEmail_(subject, resultTableData, toEmail, this, arguments, var=var):
    var = Scope({'subject':subject, 'resultTableData':resultTableData, 'toEmail':toEmail, 'this':this, 'arguments':arguments}, var)
    var.registers(['subject', 'resultTableData', 'toEmail', 'mailOptions'])
    var.put('mailOptions', Js({'from':Js('Diamond Search <sales@anikadiamond.com>'),'to':var.get('toEmail')}))
    var.get('mailOptions').put('subject', var.get('subject'))
    var.get('mailOptions').put('html', ((Js('Hi,<br><br>Your report is as follow: <br><br>')+var.get('util').callprop('CreateHtmlTableFromResultArray', var.get('resultTableData')))+Js('<br><br>Thanks for using Diamond Search.')))
    @Js
    def PyJs_anonymous_14_(err, this, arguments, var=var):
        var = Scope({'err':err, 'this':this, 'arguments':arguments}, var)
        var.registers(['err'])
        var.get('console').callprop('error', Js('Sending Email ERROR: '), var.get('err'))
    PyJs_anonymous_14_._set_name('anonymous')
    @Js
    def PyJs_anonymous_15_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.get('console').callprop('log', (Js('Search Result email sent to:')+var.get('toEmail')))
    PyJs_anonymous_15_._set_name('anonymous')
    return var.get('mailTransport').callprop('sendMail', var.get('mailOptions')).callprop('then', PyJs_anonymous_15_).callprop('catch', PyJs_anonymous_14_)
PyJsHoisted_sendSearchResultEmail_.func_name = 'sendSearchResultEmail'
var.put('sendSearchResultEmail', PyJsHoisted_sendSearchResultEmail_)
@Js
def PyJsHoisted_sendMailResponse_(uid, queryMode, ts, toEmail, this, arguments, var=var):
    var = Scope({'uid':uid, 'queryMode':queryMode, 'ts':ts, 'toEmail':toEmail, 'this':this, 'arguments':arguments}, var)
    var.registers(['userReply', 'queryMode', 'uid', 'ts', 'toEmail'])
    var.put('userReply', Js(''))
    @Js
    def PyJs_anonymous_16_(lastResult, this, arguments, var=var):
        var = Scope({'lastResult':lastResult, 'this':this, 'arguments':arguments}, var)
        var.registers(['lastResult'])
        if var.get('lastResult').get('searchResult'):
            var.get('sendSearchResultEmail')(Js('Result from diamond search:'), var.get('util').callprop('ParseBQResultAndCreateArray', var.get('lastResult').get('searchResult'), var.get('lastResult').get('columnName')), var.get('toEmail'))
            var.put('userReply', Js('Email was sent with following search Result'))
        else:
            var.put('userReply', Js('No Results to send'))
        return var.get('replyUser_')(var.get('uid'), var.get('queryMode'), var.get('ts'), Js('Email assistant'), var.get('userReply'), var.get('lastResult').get('searchResult'))
    PyJs_anonymous_16_._set_name('anonymous')
    var.get('getLastResult')(var.get('uid'), PyJs_anonymous_16_)
PyJsHoisted_sendMailResponse_.func_name = 'sendMailResponse'
var.put('sendMailResponse', PyJsHoisted_sendMailResponse_)
Js('use strict')
var.put('gcs', var.get('require')(Js('@google-cloud/storage')))
var.put('NodeCache', var.get('require')(Js('node-cache')))
var.put('csv', var.get('require')(Js('csvtojson')))
var.put('fs', var.get('require')(Js('fs')))
var.put('cloudconvert', var.get('require')(Js('cloudconvert')).create(Js('o99mxJrAzJpaUDhPL7JnViPik646Vdzu0xUoJM-XRVaJ5Y0iZOm3jvle2EXQPSBdOONWJpWbN_NSxdTOR0pMeA')))
var.put('parse', var.get('require')(Js('csv-parse')))
var.put('xlsx', var.get('require')(Js('node-xlsx')))
var.put('cors', var.get('require')(Js('cors'))(Js({'origin':Js(True)})))
var.put('queryProcessing', var.get('require')(Js('./queryProcessing.js')))
var.put('quickSearchResponse', var.get('require')(Js('./quickSearchResponse.js')))
var.put('firestoreUtil', var.get('require')(Js('./firestoreUtil.js')))
var.put('arrayToJson', var.get('require')(Js('./arrayToJson.js')))
var.put('util', var.get('require')(Js('./util.js')))
var.put('gConst', var.get('require')(Js('./gConst')))
var.put('functions', var.get('require')(Js('firebase-functions')))
var.put('admin', var.get('require')(Js('firebase-admin')))
var.get('admin').callprop('initializeApp')
var.put('_require', var.get('require')(Js('@google-cloud/bigquery')))
var.put('BigQuery', var.get('_require').get('BigQuery'))
var.put('projectId', Js('cloudstoragehelloworld'))
var.put('bigquery', var.get('BigQuery').create(Js({'projectId':var.get('projectId')})))
var.put('_require2', var.get('require')(Js('@google-cloud/storage')))
var.put('Storage', var.get('_require2').get('Storage'))
var.put('storage', var.get('Storage').create(Js({'projectId':var.get('projectId')})))
var.put('firestoreDb', var.get('admin').callprop('firestore'))
var.put('nodemailer', var.get('require')(Js('nodemailer')))
var.put('gmailEmail', Js('temp@email.com'))
var.put('gmailPassword', Js('psswrd'))
var.put('mailTransport', var.get('nodemailer').callprop('createTransport', Js('smtps://').callprop('concat', var.get('gmailEmail'), Js(':')).callprop('concat', var.get('gmailPassword'), Js('@smtp.gmail.com'))))
pass
pass
var.put('memCacheUserLastResult', var.get('NodeCache').create(Js({'stdTTL':Js(3600.0)})))
pass
pass
@Js
def PyJs_anonymous_2_(snapshot, this, arguments, var=var):
    var = Scope({'snapshot':snapshot, 'this':this, 'arguments':arguments}, var)
    var.registers(['queryMode', 'uid', 'userMessage', 'parsesUserRequest', 'snapshot', 'ts'])
    if PyJsStrictEq(var.get('snapshot').callprop('val').get('botReply'),Js('true')):
        return var.get('undefined')
    var.put('userMessage', var.get('snapshot').callprop('val').get('text'))
    var.put('uid', var.get('snapshot').callprop('val').get('uid'))
    var.put('ts', var.get('snapshot').callprop('val').get('timeStamp'))
    var.get('console').callprop('log', (((((Js('New User Message:')+var.get('userMessage'))+Js(' With timeStamp:'))+var.get('ts'))+Js(' and UID is: '))+var.get('uid')))
    var.put('parsesUserRequest', var.get('queryProcessing').callprop('parseUserRequest', var.get('userMessage')))
    var.put('queryMode', var.get('parsesUserRequest').get('queryMode'))
    while 1:
        SWITCHED = False
        CONDITION = (var.get('queryMode'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js('help')):
            SWITCHED = True
            return var.get('replyUserFn_')(var.get('uid'), var.get('queryMode'), var.get('ts'), Js('Message from system'), var.get('parsesUserRequest').get('userMessage'), Js(''))
        if SWITCHED or PyJsStrictEq(CONDITION, Js('quick-search')):
            SWITCHED = True
            return var.get('quickSearchRespond')(var.get('uid'), var.get('queryMode'), var.get('ts'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js('email')):
            SWITCHED = True
            var.get('sendMailResponse')(var.get('uid'), var.get('queryMode'), var.get('ts'), var.get('parsesUserRequest').get('email'))
            return var.get('undefined')
        if SWITCHED or PyJsStrictEq(CONDITION, Js('btQuery')):
            SWITCHED = True
            return var.get('queryAndSendBQResult')(var.get('uid'), var.get('queryMode'), var.get('ts'), var.get('parsesUserRequest'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js('hide')):
            SWITCHED = True
            return var.get('changeColumnVisibility')(var.get('uid'), var.get('queryMode'), var.get('ts'), var.get('parsesUserRequest').get('columnNameArray'), Js(False))
        if SWITCHED or PyJsStrictEq(CONDITION, Js('show')):
            SWITCHED = True
            return var.get('changeColumnVisibility')(var.get('uid'), var.get('queryMode'), var.get('ts'), var.get('parsesUserRequest').get('columnNameArray'), Js(True))
        if SWITCHED or PyJsStrictEq(CONDITION, Js('image')):
            SWITCHED = True
            return var.get('replyUserFn_')(var.get('uid'), var.get('queryMode'), var.get('ts'), Js('Message from system'), Js('We are working on adding feature to show image of stone.'), Js(''))
        if SWITCHED or PyJsStrictEq(CONDITION, Js('video')):
            SWITCHED = True
            return var.get('replyUserFn_')(var.get('uid'), var.get('queryMode'), var.get('ts'), Js('Message from system'), Js('We are working on adding feature to show video of stone.'), Js(''))
        if SWITCHED or PyJsStrictEq(CONDITION, Js('changeRate')):
            SWITCHED = True
            return var.get('changeRateLastResult_')(var.get('uid'), var.get('queryMode'), var.get('ts'), var.get('parsesUserRequest').get('percent'), var.get('parsesUserRequest').get('constUsd'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js('cache')):
            SWITCHED = True
            var.get('firestoreUtil').callprop('FirestoreRead', var.get('uid'), var.get('queryMode'), var.get('ts'), var.get('firestoreDb'), var.get('replyUserFn_'))
            return var.get('replyUserFn_')(var.get('uid'), var.get('queryMode'), var.get('ts'), Js('Message from system'), Js('Cache return'), Js(''))
        if True:
            SWITCHED = True
            return var.get('replyUserFn_')(var.get('uid'), var.get('queryMode'), var.get('ts'), Js('Message from system'), Js('Your request is invalid, message/search "help" for usage instructions.'), Js(''))
        SWITCHED = True
        break
PyJs_anonymous_2_._set_name('anonymous')
var.get('exports').put('replyQueryMessages', var.get('functions').get('database').callprop('ref', Js('/messages/{uid}/{messageId}')).callprop('onCreate', PyJs_anonymous_2_))
@Js
def PyJs_anonymous_3_(req, res, this, arguments, var=var):
    var = Scope({'req':req, 'res':res, 'this':this, 'arguments':arguments}, var)
    var.registers(['res', 'req'])
    if PyJsStrictEq(var.get('req').get('method'),Js('PUT')):
        return var.get('res').callprop('status', Js(403.0)).callprop('send', Js('Forbidden!'))
    @Js
    def PyJs_anonymous_4_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['companyCode'])
        if var.get('req').get('query'):
            var.get('console').callprop('log', (Js(' Req query:')+var.get('JSON').callprop('stringify', var.get('req').get('query'))))
        var.get('console').callprop('log', (Js(' Req Json:')+var.get('JSON').callprop('stringify', var.get('req').get('method'))))
        var.put('companyCode', var.get('req').get('query').get('code'))
        var.get('console').callprop('log', (Js('loadData param: Company Code:')+var.get('companyCode')))
        var.get('console').callprop('log', (Js('Sending Company code back:')+var.get('companyCode')))
        var.get('firestoreUtil').callprop('AddToFirestore', var.get('firestoreDb'), var.get('req').get('body'), var.get('companyCode'))
        var.get('res').callprop('status', Js(200.0)).callprop('send', (Js('Response 200 from kp-Firebase')+var.get('companyCode')))
    PyJs_anonymous_4_._set_name('anonymous')
    return var.get('cors')(var.get('req'), var.get('res'), PyJs_anonymous_4_)
PyJs_anonymous_3_._set_name('anonymous')
var.get('exports').put('loadData', var.get('functions').get('https').callprop('onRequest', PyJs_anonymous_3_))
def PyJs_LONG_5_(var=var):
    return ((((((((((((((Js(' SELECT ')+Js('  Color, '))+Js('  Clarity, '))+Js('  ROUND(Size,2) Carat, '))+Js('  FLOOR(Min(Rate_US)) Min_Price, '))+Js('  CEIL(Max(Rate_US)) Max_Price, '))+Js('  ROUND(Avg(Rate_US)) Avg_Price, '))+Js('  count(*) Count '))+Js(' FROM cloudstoragehelloworld.Diamond_Inv.latest '))+Js(' GROUP BY '))+Js('  Color, '))+Js('  Clarity, '))+Js('  Carat '))+Js(' ORDER BY '))+Js('  Color, '))
var.put('QuickSearchQuery', ((PyJs_LONG_5_()+Js('  Clarity, '))+Js('  Carat ')))
var.put('quickSearchMemCache', var.get('NodeCache').create(Js({'stdTTL':Js(3600.0)})))
pass
pass
pass
pass
pass
@Js
def PyJs_anonymous_12_(event, this, arguments, var=var):
    var = Scope({'event':event, 'this':this, 'arguments':arguments}, var)
    var.registers(['event', 'fullName', 'user'])
    var.put('user', var.get('event').get('data'))
    var.put('fullName', var.get('user').get('displayName'))
    var.get('console').callprop('log', ((Js('A new user, ')+var.get('fullName'))+Js(', signed in for the first time.')))
    var.get('sendSearchResultEmail')((var.get('fullName')+Js(' signed in for the first time.')), Js(''), Js('kalpesh@anikadiamond.com'))
    @Js
    def PyJs_anonymous_13_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.get('admin').callprop('database').callprop('ref', (Js('users/')+var.get('user').get('uid'))).callprop('set', Js({'agreement':Js(0.0)}))
    PyJs_anonymous_13_._set_name('anonymous')
    var.get('admin').callprop('database').callprop('ref', (Js('messages/')+var.get('user').get('uid'))).callprop('push', Js({'name':Js('Welcome Messenger'),'photoUrl':Js('/images/logo.png'),'botReply':Js('true'),'text':((var.get('fullName')+Js(' signed in for the first time! Welcome! \n'))+Js('Type "help" to get started.'))})).callprop('then', PyJs_anonymous_13_)
PyJs_anonymous_12_._set_name('anonymous')
var.get('exports').put('addWelcomeMessages', var.get('functions').get('auth').callprop('user').callprop('onCreate', PyJs_anonymous_12_))
pass
pass
@Js
def PyJs_anonymous_17_(event, this, arguments, var=var):
    var = Scope({'event':event, 'this':this, 'arguments':arguments}, var)
    var.registers(['downloadUrl', 'bucket', 'uid', 'snapshot', 'statusOfFile', 'uploadedFile', 'event', 'inventoryId', 'fileName'])
    var.put('snapshot', var.get('event').get('data'))
    if var.get('snapshot').get('previous').callprop('exists'):
        return var.get('undefined')
    var.put('inventoryId', var.get('snapshot').get('ref').get('parent').get('ref').get('key'))
    var.put('fileName', var.get('snapshot').callprop('val').get('filename'))
    var.put('statusOfFile', var.get('snapshot').callprop('val').get('status'))
    var.put('uid', var.get('snapshot').callprop('val').get('uid'))
    var.put('bucket', var.get('gcs').callprop('bucket', Js('dinsightmessenger.appspot.com')))
    var.put('uploadedFile', var.get('bucket').callprop('file', ((var.get('uid')+Js('/Personal/'))+var.get('fileName'))))
    var.put('downloadUrl', (Js('/tmp/')+var.get('fileName')))
    if (var.get('fileName').callprop('split', Js('.')).get('1')==Js('csv')):
        @Js
        def PyJs_anonymous_18_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            @Js
            def PyJs_read_19_(err, data, this, arguments, var=var):
                var = Scope({'err':err, 'data':data, 'this':this, 'arguments':arguments, 'read':PyJs_read_19_}, var)
                var.registers(['err', 'data'])
                if var.get('err'):
                    PyJsTempException = JsToPyException(var.get('err'))
                    raise PyJsTempException
                try:
                    @Js
                    def PyJs_anonymous_20_(err, output, this, arguments, var=var):
                        var = Scope({'err':err, 'output':output, 'this':this, 'arguments':arguments}, var)
                        var.registers(['err', 'output'])
                        @Js
                        def PyJs_anonymous_21_(this, arguments, var=var):
                            var = Scope({'this':this, 'arguments':arguments}, var)
                            var.registers([])
                            var.get('admin').callprop('database').callprop('ref', ((Js('Inventory/')+var.get('inventoryId'))+Js('/Data/'))).callprop('set', Js({'data':var.get('output')}))
                        PyJs_anonymous_21_._set_name('anonymous')
                        @Js
                        def PyJs_anonymous_22_(this, arguments, var=var):
                            var = Scope({'this':this, 'arguments':arguments}, var)
                            var.registers([])
                            var.get('admin').callprop('database').callprop('ref', (Js('messages/')+var.get('uid'))).callprop('push', Js({'name':Js('System'),'text':(var.get('fileName')+Js(' file parsed successfully')),'botReply':Js('true'),'photoUrl':Js('/images/profile_placeholder.png')}))
                        PyJs_anonymous_22_._set_name('anonymous')
                        @Js
                        def PyJs_anonymous_23_(this, arguments, var=var):
                            var = Scope({'this':this, 'arguments':arguments}, var)
                            var.registers(['j', 'i'])
                            var.put('i', Js(0.0))
                            #for JS loop
                            var.put('j', Js(0.0))
                            while ((var.get('i')<Js(4.0)) and (var.get('j')<var.get('output').get('length'))):
                                try:
                                    if (var.get('output').get(var.get('j')).get('length')==var.get('output').get('0').get('length')):
                                        var.get('admin').callprop('database').callprop('ref', ((((Js('Inventory/')+var.get('inventoryId'))+Js('/Sample/'))+var.get('i'))+Js('/'))).callprop('set', Js({'row':var.get('output').get(var.get('j')).callprop('join', Js('|'))}))
                                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                                finally:
                                        (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                        PyJs_anonymous_23_._set_name('anonymous')
                        var.get('admin').callprop('database').callprop('ref', ((Js('Inventory/')+var.get('inventoryId'))+Js('/ExtractedHeaders/'))).callprop('set', Js({'headers':var.get('output').get('0')})).callprop('then', PyJs_anonymous_23_).callprop('then', PyJs_anonymous_22_).callprop('then', PyJs_anonymous_21_)
                    PyJs_anonymous_20_._set_name('anonymous')
                    var.get('parse')(var.get('data'), Js({'comment':Js('#')}), PyJs_anonymous_20_)
                except PyJsException as PyJsTempException:
                    PyJsHolder_6572726f72_92736137 = var.own.get('error')
                    var.force_own_put('error', PyExceptionToJs(PyJsTempException))
                    try:
                        var.get('admin').callprop('database').callprop('ref', (Js('messages/')+var.get('uid'))).callprop('push', Js({'name':Js('System'),'text':(var.get('fileName')+Js(" file couldn't be parsed successfully")),'botReply':Js('true'),'photoUrl':Js('/images/profile_placeholder.png')}))
                    finally:
                        if PyJsHolder_6572726f72_92736137 is not None:
                            var.own['error'] = PyJsHolder_6572726f72_92736137
                        else:
                            del var.own['error']
                        del PyJsHolder_6572726f72_92736137
            PyJs_read_19_._set_name('read')
            var.get('fs').callprop('readFile', var.get('downloadUrl'), PyJs_read_19_)
        PyJs_anonymous_18_._set_name('anonymous')
        var.get('uploadedFile').callprop('download', Js({'destination':var.get('downloadUrl')})).callprop('then', PyJs_anonymous_18_)
    else:
        @Js
        def PyJs_anonymous_24_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['sheet', 'j', 'i', 'rows', 'obj', 'writeStr'])
            try:
                var.put('obj', var.get('xlsx').callprop('parse', var.get('downloadUrl')))
                var.put('rows', Js([]))
                var.put('writeStr', Js(''))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('obj').get('length')):
                    try:
                        var.put('sheet', var.get('obj').get(var.get('i')))
                        #for JS loop
                        var.put('j', Js(0.0))
                        while (var.get('j')<var.get('sheet').get('data').get('length')):
                            try:
                                var.get('rows').callprop('push', var.get('sheet').get('data').get(var.get('j')))
                            finally:
                                    (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                @Js
                def PyJs_anonymous_25_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    var.get('admin').callprop('database').callprop('ref', ((Js('Inventory/')+var.get('inventoryId'))+Js('/Data/'))).callprop('set', Js({'data':var.get('rows')}))
                PyJs_anonymous_25_._set_name('anonymous')
                @Js
                def PyJs_anonymous_26_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    var.get('admin').callprop('database').callprop('ref', (Js('messages/')+var.get('uid'))).callprop('push', Js({'name':Js('System'),'text':(var.get('fileName')+Js(' file parsed successfully')),'botReply':Js('true'),'photoUrl':Js('/images/profile_placeholder.png')}))
                PyJs_anonymous_26_._set_name('anonymous')
                @Js
                def PyJs_anonymous_27_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers(['j', 'i'])
                    var.put('i', Js(0.0))
                    #for JS loop
                    var.put('j', Js(0.0))
                    while ((var.get('i')<Js(4.0)) and (var.get('j')<var.get('rows').get('length'))):
                        try:
                            if (var.get('rows').get(var.get('j')).get('length')==var.get('rows').get('0').get('length')):
                                var.get('admin').callprop('database').callprop('ref', ((((Js('Inventory/')+var.get('inventoryId'))+Js('/Sample/'))+var.get('i'))+Js('/'))).callprop('set', Js({'row':var.get('rows').get(var.get('j')).callprop('join', Js('|'))}))
                                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                        finally:
                                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                PyJs_anonymous_27_._set_name('anonymous')
                var.get('admin').callprop('database').callprop('ref', ((Js('Inventory/')+var.get('inventoryId'))+Js('/ExtractedHeaders/'))).callprop('set', Js({'headers':var.get('rows').get('0')})).callprop('then', PyJs_anonymous_27_).callprop('then', PyJs_anonymous_26_).callprop('then', PyJs_anonymous_25_)
            except PyJsException as PyJsTempException:
                PyJsHolder_6572726f72_32512252 = var.own.get('error')
                var.force_own_put('error', PyExceptionToJs(PyJsTempException))
                try:
                    var.get('admin').callprop('database').callprop('ref', (Js('messages/')+var.get('uid'))).callprop('push', Js({'name':Js('System'),'text':(var.get('fileName')+Js(" file couldn't be parsed successfully")),'botReply':Js('true'),'photoUrl':Js('/images/profile_placeholder.png')}))
                finally:
                    if PyJsHolder_6572726f72_32512252 is not None:
                        var.own['error'] = PyJsHolder_6572726f72_32512252
                    else:
                        del var.own['error']
                    del PyJsHolder_6572726f72_32512252
        PyJs_anonymous_24_._set_name('anonymous')
        var.get('uploadedFile').callprop('download', Js({'destination':var.get('downloadUrl')})).callprop('then', PyJs_anonymous_24_)
PyJs_anonymous_17_._set_name('anonymous')
var.get('exports').put('eventForFile', var.get('functions').get('database').callprop('ref', Js('/Inventory/{inventoryid}/file/')).callprop('onWrite', PyJs_anonymous_17_))
@Js
def PyJs_anonymous_28_(event, this, arguments, var=var):
    var = Scope({'event':event, 'this':this, 'arguments':arguments}, var)
    var.registers(['downloadUrl', 'bucket', 'uid', 'snapshot', 'uploadedFile', 'event', 'fileName'])
    var.put('snapshot', var.get('event').get('data'))
    var.put('fileName', var.get('snapshot').callprop('val').get('filename'))
    var.put('uid', var.get('snapshot').callprop('val').get('uid'))
    var.put('bucket', var.get('gcs').callprop('bucket', Js('dinsightmessenger.appspot.com')))
    var.put('uploadedFile', var.get('bucket').callprop('file', ((var.get('uid')+Js('/Personal/'))+var.get('fileName'))))
    var.put('downloadUrl', (Js('/tmp/')+var.get('fileName')))
    if (var.get('fileName').callprop('split', Js('.')).get('1')==Js('csv')):
        @Js
        def PyJs_anonymous_29_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            @Js
            def PyJs_read_30_(err, data, this, arguments, var=var):
                var = Scope({'err':err, 'data':data, 'this':this, 'arguments':arguments, 'read':PyJs_read_30_}, var)
                var.registers(['err', 'data'])
                if var.get('err'):
                    PyJsTempException = JsToPyException(var.get('err'))
                    raise PyJsTempException
                @Js
                def PyJs_anonymous_31_(err, output, this, arguments, var=var):
                    var = Scope({'err':err, 'output':output, 'this':this, 'arguments':arguments}, var)
                    var.registers(['err', 'output'])
                    var.put('writeStr', var.get('arrayToJson').callprop('arrayToJsonFn', var.get('output'), Js('trial')))
                    var.get('admin').callprop('database').callprop('ref', Js('Check/')).callprop('push', Js({'text':Js('parsing done')}))
                    @Js
                    def PyJs_anonymous_32_(err, this, arguments, var=var):
                        var = Scope({'err':err, 'this':this, 'arguments':arguments}, var)
                        var.registers(['err'])
                        if var.get('err'):
                            return var.get('console').callprop('log', var.get('err'))
                    PyJs_anonymous_32_._set_name('anonymous')
                    var.get('fs').callprop('writeFile', Js('/tmp/test.txt'), var.get('writeStr'), PyJs_anonymous_32_)
                    var.get('bucket').callprop('upload', Js('/tmp/test.txt'), Js({'destination':((Js('Edited/')+var.get('fileName').callprop('split', Js('.')).get('0'))+Js('.txt'))}))
                PyJs_anonymous_31_._set_name('anonymous')
                var.get('parse')(var.get('data'), Js({'comment':Js('#')}), PyJs_anonymous_31_)
            PyJs_read_30_._set_name('read')
            var.get('fs').callprop('readFile', var.get('downloadUrl'), PyJs_read_30_)
        PyJs_anonymous_29_._set_name('anonymous')
        var.get('uploadedFile').callprop('download', Js({'destination':var.get('downloadUrl')})).callprop('then', PyJs_anonymous_29_)
    else:
        var.get('console').callprop('log', (Js('Starting of download')+var.get('fileName')))
        @Js
        def PyJs_anonymous_33_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            var.get('console').callprop('log', (Js('Completed download')+var.get('fileName')))
            var.get('fs').callprop('createReadStream', var.get('downloadUrl')).callprop('pipe', var.get('cloudconvert').callprop('convert', Js({'inputformat':Js('xls'),'outputformat':Js('csv'),'input':Js('upload')}))).callprop('pipe', var.get('fs').callprop('createWriteStream', Js('/tmp/output.csv')))
        PyJs_anonymous_33_._set_name('anonymous')
        var.get('uploadedFile').callprop('download', Js({'destination':var.get('downloadUrl')})).callprop('then', PyJs_anonymous_33_)
PyJs_anonymous_28_._set_name('anonymous')
var.get('exports').put('eventForFile1', var.get('functions').get('database').callprop('ref', Js('/Inventory1/{uid}/file/')).callprop('onWrite', PyJs_anonymous_28_))
@Js
def PyJs_anonymous_34_(event, this, arguments, var=var):
    var = Scope({'event':event, 'this':this, 'arguments':arguments}, var)
    var.registers(['arrayOfIndex', 'companyCode', 'loopLimit', 'bucket', 'uid', 'snapshot', 'i', 'event', 'inventoryId', 'companyIndex'])
    var.put('snapshot', var.get('event').get('data'))
    var.put('bucket', var.get('gcs').callprop('bucket', Js('dinsightmessenger.appspot.com')))
    var.put('arrayOfIndex', var.get('snapshot').callprop('val'))
    var.put('loopLimit', var.get('arrayOfIndex').get('length'))
    var.put('companyIndex', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('loopLimit')):
        try:
            var.get('companyIndex').callprop('push', var.get('parseInt')(var.get('arrayOfIndex').get(var.get('i'))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    var.put('inventoryId', var.get('snapshot').get('ref').get('parent').get('ref').get('parent').get('key'))
    @Js
    def PyJs_anonymous_35_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        @Js
        def PyJs_anonymous_36_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            @Js
            def PyJs_anonymous_37_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers([])
                try:
                    var.put('writeStr', var.get('arrayToJson').callprop('arrayToJsonFn', var.get('output'), var.get('companyIndex'), var.get('companyCode')))
                    try:
                        @Js
                        def PyJs_anonymous_38_(err, this, arguments, var=var):
                            var = Scope({'err':err, 'this':this, 'arguments':arguments}, var)
                            var.registers(['err'])
                            if var.get('err'):
                                return var.get('console').callprop('log', var.get('err'))
                        PyJs_anonymous_38_._set_name('anonymous')
                        var.get('fs').callprop('writeFile', Js('/tmp/test.txt'), var.get('writeStr'), PyJs_anonymous_38_)
                        @Js
                        def PyJs_anonymous_39_(this, arguments, var=var):
                            var = Scope({'this':this, 'arguments':arguments}, var)
                            var.registers([])
                            var.get('admin').callprop('database').callprop('ref', ((Js('error/')+var.get('uid'))+Js('/'))).callprop('set', Js({'columnMapping':var.get(u"null")}))
                            var.get('admin').callprop('database').callprop('ref', ((Js('Inventory/')+var.get('inventoryId'))+Js('/file/'))).callprop('update', Js({'status':Js('2')}))
                            var.get('admin').callprop('database').callprop('ref', (Js('messages/')+var.get('uid'))).callprop('push', Js({'name':Js('System'),'text':Js('Column mapping has been successfully done.'),'botReply':Js('true'),'photoUrl':Js('/images/profile_placeholder.png')}))
                            var.get('admin').callprop('database').callprop('ref', ((Js('Inventory/')+var.get('inventoryId'))+Js('/ExtractedArray/'))).callprop('set', Js({'array':var.get('companyIndex')}))
                        PyJs_anonymous_39_._set_name('anonymous')
                        var.get('bucket').callprop('upload', Js('/tmp/test.txt'), Js({'destination':((Js('Edited/')+var.get('lastFileName'))+Js('.txt'))})).callprop('then', PyJs_anonymous_39_)
                    except PyJsException as PyJsTempException:
                        PyJsHolder_657272_48166646 = var.own.get('err')
                        var.force_own_put('err', PyExceptionToJs(PyJsTempException))
                        try:
                            var.get('console').callprop('log', var.get('err').get('message'))
                            var.get('admin').callprop('database').callprop('ref', ((Js('error/')+var.get('uid'))+Js('/'))).callprop('set', Js({'columnMapping':Js("Network error. Couldn't complete column mapping.")}))
                            var.get('admin').callprop('database').callprop('ref', (Js('messages/')+var.get('uid'))).callprop('push', Js({'name':Js('System'),'text':Js("Network error. Couldn't complete column mapping."),'botReply':Js('true'),'photoUrl':Js('/images/profile_placeholder.png')}))
                        finally:
                            if PyJsHolder_657272_48166646 is not None:
                                var.own['err'] = PyJsHolder_657272_48166646
                            else:
                                del var.own['err']
                            del PyJsHolder_657272_48166646
                except PyJsException as PyJsTempException:
                    PyJsHolder_6572726f72_74035783 = var.own.get('error')
                    var.force_own_put('error', PyExceptionToJs(PyJsTempException))
                    try:
                        var.get('console').callprop('log', var.get('error').get('message'))
                        var.get('admin').callprop('database').callprop('ref', ((Js('error/')+var.get('uid'))+Js('/'))).callprop('set', Js({'columnMapping':var.get('error').get('message')}))
                        var.get('admin').callprop('database').callprop('ref', (Js('messages/')+var.get('uid'))).callprop('push', Js({'name':Js('System'),'botReply':Js('true'),'text':var.get('error').get('message'),'photoUrl':Js('/images/profile_placeholder.png')}))
                    finally:
                        if PyJsHolder_6572726f72_74035783 is not None:
                            var.own['error'] = PyJsHolder_6572726f72_74035783
                        else:
                            del var.own['error']
                        del PyJsHolder_6572726f72_74035783
            PyJs_anonymous_37_._set_name('anonymous')
            @Js
            def PyJs_anonymous_40_(snapshot, this, arguments, var=var):
                var = Scope({'snapshot':snapshot, 'this':this, 'arguments':arguments}, var)
                var.registers(['snapshot'])
                var.put('output', var.get('snapshot').callprop('val'))
            PyJs_anonymous_40_._set_name('anonymous')
            var.get('admin').callprop('database').callprop('ref', ((Js('Inventory/')+var.get('inventoryId'))+Js('/Data/data'))).callprop('once', Js('value'), PyJs_anonymous_40_).callprop('then', PyJs_anonymous_37_)
        PyJs_anonymous_36_._set_name('anonymous')
        @Js
        def PyJs_anonymous_41_(data, this, arguments, var=var):
            var = Scope({'data':data, 'this':this, 'arguments':arguments}, var)
            var.registers(['data'])
            var.put('lastFileName', (var.get('data').callprop('val').get('companyname')+var.get('getDateInFormat')()))
            var.put('companyCode', var.get('data').callprop('val').get('code'))
        PyJs_anonymous_41_._set_name('anonymous')
        var.get('admin').callprop('database').callprop('ref', ((Js('Inventory/')+var.get('inventoryId'))+Js('/file/'))).callprop('once', Js('value'), PyJs_anonymous_41_).callprop('then', PyJs_anonymous_36_)
    PyJs_anonymous_35_._set_name('anonymous')
    @Js
    def PyJs_anonymous_42_(data, this, arguments, var=var):
        var = Scope({'data':data, 'this':this, 'arguments':arguments}, var)
        var.registers(['data'])
        var.put('uid', var.get('data').callprop('val').get('uid'))
    PyJs_anonymous_42_._set_name('anonymous')
    var.get('admin').callprop('database').callprop('ref', ((Js('Inventory/')+var.get('inventoryId'))+Js('/file/'))).callprop('once', Js('value'), PyJs_anonymous_42_).callprop('then', PyJs_anonymous_35_)
PyJs_anonymous_34_._set_name('anonymous')
var.get('exports').put('eventForFileParsing', var.get('functions').get('database').callprop('ref', Js('/Inventory/{inventoryid}/TemporaryExtractedArray/array')).callprop('onWrite', PyJs_anonymous_34_))
@Js
def PyJs_anonymous_43_(event, this, arguments, var=var):
    var = Scope({'event':event, 'this':this, 'arguments':arguments}, var)
    var.registers(['event', 'snapshot'])
    var.put('snapshot', var.get('event').get('data'))
    if (var.get('snapshot').callprop('val')==Js('Administrator')):
        @Js
        def PyJs_anonymous_44_(data, this, arguments, var=var):
            var = Scope({'data':data, 'this':this, 'arguments':arguments}, var)
            var.registers(['data'])
            var.get('admin').callprop('database').callprop('ref', ((Js('Request/')+var.get('snapshot').get('ref').get('parent').get('key'))+Js('/'))).callprop('set', Js({'firstname':var.get('data').callprop('val').get('firstname'),'lastname':var.get('data').callprop('val').get('lastname'),'email':var.get('data').callprop('val').get('email'),'company':var.get('data').callprop('val').get('companyname')}))
        PyJs_anonymous_44_._set_name('anonymous')
        var.get('admin').callprop('database').callprop('ref', ((Js('users/')+var.get('snapshot').get('ref').get('parent').get('key'))+Js('/'))).callprop('once', Js('value'), PyJs_anonymous_44_)
PyJs_anonymous_43_._set_name('anonymous')
var.get('exports').put('eventForAdminEntry', var.get('functions').get('database').callprop('ref', Js('/users/{uid}/designation/')).callprop('onWrite', PyJs_anonymous_43_))
@Js
def PyJs_anonymous_45_(event, this, arguments, var=var):
    var = Scope({'event':event, 'this':this, 'arguments':arguments}, var)
    var.registers(['event', 'globalCompanyName', 'snapshot'])
    var.put('snapshot', var.get('event').get('data'))
    var.put('globalCompanyName', Js(''))
    @Js
    def PyJs_anonymous_46_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['listOfCompanyId'])
        if (var.get('snapshot').callprop('val')==Js(1.0)):
            @Js
            def PyJs_anonymous_47_(data, this, arguments, var=var):
                var = Scope({'data':data, 'this':this, 'arguments':arguments}, var)
                var.registers(['companyName', 'listOfEmployees', 'data'])
                if (var.get('data').callprop('val').get('designation')==Js('Administrator')):
                    var.get('admin').callprop('database').callprop('ref', ((Js('Request/')+var.get('snapshot').get('ref').get('parent').get('key'))+Js('/'))).callprop('set', Js({'firstname':var.get(u"null"),'lastname':var.get(u"null"),'email':var.get(u"null"),'company':var.get(u"null")}))
                    @Js
                    def PyJs_anonymous_48_(this, arguments, var=var):
                        var = Scope({'this':this, 'arguments':arguments}, var)
                        var.registers([])
                        var.get('admin').callprop('database').callprop('ref', ((Js('users/')+var.get('snapshot').get('ref').get('parent').get('key'))+Js('/'))).callprop('update', Js({'inventorypermission':var.get(u"null"),'code':var.get(u"null")}))
                    PyJs_anonymous_48_._set_name('anonymous')
                    def PyJs_LONG_49_(var=var):
                        return var.get('admin').callprop('database').callprop('ref', ((Js('Company/')+var.get('data').callprop('val').get('companyname'))+Js('/'))).callprop('set', Js({'companyname':var.get('data').callprop('val').get('companyname'),'permission':var.get('data').callprop('val').get('inventorypermission'),'admin':var.get('snapshot').get('ref').get('parent').get('key'),'code':var.get('data').callprop('val').get('code')}))
                    PyJs_LONG_49_().callprop('then', PyJs_anonymous_48_)
                else:
                    var.put('listOfEmployees', Js([]))
                    var.put('companyName', var.get('data').callprop('val').get('companyname'))
                    if (var.get('companyName')!=Js('Other')):
                        @Js
                        def PyJs_anonymous_50_(this, arguments, var=var):
                            var = Scope({'this':this, 'arguments':arguments}, var)
                            var.registers(['uniqueListOfEmployees'])
                            var.get('listOfEmployees').callprop('push', var.get('snapshot').get('ref').get('parent').get('key'))
                            @Js
                            def PyJs_anonymous_51_(a, b, this, arguments, var=var):
                                var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
                                var.registers(['b', 'a'])
                                if (var.get('a').callprop('indexOf', var.get('b'))<Js(0.0)):
                                    var.get('a').callprop('push', var.get('b'))
                                return var.get('a')
                            PyJs_anonymous_51_._set_name('anonymous')
                            var.put('uniqueListOfEmployees', var.get('listOfEmployees').callprop('reduce', PyJs_anonymous_51_, Js([])))
                            var.get('admin').callprop('database').callprop('ref', ((Js('Company/')+var.get('companyName'))+Js('/'))).callprop('update', Js({'employees':var.get('uniqueListOfEmployees')}))
                        PyJs_anonymous_50_._set_name('anonymous')
                        @Js
                        def PyJs_anonymous_52_(oldListOfEmployees, this, arguments, var=var):
                            var = Scope({'oldListOfEmployees':oldListOfEmployees, 'this':this, 'arguments':arguments}, var)
                            var.registers(['oldListOfEmployees'])
                            @Js
                            def PyJs_anonymous_53_(grandchildnapshot, this, arguments, var=var):
                                var = Scope({'grandchildnapshot':grandchildnapshot, 'this':this, 'arguments':arguments}, var)
                                var.registers(['grandchildnapshot'])
                                var.get('listOfEmployees').callprop('push', var.get('grandchildnapshot').callprop('val'))
                            PyJs_anonymous_53_._set_name('anonymous')
                            var.get('oldListOfEmployees').callprop('forEach', PyJs_anonymous_53_)
                        PyJs_anonymous_52_._set_name('anonymous')
                        var.get('admin').callprop('database').callprop('ref', ((Js('Company/')+var.get('companyName'))+Js('/employees/'))).callprop('once', Js('value'), PyJs_anonymous_52_).callprop('then', PyJs_anonymous_50_)
            PyJs_anonymous_47_._set_name('anonymous')
            var.get('admin').callprop('database').callprop('ref', ((Js('users/')+var.get('snapshot').get('ref').get('parent').get('key'))+Js('/'))).callprop('once', Js('value'), PyJs_anonymous_47_)
            var.put('listOfCompanyId', Js([]))
            @Js
            def PyJs_anonymous_54_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers([])
                var.get('admin').callprop('database').callprop('ref', ((Js('UserAccessMapping/')+var.get('snapshot').get('ref').get('parent').get('key'))+Js('/'))).callprop('update', Js({'fileaccess':var.get('listOfCompanyId')}))
            PyJs_anonymous_54_._set_name('anonymous')
            @Js
            def PyJs_anonymous_55_(subsnapshot, this, arguments, var=var):
                var = Scope({'subsnapshot':subsnapshot, 'this':this, 'arguments':arguments}, var)
                var.registers(['subsnapshot'])
                @Js
                def PyJs_anonymous_56_(subchildsnapshot, this, arguments, var=var):
                    var = Scope({'subchildsnapshot':subchildsnapshot, 'this':this, 'arguments':arguments}, var)
                    var.registers(['subchildsnapshot'])
                    if (var.get('subchildsnapshot').callprop('val').get('permission')==Js('Public')):
                        var.get('listOfCompanyId').callprop('push', var.get('subchildsnapshot').callprop('val').get('code'))
                    else:
                        if (var.get('subchildsnapshot').callprop('val').get('permission')==Js('Protected')):
                            if (var.get('globalCompanyName')==var.get('subchildsnapshot').get('key')):
                                var.get('listOfCompanyId').callprop('push', var.get('subchildsnapshot').callprop('val').get('code'))
                        else:
                            var.get('console').callprop('log', Js('private'))
                PyJs_anonymous_56_._set_name('anonymous')
                var.get('subsnapshot').callprop('forEach', PyJs_anonymous_56_)
            PyJs_anonymous_55_._set_name('anonymous')
            var.get('admin').callprop('database').callprop('ref', Js('Company')).callprop('once', Js('value'), PyJs_anonymous_55_).callprop('then', PyJs_anonymous_54_)
    PyJs_anonymous_46_._set_name('anonymous')
    @Js
    def PyJs_anonymous_57_(user, this, arguments, var=var):
        var = Scope({'user':user, 'this':this, 'arguments':arguments}, var)
        var.registers(['user'])
        var.put('globalCompanyName', var.get('user').callprop('val').get('companyname'))
    PyJs_anonymous_57_._set_name('anonymous')
    var.get('admin').callprop('database').callprop('ref', ((Js('users/')+var.get('snapshot').get('ref').get('parent').get('key'))+Js('/'))).callprop('once', Js('value'), PyJs_anonymous_57_).callprop('then', PyJs_anonymous_46_)
PyJs_anonymous_45_._set_name('anonymous')
var.get('exports').put('eventForUserEntryApproval', var.get('functions').get('database').callprop('ref', Js('/users/{uid}/approvalstatus/')).callprop('onWrite', PyJs_anonymous_45_))
@Js
def PyJs_anonymous_58_(event, this, arguments, var=var):
    var = Scope({'event':event, 'this':this, 'arguments':arguments}, var)
    var.registers(['companyId', 'userId', 'companyCode', 'event', 'permission'])
    if var.get('event').get('data').callprop('exists').neg():
        return var.get('undefined')
    pass
    var.put('companyId', var.get('event').get('data').get('ref').get('parent').get('key'))
    var.put('permission', var.get('event').get('data'))
    @Js
    def PyJs_anonymous_59_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        if var.get('event').get('data').get('previous').callprop('exists'):
            pass
        else:
            if (var.get('permission').callprop('val')==Js('Public')):
                @Js
                def PyJs_anonymous_60_(snapshot, this, arguments, var=var):
                    var = Scope({'snapshot':snapshot, 'this':this, 'arguments':arguments}, var)
                    var.registers(['snapshot'])
                    @Js
                    def PyJs_anonymous_61_(childsnapshot, this, arguments, var=var):
                        var = Scope({'childsnapshot':childsnapshot, 'this':this, 'arguments':arguments}, var)
                        var.registers(['childsnapshot', 'accessString'])
                        var.put('accessString', Js([]))
                        @Js
                        def PyJs_anonymous_62_(this, arguments, var=var):
                            var = Scope({'this':this, 'arguments':arguments}, var)
                            var.registers(['uniqueAccessString'])
                            @Js
                            def PyJs_anonymous_63_(a, b, this, arguments, var=var):
                                var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
                                var.registers(['b', 'a'])
                                if (var.get('a').callprop('indexOf', var.get('b'))<Js(0.0)):
                                    var.get('a').callprop('push', var.get('b'))
                                return var.get('a')
                            PyJs_anonymous_63_._set_name('anonymous')
                            var.put('uniqueAccessString', var.get('accessString').callprop('reduce', PyJs_anonymous_63_, Js([])))
                            var.get('admin').callprop('database').callprop('ref', ((Js('UserAccessMapping/')+var.get('childsnapshot').get('key'))+Js('/'))).callprop('update', Js({'fileaccess':var.get('uniqueAccessString')}))
                        PyJs_anonymous_62_._set_name('anonymous')
                        @Js
                        def PyJs_anonymous_64_(oldAccessString, this, arguments, var=var):
                            var = Scope({'oldAccessString':oldAccessString, 'this':this, 'arguments':arguments}, var)
                            var.registers(['oldAccessString'])
                            @Js
                            def PyJs_anonymous_65_(grandshildnapshot, this, arguments, var=var):
                                var = Scope({'grandshildnapshot':grandshildnapshot, 'this':this, 'arguments':arguments}, var)
                                var.registers(['grandshildnapshot'])
                                var.get('accessString').callprop('push', var.get('grandshildnapshot').callprop('val'))
                            PyJs_anonymous_65_._set_name('anonymous')
                            var.get('oldAccessString').callprop('forEach', PyJs_anonymous_65_)
                            var.get('accessString').callprop('push', var.get('companyCode'))
                        PyJs_anonymous_64_._set_name('anonymous')
                        var.get('admin').callprop('database').callprop('ref', ((Js('UserAccessMapping/')+var.get('childsnapshot').get('key'))+Js('/fileaccess/'))).callprop('once', Js('value'), PyJs_anonymous_64_).callprop('then', PyJs_anonymous_62_)
                    PyJs_anonymous_61_._set_name('anonymous')
                    var.get('snapshot').callprop('forEach', PyJs_anonymous_61_)
                PyJs_anonymous_60_._set_name('anonymous')
                var.get('admin').callprop('database').callprop('ref', Js('users/')).callprop('once', Js('value'), PyJs_anonymous_60_)
            else:
                if (var.get('permission').callprop('val')==Js('Protected')):
                    @Js
                    def PyJs_anonymous_66_(snapshot, this, arguments, var=var):
                        var = Scope({'snapshot':snapshot, 'this':this, 'arguments':arguments}, var)
                        var.registers(['snapshot'])
                        @Js
                        def PyJs_anonymous_67_(childsnapshot, this, arguments, var=var):
                            var = Scope({'childsnapshot':childsnapshot, 'this':this, 'arguments':arguments}, var)
                            var.registers(['childsnapshot', 'accessString'])
                            if (var.get('childsnapshot').callprop('val').get('companyname')==var.get('companyId')):
                                var.put('accessString', Js([]))
                                @Js
                                def PyJs_anonymous_68_(this, arguments, var=var):
                                    var = Scope({'this':this, 'arguments':arguments}, var)
                                    var.registers(['uniqueAccessString'])
                                    @Js
                                    def PyJs_anonymous_69_(a, b, this, arguments, var=var):
                                        var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
                                        var.registers(['b', 'a'])
                                        if (var.get('a').callprop('indexOf', var.get('b'))<Js(0.0)):
                                            var.get('a').callprop('push', var.get('b'))
                                        return var.get('a')
                                    PyJs_anonymous_69_._set_name('anonymous')
                                    var.put('uniqueAccessString', var.get('accessString').callprop('reduce', PyJs_anonymous_69_, Js([])))
                                    var.get('admin').callprop('database').callprop('ref', ((Js('UserAccessMapping/')+var.get('childsnapshot').get('key'))+Js('/'))).callprop('update', Js({'fileaccess':var.get('uniqueAccessString')}))
                                PyJs_anonymous_68_._set_name('anonymous')
                                @Js
                                def PyJs_anonymous_70_(oldAccessString, this, arguments, var=var):
                                    var = Scope({'oldAccessString':oldAccessString, 'this':this, 'arguments':arguments}, var)
                                    var.registers(['oldAccessString'])
                                    @Js
                                    def PyJs_anonymous_71_(grandshildnapshot, this, arguments, var=var):
                                        var = Scope({'grandshildnapshot':grandshildnapshot, 'this':this, 'arguments':arguments}, var)
                                        var.registers(['grandshildnapshot'])
                                        var.get('accessString').callprop('push', var.get('grandshildnapshot').callprop('val'))
                                    PyJs_anonymous_71_._set_name('anonymous')
                                    var.get('oldAccessString').callprop('forEach', PyJs_anonymous_71_)
                                    var.get('accessString').callprop('push', var.get('companyCode'))
                                PyJs_anonymous_70_._set_name('anonymous')
                                var.get('admin').callprop('database').callprop('ref', ((Js('UserAccessMapping/')+var.get('childsnapshot').get('key'))+Js('/fileaccess/'))).callprop('once', Js('value'), PyJs_anonymous_70_).callprop('then', PyJs_anonymous_68_)
                        PyJs_anonymous_67_._set_name('anonymous')
                        var.get('snapshot').callprop('forEach', PyJs_anonymous_67_)
                    PyJs_anonymous_66_._set_name('anonymous')
                    var.get('admin').callprop('database').callprop('ref', Js('users/')).callprop('once', Js('value'), PyJs_anonymous_66_)
                else:
                    @Js
                    def PyJs_anonymous_72_(this, arguments, var=var):
                        var = Scope({'this':this, 'arguments':arguments}, var)
                        var.registers(['accessString'])
                        var.put('accessString', Js([]))
                        @Js
                        def PyJs_anonymous_73_(this, arguments, var=var):
                            var = Scope({'this':this, 'arguments':arguments}, var)
                            var.registers(['uniqueAccessString'])
                            @Js
                            def PyJs_anonymous_74_(a, b, this, arguments, var=var):
                                var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
                                var.registers(['b', 'a'])
                                if (var.get('a').callprop('indexOf', var.get('b'))<Js(0.0)):
                                    var.get('a').callprop('push', var.get('b'))
                                return var.get('a')
                            PyJs_anonymous_74_._set_name('anonymous')
                            var.put('uniqueAccessString', var.get('accessString').callprop('reduce', PyJs_anonymous_74_, Js([])))
                            var.get('admin').callprop('database').callprop('ref', ((Js('UserAccessMapping/')+var.get('userId'))+Js('/'))).callprop('update', Js({'fileaccess':var.get('uniqueAccessString')}))
                        PyJs_anonymous_73_._set_name('anonymous')
                        @Js
                        def PyJs_anonymous_75_(oldAccessString, this, arguments, var=var):
                            var = Scope({'oldAccessString':oldAccessString, 'this':this, 'arguments':arguments}, var)
                            var.registers(['oldAccessString'])
                            @Js
                            def PyJs_anonymous_76_(grandshildnapshot, this, arguments, var=var):
                                var = Scope({'grandshildnapshot':grandshildnapshot, 'this':this, 'arguments':arguments}, var)
                                var.registers(['grandshildnapshot'])
                                var.get('accessString').callprop('push', var.get('grandshildnapshot').callprop('val'))
                            PyJs_anonymous_76_._set_name('anonymous')
                            var.get('oldAccessString').callprop('forEach', PyJs_anonymous_76_)
                            var.get('accessString').callprop('push', var.get('companyCode'))
                        PyJs_anonymous_75_._set_name('anonymous')
                        var.get('admin').callprop('database').callprop('ref', ((Js('UserAccessMapping/')+var.get('userId'))+Js('/fileaccess/'))).callprop('once', Js('value'), PyJs_anonymous_75_).callprop('then', PyJs_anonymous_73_)
                    PyJs_anonymous_72_._set_name('anonymous')
                    @Js
                    def PyJs_anonymous_77_(snapshot, this, arguments, var=var):
                        var = Scope({'snapshot':snapshot, 'this':this, 'arguments':arguments}, var)
                        var.registers(['snapshot'])
                        var.put('userId', var.get('snapshot').callprop('val').get('admin'))
                    PyJs_anonymous_77_._set_name('anonymous')
                    var.get('admin').callprop('database').callprop('ref', ((Js('Company/')+var.get('companyId'))+Js('/'))).callprop('once', Js('value'), PyJs_anonymous_77_).callprop('then', PyJs_anonymous_72_)
    PyJs_anonymous_59_._set_name('anonymous')
    @Js
    def PyJs_anonymous_78_(companycode, this, arguments, var=var):
        var = Scope({'companycode':companycode, 'this':this, 'arguments':arguments}, var)
        var.registers(['companycode'])
        var.put('companyCode', var.get('companycode'))
    PyJs_anonymous_78_._set_name('anonymous')
    var.get('admin').callprop('database').callprop('ref', ((Js('Company/')+var.get('companyId'))+Js('/'))).callprop('once', Js('value'), PyJs_anonymous_78_).callprop('then', PyJs_anonymous_59_)
PyJs_anonymous_58_._set_name('anonymous')
var.get('exports').put('eventForFilePermission', var.get('functions').get('database').callprop('ref', Js('/Company/{companyid}/permission/')).callprop('onWrite', PyJs_anonymous_58_))
pass


# Add lib to the module scope
index = var.to_python()