import pickle
import streamlit as st
import pandas as pd


file_name = 'model.sav'
model = pickle.load(open(file_name, 'rb'))


@st.cache
def predict(parents_great_pret, parents_pretentious,
       parents_usual, has_nurs_critical, has_nurs_improper,
       has_nurs_less_proper, has_nurs_proper, has_nurs_very_crit,
       form_complete, form_completed, form_foster, form_incomplete,
       children_1, children_2, children_3, children_more,
       housing_convenient, housing_critical, housing_less_conv,
       finance_convenient, finance_inconv, social_nonprob,
       social_problematic, social_slightly_prob, health_not_recom,
       health_priority, health_recommended):
    prediction = model.predict(pd.DataFrame([[parents_great_pret, parents_pretentious,
       parents_usual, has_nurs_critical, has_nurs_improper,
       has_nurs_less_proper, has_nurs_proper, has_nurs_very_crit,
       form_complete, form_completed, form_foster, form_incomplete,
       children_1, children_2, children_3, children_more,
       housing_convenient, housing_critical, housing_less_conv,
       finance_convenient, finance_inconv, social_nonprob,
       social_problematic, social_slightly_prob, health_not_recom,
       health_priority, health_recommended]], columns=['parents_great_pret', 'parents_pretentious',
       'parents_usual', 'has_nurs_critical', 'has_nurs_improper',
       'has_nurs_less_proper', 'has_nurs_proper', 'has_nurs_very_crit',
       'form_complete', 'form_completed', 'form_foster', 'form_incomplete',
       'children_1', 'children_2', 'children_3', 'children_more',
       'housing_convenient', 'housing_critical', 'housing_less_conv',
       'finance_convenient', 'finance_inconv', 'social_nonprob',
       'social_problematic', 'social_slightly_prob', 'health_not_recom',
       'health_priority', 'health_recommended']))
    return prediction




st.title('Nursery')
st.header('Entre las características de la  planilla de matrícula:')
parents = st.selectbox(
    'Parents:',
    ('great_pret', 'pretentious','usual')
)
if(parents == 'great_pret'):
    parents_great_pret = 1
    parents_pretentious=0
    parents_usual = 0
elif(parents == 'pretentious'):
    parents_pretentious = 1
    parents_great_pret=0 
    parents_usual = 0
elif(parents == 'usual'):
    parents_usual = 1
    parents_pretentious=0 
    parents_great_pret = 0

#---------------------------------------------------------
has_nurs = st.selectbox(
    'Has a nursery:',
    ('proper', 'less_proper', 'improper', 'critical', 'very_crit')
)
if(has_nurs == 'proper'):
    has_nurs_proper = 1
    has_nurs_improper = 0
    has_nurs_less_proper = 0
    has_nurs_very_crit = 0
    has_nurs_critical = 0
elif(has_nurs == 'less_proper'):
    has_nurs_less_proper = 1
    has_nurs_proper = 0
    has_nurs_improper = 0
    has_nurs_very_crit = 0
    has_nurs_critical = 0
elif(has_nurs == 'improper'):
    has_nurs_less_proper = 0
    has_nurs_proper = 0
    has_nurs_improper = 1
    has_nurs_very_crit = 0
    has_nurs_critical = 0
elif(has_nurs == 'critical'):
    has_nurs_less_proper = 0
    has_nurs_proper = 0
    has_nurs_improper = 0
    has_nurs_very_crit = 0
    has_nurs_critical = 1
elif(has_nurs == 'very_crit'):
    has_nurs_less_proper = 0
    has_nurs_proper = 0
    has_nurs_improper = 0
    has_nurs_very_crit = 1
    has_nurs_critical = 0
#----------------------------------------------------------------
form = st.selectbox(
    'Form:',
    ('complete', 'completed', 'incomplete', 'foster')
)
if(form == 'complete'):
    form_complete = 1
    form_completed = 0
    form_foster = 0
    form_incomplete = 0
elif(form == 'completed'):
    form_complete = 0
    form_completed = 1
    form_foster = 0
    form_incomplete = 0
elif(form == 'incomplete'):
    form_complete = 0
    form_completed = 0
    form_foster = 0
    form_incomplete = 1
elif(form == 'foster'):
    form_complete = 0
    form_completed = 0
    form_foster = 1
    form_incomplete = 0
    
#----------------------------------------------------------------
children = st.selectbox(
    'Children:',
    ('1', '2', '3', 'more')
)
if(children == '1'):
    children_1 = 1
    children_2 = 0
    children_3 = 0
    children_more = 0
elif(children == '2'):
    children_1 = 0
    children_2 = 1
    children_3 = 0
    children_more = 0
elif(children == '3'):
    children_1 = 0
    children_2 = 0
    children_3 = 1
    children_more = 0
elif(children == 'more'):
    children_1 = 0
    children_2 = 0
    children_3 = 0
    children_more = 1

#----------------------------------------------------------------
housing = st.selectbox(
    'Housing:',
    ('convenient', 'less_conv', 'critical')
)
if(housing == 'convenient'):
    housing_convenient = 1
    housing_critical = 0
    housing_less_conv = 0
elif(housing == 'less_conv'):
    housing_convenient = 0
    housing_critical = 0
    housing_less_conv = 1
elif(housing == 'critical'):
    housing_convenient = 0
    housing_critical = 1
    housing_less_conv = 0

#---------------------------------------------------------------
finance = st.selectbox(
    'Finance:',
    ('convenient', 'inconv')
)
if(finance == 'convenient'):
    finance_convenient = 1 
    finance_inconv = 0
elif(finance == 'inconv'):
    finance_convenient = 0 
    finance_inconv = 1

#--------------------------------------------------------------
social = st.selectbox(
    'Social:',
    ('nonprob', 'slightly_prob', 'problematic')
)
if(social == 'nonprob'):
    social_nonprob = 1
    social_problematic = 0
    social_slightly_prob = 0
elif(social == 'slightly_prob'):
    social_nonprob = 0
    social_problematic = 0
    social_slightly_prob = 1
elif(social == 'problematic'):
    social_nonprob = 0
    social_problematic = 1
    social_slightly_prob = 0

#-------------------------------------------------------------
health = st.selectbox(
    'Health:',
    ('recommended', 'priority', 'not_recom')
)
if(health == 'recommended'):
    health_not_recom = 0
    health_priority = 0
    health_recommended = 1
elif(health == 'priority'):
    health_not_recom = 0
    health_priority = 1
    health_recommended = 0
elif(health == 'not_recom'):
    health_not_recom = 1
    health_priority = 0
    health_recommended = 0


if st.button('Predecir la posibilidad de la aceptación en la guardería'):
    value = predict(parents_great_pret, parents_pretentious,
       parents_usual, has_nurs_critical, has_nurs_improper,
       has_nurs_less_proper, has_nurs_proper, has_nurs_very_crit,
       form_complete, form_completed, form_foster, form_incomplete,
       children_1, children_2, children_3, children_more,
       housing_convenient, housing_critical, housing_less_conv,
       finance_convenient, finance_inconv, social_nonprob,
       social_problematic, social_slightly_prob, health_not_recom,
       health_priority, health_recommended)
    if value == 0:
        st.header('Not Recommended')
    elif value == 1:
        st.header('Recommended')
    elif value == 2:
        st.header('Very Recommended')
    elif value == 3:
        st.header('Priority')
    else:
        st.header('Special Priority')
    