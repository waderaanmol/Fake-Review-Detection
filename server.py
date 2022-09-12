from flask import Flask, render_template, request, jsonify
import deploy

app = Flask (__name__)

@app.route ('/')
def index ():
    return render_template ('index.html')
    
@app.route ('/productall')
def productall ():
    return render_template ('products-all.html')
    
@app.route ('/productdetails')
def productdetails ():
    return render_template ('product-details.html')
    
@app.route ('/productdetails1')
def productdetails1 ():
    return render_template ('product-details1.html')

@app.route ('/productdetails2')
def productdetails2 ():
    return render_template ('product-details2.html')

@app.route ('/productdetails3')
def productdetails3 ():
    return render_template ('product-details3.html')

@app.route ('/productdetails4')
def productdetails4 ():
    return render_template ('product-details4.html')

@app.route ('/productdetails5')
def productdetails5 ():
    return render_template ('product-details5.html')

@app.route ('/productdetails6')
def productdetails6 ():
    return render_template ('product-details6.html')

@app.route ('/productdetails7')
def productdetails7 ():
    return render_template ('product-details7.html')



@app.route ('/api/bot', methods = ['POST'])
def say_name ():
	json = request.get_json()

	review_text = request.form['review_text']
	rating = request.form['rating']
	verified_purchase =  request.form['verified_purchase']
	product_category = request.form['product_category']

	result =  deploy.get_result(review_text, rating, verified_purchase, product_category)
	print (result)

	if result[0] == 1:
		return jsonify (result = 'T')

	else:
		return jsonify (result = 'F')

from pyngrok import ngrok

def config_ngrok() :
    app.config['START_NGROK'] = True
    url = ngrok.connect(5000)
    print(' * Public URL:', url)

if __name__ == '__main__':
    config_ngrok()
    app.run ()
