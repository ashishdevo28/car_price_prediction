# Car Price Prediction Deployment on Heroku

Here we have deoployed a simple app on the Heroku, just to learn the deoployment Processs.



## Process
0. We have created a `README.md` file and we have added all the details about the project.
1. We have used the jupter notebook for the model creation. We have created the model for price prediction(not Time-Series). 
2. After Sucessfully traininhg the model on the jupyer notebook, we have used the model to predict the price of the car.
3. We have created `app.py` and we have trained model file in the `models` folder. We have used Steamlit for the web interface.
4. We have created a `requirements.txt` file and we have installed all the required packages.
5. Now we have created a `setup.sh` file and we have added all the details about the deployment. You can use the same file for deploying the model on the cloud without any changes.
6. The file which is most important here is `Procfile`. It is the file Heroku knowas as the process file. It is the file which tells the Heroku what to do with the app. 
7. Finally this part is done. Now we have to deploy the app on the cloud.
8. Just make Heroku account and follow the steps there.


## Editings
1. We have removed the `pickle` file from repository. But you can add your own here

## Contibutions
If you have any contibutions to this project, please feel free to add it here.