from extract.handlers import handleBaseClass

class handle(handleBaseClass):

    def _libarchive(self):
        try:
            # Do the actual extraction
            with open(config['fileName'],"rb") as f:                                            
                for entry in libarchive.public.memory_pour(f.read()):
                    pass
            return True

        except:
            return False
        
    def _lrunzip(self):
        # Make sure it exists
        if not shutil.which("lrunzip"):
            logger.warn("lrunzip not found. try installing it.")
            return False

        try:
            subprocess.check_output(["lrunzip",self.config['fileName']])
            return True

        except:
            return False


    def extract(self):
        # List of preferred extraction options
        extract_options = [
            self._libarchive,
            self._lrunzip,
        ]

        config = self.config

        # Find the base directory of the file
        directory = os.path.dirname(os.path.abspath(config['fileName']))

        # Default to extracting to the same directory
        os.chdir(directory)

        # Try different options
        if not any(option() for option in extract_options):
            logger.error("Extraction attempts failed!")
            # Return before we accidentally remove the file
            return False

        # Call parent handler
        handleBaseClass.extract(self)
        

import logging
import os
import libarchive.public
import subprocess
import shutil

logger = logging.getLogger('extract.handlers.application.x_lrzip')
