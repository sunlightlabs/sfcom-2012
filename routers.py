class WordpressRouter(object):
    
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'wordpress':
            return 'wordpress'
        return None
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'wordpress':
            return 'wordpress'
        return None
    
    def allow_syncdb(self, db, model):
        if model._meta.app_label == 'wordpress':
            return False
        return None