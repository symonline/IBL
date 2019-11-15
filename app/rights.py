from app import app

from app import db

from app.models import ShareHolder, Right, HoldersRight

# Allow custom object to be imported automatically into Python shell
# when "flask shell is entered on the os prompt  
@app.shell_context_processor 
def make_shell_contexs():
    return {'db':db ,'ShareHolder':ShareHolder, 'Right':Right, 'HoldersRight':HoldersRight} 
    