#import requried modules

from flask import Flask

    
app = Flask('flaskapp')

#set the proper GET endpoint
@app.route('/app1', methods=["GET"]) 

def helloworld():    
    return 'hello, App1 is up!'
     
if __name__ == '__main__':
    app.run(host='0.0.0.0') 