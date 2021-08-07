import streamlit as st
import pickle

model = pickle.load(open('random_forest_regression_model.pkl','rb'))

def main():
    st.title("Car Selling Price Prediction")
    st.markdown("#### Do you want to sell your Car? \n#### Check your selling price.......")

    st.write('')
    st.write('')

    years = st.number_input("Which year you have purchased car?",1990, 2021, step=1, key='year')
    Years_old = 2021-years

    Present_Price = st.number_input('What is on-road price of the car? (In Lakhs)', 0.00, 50.00, step=0.5, key="present_price")

    Kms_Driven = st.number_input('How much distance covered till now?',0.00, 500000.00, step=500.00, key = 'drived')

    Owner = st.radio("The number of owners car hd previously?", (0, 1, 3), key='owner')

    Fuel_Type_Petrol = st.selectbox('What is fuel type of the car?', ('Petrol', 'Diesel', 'CNG'), key = 'fuel')
    if(Fuel_Type_Petrol== 'Petrol'):
        Fuel_Type_Petrol = 1
        Fuel_Type_Diesel = 0
    elif(Fuel_Type_Petrol == 'Diesel'):
        Fuel_Type_Petrol = 0
        Fuel_Type_Diesel = 1
    else:
        Fuel_Type_Petrol = 0
        Fuel_Type_Diesel = 0

    Seller_Type_Individual = st.selectbox('Are you a dealer or an individual?', ('Dealer', 'Individual'), key='dealer')
    if Seller_Type_Individual == 'Individual':
        Seller_Type_Individual = 1
    else:
        Seller_Type_Individual = 0
    Transmission_Mannual = st.selectbox('What is Transmission Type?', ('Manual', 'Automatic'), key='manual')
    if Transmission_Mannual == 'Mannual':
        Transmission_Mannual = 1
    else:
        Transmission_Mannual = 0

    if st.button("Predict Price", key='predict'):
        try:
            Model = model
            predicition = Model.predict([[Present_Price, Kms_Driven, Owner, Years_old, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
            output = round(predicition[0],2)
            if output < 0:
                st.warning("You can't sell car!")
            else:
                st.success("You can sell car for {}".format(output))

        except:
            st.warning("Something went wrong\n Try Again")

if __name__ == '__main__':
    main()
