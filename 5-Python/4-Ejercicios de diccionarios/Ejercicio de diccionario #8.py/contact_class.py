from datetime import datetime
import uuid

class Contact:
    def __init__(self):
        self.id = uuid.uuid4().hex[-3:]
        self.contact = {
            f'{self.id}':{
                'fecha_registro': datetime.now().strftime("%d-%m-%Y"),
                'porcentaje': 0
            }
        }
    def modifiedContact(self, old_contact, id):
        self.contact.clear()
        self.id = id
        self.contact.update(old_contact)
        
    def set_personal_data (self, name="", birth_date="", genre=""): 
        date = ""  
        try:
            date = datetime.strptime(birth_date, "%d-%m-%Y")
            
        except:
            date = datetime.strptime("01-01-2001", "%d-%m-%Y")
            
        date = date.strftime("%d-%m-%Y")     
        personal_data = {
                'datos_personales': { 
                    'nombre' : name,
                    'fecha_de_nacimiento': date,
                    'genero': genre
                } 
            }
            
        return personal_data
        
        
    def set_contact_data (self, phones, email):
        datos_contacto = {
            'datos_contacto':{
                'telefonos': phones,
                'email': email
            }
        }
        
        return datos_contacto
        
    def set_address (self, street, city, state):
        address = {
            'domicilio':{
                'calle_numero': street,
                'ciudad': city,
                'entidad': state
            }
        }
        
        return address
        
    def set_hobbies (self, sports, movies, music_genres, music_artists):
        hobbies = {
            'hobbies': {
                'deportes': sports,
                'películas': movies,
                'musica': {
                    'generos': music_genres,
                    'grupos': []
                }
                
            }
        }
        
        for artist in music_artists.keys():
            artist_element = { 'nombre': artist, 'canciones':music_artists.get(f'{artist}')}
            
            hobbies["hobbies"]["musica"]["grupos"].append(artist_element)
            
        return hobbies
    
    def save_entry(self, entry):
        self.contact[f'{self.id}'].update(entry)
        self.porcentage_status()
        
    def porcentage_status(self):
        self.contact[f'{self.id}'].update({'porcentaje' : 0})
        porcentaje = 5
        
        if self.contact[f'{self.id}'].get("datos_personales") != None:
            porcentaje += 20
        if self.contact[f'{self.id}'].get("datos_contacto") != None:
            porcentaje += 20
        if self.contact[f'{self.id}'].get("domicilio") != None:
            porcentaje += 15
        if self.contact[f'{self.id}'].get("hobbies") != None:
            porcentaje += 40
        self.contact[f'{self.id}'].update({'porcentaje' : porcentaje})
        return porcentaje

    def get_keys(self):
        return self.contact[f'{self.id}'].keys() 
    
    def get_inside_contact(self):
        return self.contact[f'{self.id}']
    
    def get_contact(self):
        return self.contact
    
    def __str__(self):
        return f"{self.contact}"
        