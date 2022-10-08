# Creation d'une API pour présenter les différents projets que j'ai en Data Science.

from flask import Flask, render_template, make_response, request, redirect, url_for, send_file
import joblib
import pandas as pd
import numpy as np
import os
import sklearn
from sklearn.linear_model import LogisticRegression

from predictions_file import predict_bills

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("index.html")
##############################################################################################
@app.route('/p1_presentation', methods=['GET', 'POST'])
def p1_presentation():
    return render_template("/p1_base_de_donnees_sql_immo/p1_presentation.html")

@app.route('/p1_code_python', methods=['GET', 'POST'])
def p1_code_python():
    return render_template("/p1_base_de_donnees_sql_immo/p1_code_python.html")

@app.route('/p1_code_table_donnees', methods=['GET', 'POST'])
def p1_code_table_donnees():
    return render_template("/p1_base_de_donnees_sql_immo/p1_code_table_donnees.html")

@app.route('/p1_queries', methods=['GET', 'POST'])
def p1_queries():
    return render_template("/p1_base_de_donnees_sql_immo/p1_queries.html")

@app.route('/p1_resultat_queries', methods=['GET', 'POST'])
def p1_resultat_queries():
    return render_template("/p1_base_de_donnees_sql_immo/p1_resultat_queries.html")
#########################################################################
@app.route('/p2_presentation', methods=['GET', 'POST'])
def p2_presentation():
    return render_template("p2_etude_de_marche/p2_presentation.html")

@app.route('/p2_notebook_etude_de_marche', methods=['GET', 'POST'])
def p2_notebook_etude_de_marche():
    return render_template("p2_etude_de_marche/p2_notebook_etude_de_marche.html")
#########################################################################
@app.route('/p3_presentation', methods=['GET', 'POST'])
def p3_presentation():
    return render_template("/p3_detection_faux_billet/p3_presentation.html")

@app.route('/p3_notebook_detection_faux_billet', methods=['GET', 'POST'])
def p3_notebook_detection_faux_billet():
    return render_template("/p3_detection_faux_billet/p3_notebook_detection_faux_billet.html")
###
app.config["DEBUG"] = True
loaded_model = joblib.load("lrmodel.sav")

@app.route('/api_detection_faux_billet')
def index():
    return render_template('/p3_detection_faux_billet/p3_home_detection_faux_billet.html')
#This first part give user interface where the home.html file display, the uplaod and submit button.

@app.route('/api_detection_faux_billet', methods=['GET', 'POST'])
def uploadFiles():
    uploaded_file = request.files['file']
    #request.files allow the utilisator to import a file and send/post it to the server.
    #Note that 'file' is not the filename; it's the name of the form field (home.html --> name="file") containing the file.
    
    if uploaded_file.filename != '':
    #uploaded_file now contain the file because it uploaded it but if there are no uploaded file,
    #there are no way to know the name of the file for the api.
    #So, xyz.filename is an attribut that know the file name that was uploaded, and the if statement,
    #above say that if the filename of the uploaded file is different than '' so, there are a file uploaded. 
        file_path = ( "file.csv")
        uploaded_file.save(file_path)
    return redirect(url_for('downloadFile'))
    #And we give the filename with it's extensions (.csv) will be stored in a varaible.
    #Then with the .save attribut we save it.
#now we are reading the file, make predictions with our model and save the predictions.
#then we are sending the CSV with the predictions to the user as attachement 
@app.route('/download')
def downloadFile ():
    path = "file.csv"
    #Now we call back the file for use it here in the page where we can give the file inside the model.
    predictions = predict_bills(pd.read_csv(path))
    #We create a variable that use the predict_bills function in order to read the csv file that we upload.
    #For more informations about this function go to predictions_file.py.
    predictions.to_csv('predictions.csv',index=False)
    #Then we save as a csv file the results.
    return send_file("predictions.csv", as_attachment=True)
    #And thanks to the return and send_file function we dowloaded the file with the results.
###################################################################################################

@app.route('/p4_presentation', methods=['GET', 'POST'])
def p4_presentation():
    return render_template("/p4_etude_sante_public/p4_presentation.html")

@app.route('/p4_notebook_etude_sante_public', methods=['GET', 'POST'])
def p4_notebook_etude_sante_public():
    return render_template("p4_etude_sante_public/p4_notebook_etude_sante_public.html")
#################################################################################################
@app.route('/p5_presentation', methods=['GET', 'POST'])
def p5_presentation():
    return render_template("/p5_optimisation_donnees_boutique/p5_presentation.html")

@app.route('/p5_notebook_optimisation_donnees_boutique', methods=['GET', 'POST'])
def p5_notebook_optimisation_donnees_boutique():
    return render_template("/p5_optimisation_donnees_boutique/p5_notebook_optimisation_donnees_boutique.html")
##################################################################################################
@app.route('/p6_presentation', methods=['GET', 'POST'])
def p6_presentation():
    return render_template("/p6_analyse_vente_librairie/p6_presentation.html")

@app.route('/p6_notebook_analyse_vente_librairie_eda', methods=['GET', 'POST'])
def p6_notebook_analyse_vente_librairie_eda():
    return render_template("/p6_analyse_vente_librairie/p6_notebook_analyse_vente_librairie_eda.html")

@app.route('/p6_notebook_analyse_vente_librairie_rassemblement_date', methods=['GET', 'POST'])
def p6_notebook_analyse_vente_librairie_rassemblement_date():
    return render_template("/p6_analyse_vente_librairie/p6_notebook_analyse_vente_librairie_rassemblement_date.html")

@app.route('/p6_notebook_analyse_vente_librairie_antoine', methods=['GET', 'POST'])
def p6_notebook_analyse_vente_librairie_antoine():
    return render_template("/p6_analyse_vente_librairie/p6_notebook_analyse_vente_librairie_antoine.html")

@app.route('/p6_notebook_analyse_vente_librairie_julie', methods=['GET', 'POST'])
def p6_notebook_analyse_vente_librairie_julie():
    return render_template("/p6_analyse_vente_librairie/p6_notebook_analyse_vente_librairie_julie.html")
##############################################################################################################
@app.route('/p7_presentation', methods=['GET', 'POST'])
def p7_presentation():
    return render_template("/p7_analyse_indicateur_egalite_hf/p7_presentation.html")

@app.route('/p7_notebook_preparation_donnees', methods=['GET', 'POST'])
def p7_notebook_preparation_donnees():
    return render_template("/p7_analyse_indicateur_egalite_hf/p7_preparation_donnees.html")

@app.route('/p7_notebook_anonymisation_data_csv', methods=['GET', 'POST'])
def p7_notebook_anonymisation_data_csv():
    return render_template("/p7_analyse_indicateur_egalite_hf/p7_anonymisation_data_csv.html")
#############################################################################################################
@app.route('/p8_presentation', methods=['GET', 'POST'])
def p8_presentation():
    return render_template("/p8_etude_eau_tableau/p8_presentation.html")
########################################################################################





if __name__ == '__main__':
    app.run(debug = True)



