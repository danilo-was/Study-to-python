#%%
def create_url(
    url,
    checkin,
    checkout,
    adults,
    children,
    infants, 
    pets,
    all_locals,
)->list:
    
    url_final = []

    for location in all_locals:
        url_creat = (create_get_url(
            base_url = ''.join([url,location]),
            checkin = checkin,
            checkout = checkout,
            adults = adults,
            children = children,
            infants = infants,
            pets = pets        
        ))
        url_final = url1.append(url_creat) 
        
    return(url_final)
#%%
def create_get_url(
    base_url: str,
    checkin: str,
    checkout: str,
    adults: str,
    children: int,
    infants: str, 
    pets: str
) -> str:

    parameters = [
        'homes?id=home_tab',
        'checkin={}'.format(checkin),
        'checkout={}'.format(checkout),
        'adults={}'.format(adults),
        'children={}'.format(children),
        'infants={}'.format(infants),
        'pets={}'.format(pets)
    ]
    
    return('/'.join([base_url,'&'.join(parameters)]))
#%%
if(__name__ == "__main__"):

    create_url(
        url = 'https://airbnb.com.br/s/',
        checkin = '2022-04-01',
        checkout = '2022-04-06',
        adults = 2,
        children = 0,
        infants = 1,
        pets = 0,
        all_locals = [
           
        ]
    )
# %%
