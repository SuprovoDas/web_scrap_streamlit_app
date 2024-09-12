import streamlit as st
import requests

from beautifulsoup4 import BeautifulSoup

doctor_options = ['Dentist','Physician','Dermatologist','Gynecologist/Obstetrician',
                  'Ear Nose Throat (ENT) Specialist','Pediatrician','Ophthalmologist','Dermatologist',
                  'Cardiologist','Psychiatrist','Gastroenterologist','Neurologist','Urologist','Prosthodontist',
                'Orthodontist','Pediatric Dentist','Endodontist','Implantologist','Ayurveda','Homoeopath','Siddha','Unani',
                'Yoga & Naturopathy','Acupuncturist','Physiotherapist','Psychologist','Audiologist','Speech Therapist',
                'Dietitian/Nutritionist']
doctor_list = []
consultation_fee = []
web = []
exp = []

st.set_page_config(page_title='Web Scrapping -- practo.com',layout='wide',page_icon='⚕️')

st.markdown("""<h3 style= 'text-align:center;'> Web Scraping -- Practo (Book Doctor's Consultation)  </h1>
""",unsafe_allow_html=True)

with st.form('Search Element'):
    doctor_type= st.selectbox('Specialization',placeholder = "Choose an option",options=doctor_options,index=0)
    doctor_type = doctor_type.replace(" ", "-").replace("/", "-").replace('&','and').replace("(","").replace(")","")
    location= st.text_input('Location')
    submit = st.form_submit_button('Search')
    if submit:
        base_url = requests.get(f"https://www.practo.com/{location}/{doctor_type}")
        if base_url.status_code == 200:
            st.success('Website Scrapped Successfully')
            
            page_no = 1
            while True:
                
                page = requests.get(f'https://www.practo.com/{location}/{doctor_type}?page={page_no}')
                soup = BeautifulSoup(page.content,'html.parser')
                rows = soup.find_all("h2",class_="doctor-name")
                rows2 = soup.find_all("span",{'data-qa-id': 'consultation_fee'})
                rows3 = soup.find_all("div",{'data-qa-id':'doctor_card'},class_="listing-doctor-card")
                rows4 = soup.find_all("div",{'data-qa-id':'doctor_experience'},class_="uv2-spacer--xs-top")
                # Extract and clean each link
                cleaned_links = []
                for div in rows3:
                    a_tags = div.find('a')
                    full_url = a_tags['href']
                    parsed_url = urlparse(full_url)        
                    if f'/{location}/doctor' or f'/{location}/therapist' in parsed_url.path:
                        base_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, '', '', ''))
                        cleaned_links.append(f'https://www.practo.com{base_url}')
                
                if len(rows2)!= 0:
                    for exps in rows4:
                        experience_years = exps.text.strip('years experience overall ')
                        exp.append(int(experience_years))
                    
                    for c_fee in rows2:
                        if 'AED' in c_fee:
                            fee =c_fee.text.strip('AED')
                            fee = fee.replace("Free Consultation",'0')
                            fee = float(fee)*22.86
                        else:
                            fee =c_fee.text.strip('₹')
                            fee = fee.replace("Free Consultation",'0')
                            fee = float(fee)
                        consultation_fee.append(fee)
                    web.extend(cleaned_links)
                    for name in rows:
                        names = name.text.strip()
                        doctor_list.append(names)
                    page_no=page_no+1
                else:
                    break
        else:
            st.warning('We are not currently available in this location')
            submit = False
            

pd.set_option('display.max_colwidth', None)
df3 = pd.DataFrame({'Doctor Name': doctor_list[0::],
                        'Consultation Fees(₹)': consultation_fee[0::],
                        'Experience (Yrs)': exp[0::],
                        'link':web[0::]})

if df3.empty is False:
    col1, col2, col3 = st.columns([1, 8, 1])
    with col2:
        st.markdown("""<h3 style= 'text-align:center;'> Available """f'{doctor_type}  in {location.capitalize()} : {len(doctor_list)}'"""</h3>""",unsafe_allow_html=True)
        st.markdown("""<h5 style= 'text-align:center;'> Overview of Doctors Profile</h5>""",unsafe_allow_html=True)
        st.data_editor(
        df3,
        column_config={
            "link": st.column_config.LinkColumn("View Profile"),
            'Consultation Fees(₹)': st.column_config.NumberColumn(format='%.2f',width=160)
        },hide_index=True)
elif submit == True:
    st.markdown("""<h3 style= 'text-align:center;'>"""f'No  {doctor_type}  Available in  {location.capitalize()}'"""</h3>""",unsafe_allow_html=True)
