from extract.handlers import handleBaseClass

class handle(handleBaseClass):

    def extract(self):
        # TODO: Add super() call for this
        config = self.config

        # Open it up
        z = zipfile.ZipFile(config['fileName'])

        logger.info("Extracting the following files: {0}".format([x.filename for x in z.filelist]))

        # Find the base directory of the file
        directory = os.path.dirname(os.path.abspath(config['fileName']))
        
        # Do the actual extraction
        z.extractall(path=directory)

        # Call parent handler
        handleBaseClass.extract(self)
        
        

import zipfile
import logging
import os

logger = logging.getLogger('extract.handlers.application.zip')
