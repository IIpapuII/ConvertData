from Script.controller.view  import *
from Script import create_app,db
from Script.db.dbconect import init_app
app = create_app()
if __name__ =='__main__':
    init_app()
    app.run(debug=True)