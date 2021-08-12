import streamlit as st
import pickle
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))

def main():
    st.title("Check You Car Selling Price")
    st.markdown("##### Do you want to sell your car? \n##### And want to know selling price....")

    # @st.cache(allow_output_mutation=True)
    # def get_model():
    #     model = pickle.load(open('RF_price_predicting_model.pkl','rb'))
    #     return model


    st.write('')
    st.write('')

    years = st.number_input('In which year car was purchased?',1990,2021, step=1, key = 'year')
    Years_old = 2021-years

    Present_Price = st.number_input('What is the current on-road price of the car? (In ₹lakhs)', 0.00, 50.00, step=0.5, key ='present_price') 

    Kms_Driven = st.number_input("How much car has covered distance?",0.00, 500000.00, step = 500.00, key='drived')

    Owner = st.radio("The number of owners the car had previously?", (0,1,3), key='owner')

    Fuel_Type_Petrol = st.selectbox("What type of fuel car has?",('Petrol','Diesel','CNG'), key='fuel')
    if(Fuel_Type_Petrol == 'Petrol'):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
    elif(Fuel_Type_Petrol == 'Diesel'):
        Fuel_Type_Petrol = 0
        Fuel_Type_Diesel = 1
    else:
        Fuel_Type_Petrol = 0
        Fuel_Type_Diesel = 0

    Seller_Type_Individual = st.selectbox('Are you Dealer or Individual?',('Dealer','Individual'), key='dealer')
    if(Seller_Type_Individual == 'Individual'):
        Seller_Type_Individual = 1
    else:
        Seller_Type_Individual = 0

    Transmission_Mannual = st.selectbox('What is the Transmission Type ?', ('Manual','Automatic'), key='manual')
    if(Transmission_Mannual=='Mannual'):
        Transmission_Mannual=1
    else:
        Transmission_Mannual=0

    if st.button("Estimate Price", key='predict'):
        Model = model  #get_model()
        prediction = Model.predict([[Present_Price, Kms_Driven, Owner, Years_old, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
        output = round(prediction[0],2)
        if output<0:
            st.warning("You will be not able to sell car!!")
        else:
            st.success("You can sell at {} Lakhs".format(output))


if __name__ == "__main__":
    main() 