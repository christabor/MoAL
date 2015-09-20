# Eve model settings.
DOMAIN = {
    'person': {
        'schema': {
            'name': {
                'type': 'string', 'maxlength': 50,
            }
        }
    },
    'robot': {
        'schema': {
            'model': {
                'type': 'string', 'maxlength': 50
            }
        }
    },
    'cyborg': {
        'schema': {
            'name': {
                'type': 'string', 'maxlength': 50
            }
        }
    }
}

# Declaratively configure resource properties
DOMAIN['person'].update({
    'item_title': 'person',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    # 'additional_lookup': {
    #     'url': 'regex)"[\w]+")',
    #     'field': 'name'
    # }
})

DOMAIN['robot'].update({
    'item_title': 'person',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    # 'additional_lookup': {
    #     'url': 'regex)"[\w]+")',
    #     'field': 'model'
    # }
})

DOMAIN['cyborg'].update({
    'item_title': 'cyborg',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    # 'additional_lookup': {
    #     'url': 'regex)"[\w]+")',
    #     'field': 'model'
    # }
})

# /<entity>
RESOURCE_METHODS = ['GET', 'POST']
# /<entity>/<id>
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# Mongo settings
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
# MONGO_USERNAME = 'moaluser'
# MONGO_PASSWORD = 'password'
# MONGO_DBNAME = 'moal_rest'

# Redis settings
# ------------

# Rate limiting
RATE_LIMIT_GET = (1, 60)
