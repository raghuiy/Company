import db_services
import  db_services as db
from flask import Flask, render_template, request, session

print('Hello Worlds')
#db.write_to_db()

#from FILE import file
app=Flask(__name__)
app.secret_key = 'the random string'
Registrants={}
Colors=['Silver', 'Blue','Green', 'Orange', 'Pink', 'Yellow','Violet']
#largeFile='/Users/raghunathiyer/PycharmProjects/words.txt'
#WORDS=[]
#with open(largeFile, "r") as file:
 #   for line in file.readlines():
 #       WORDS.append(line.rstrip())



@app.route('/')
@app.route('/Sirs')
def index():
    return render_template('welcome.html')

@app.route('/test')
def indexes():
    return('This is a test page')


@app.route('/abbu', methods=['post','get'])
def render():
        # return ('hello Mr Ajjulan')
    if (request.method  == 'GET'):
        grx_name =request.args.get('inp')
    elif ((request.method =='POST')):
        grx_name = request.form.get('user')
        print('grx name is:', grx_name)
        db.write_to_reg_db(grx_name)
    session['gr_name'] = grx_name
    #print('Input from browser is :', grx_name)

    return render_template('greet.html',pr_name=grx_name, t_colours=Colors)

@app.route('/showResults')
def showResultsPg():
    col=request.args.get('favColor')
    Registrants.update({session['gr_name']: col})
    db_services.write_to_choice_db([3,col])
    print('Col= ',col ,' and ',session.get('gr_name'))
    #Registrants.append(kvp)
    return render_template('results.html', f_col=col,person=session.get('gr_name'))

@app.route('/showRegistrants')
def showRegistrants():
    return render_template('registrants.html',RG=Registrants)


@app.route('/search')
def search():
        return render_template('search.html')

@app.route('/showSearchResults')
def showSearchResults():
        searchQuery=request.args.get('qry')
        words =[word for word in WORDS if (word.startswith(searchQuery))]
        return render_template('searchResults.html', queryResults=words)

@app.route('/showPureJSSearchResults')
def showPureJSResults():
    searchQuery = request.args.get('qry')
    #print('Base URL', request.headers)
    print('Search query was: ',searchQuery)
    words = [word for word in WORDS if (word.startswith(searchQuery))]
    return render_template('pureJSResults.html', queryResults=words)

@app.route('/jsSearch')
def JSsearch():
        return render_template('pureJS.html')

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'




if __name__== '__main__':
    app.debug=True
    app.run(host="0.0.0.0", port=5000)

