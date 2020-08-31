from db import models

def admin_register_interface(username,password):
    models.Admin(username,password)
    