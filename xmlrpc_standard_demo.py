
import xmlrpclib

info = xmlrpclib.ServerProxy('https://demo.odoo.com/start').start()

url, db, username, password = info['host'], info['database'], info['user'], info['password']
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, username, password, {})

version = common.version()

models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
models.execute_kw(db, uid, password,
    'res.partner', 'check_access_rights',
    ['read'], {'raise_exception': False})

#to list the records
list_ids = models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [[['is_company', '=', True], ['customer', '=', True]]])
print "list_ids",list_ids

#pagination
page_ids = models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [[['is_company', '=', True], ['customer', '=', True]]],
    {'offset': 10, 'limit': 5})
print "page_ids",page_ids

#to count the records
count = models.execute_kw(db, uid, password,
    'res.partner', 'search_count',
    [[['is_company', '=', True], ['customer', '=', True]]])
print "coun",count

#to read the records

ids = models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [[['is_company', '=', True], ['customer', '=', True]]],
    {'limit': 1})
[record] = models.execute_kw(db, uid, password,
    'res.partner', 'read', [ids])
# count the number of fields fetched by default
print "total no of fields",len(record)

#read only some fields
data = models.execute_kw(db, uid, password,
    'res.partner', 'read',
    [ids], {'fields': ['name', 'country_id', 'comment']})
print "data",data

#get each fieds description
fields_data = models.execute_kw(
    db, uid, password, 'res.partner', 'fields_get',
    [], {'attributes': ['string', 'help', 'type']})
print "fields_data",fields_data

#use search read

search_read_data = models.execute_kw(db, uid, password,
    'res.partner', 'search_read',
    [[['is_company', '=', True], ['customer', '=', True]]],
    {'fields': ['name', 'country_id', 'comment'], 'limit': 5})
print "search_read_data",search_read_data

#create records
cr_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    'name': "Harshit",
}])
print "cr_id",cr_id

#to create model 
model_create_id = models.execute_kw(db, uid, password, 'ir.model', 'create', [{
    'name': "Custom Model",
    'model': "x_custom_model3",
    'state': 'manual',
}])
print "model_create_ids",model_create_id
view_model_fields = models.execute_kw(
    db, uid, password, 'x_custom_model2', 'fields_get',
    [], {'attributes': ['string', 'help', 'type']})
print "view_model_fields",view_model_fields



