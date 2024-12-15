class DefaultAppRouter:
    
    def db_for_read(self, model, **hints):
        if model._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
            return 'django_db'
        return None
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
            return 'django_db'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin'] and obj2._meta.app_label in ['auth', 'contenttypes', 'sessions', 'admin']:
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in ['auth', 'contenttypes', 'sessions', 'admin', ]:
            return db == 'django_db'
        return None