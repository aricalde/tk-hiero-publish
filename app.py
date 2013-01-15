"""
Copyright (c) 2012 Cluster Studio S. C.
----------------------------------------------------------

Publish in Hiero

"""

from tank.platform import Application

class HieroPublish(Application):
    
    def init_app(self):
        """
        Called as the application is being initialized
        """
        tk_hiero_publish = self.import_module("tk_hiero_publish")
        
    
    def destroy_app(self):
        """
        Called as the application is being destroyed
        """
        self.log_debug("Destroying tk-hiero-publish")
