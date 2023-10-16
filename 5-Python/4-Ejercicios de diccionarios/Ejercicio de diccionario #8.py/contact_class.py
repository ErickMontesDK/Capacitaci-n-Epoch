from datetime import datetime

class Contact:
    def __init__(self):
        self.contact = {}
        
    def set_personal_data (self, name, birth_date, genre):        
        date = datetime.strptime(birth_date, "%d-%m-%Y")
        date = date.strftime("%a-%m-%Y")
            
        personal_data = {
            'datos personales': { 
                'nombre' : name,
                'fecha_de_nacimiento': date,
                'genero': genre
            } 
        }
        
        self.contact.update(personal_data)
        
    def set_contact_data (self, phones, email):
        datos_contacto = {
            'datos_contacto':{
                'telefonos': phones,
                'email': email
            }
        }
        
        self.contact.update(datos_contacto)
        
    def set_address (self, street, city, state):
        address = {
            'domicilio':{
                'calle_numero': street,
                'ciudad': city,
                'entidad': state
            }
        }
        
        self.contact.update(address)
        
    def set_hobbies (self, sports, movies, music_genres, music_artists):
        hobbies = {
            'hobbies': {
                'deportes': sports,
                'películas': movies,
                'generos': music_genres,
                'grupos': []
            }
        }
        
        print(hobbies.hobbies.grupos)
        
        for artist in music_artists.keys():
            artist_element = { 'nombre': artist, 'canciones':music_artists.get(f'{artist}')}
            print(artist_element)
            
            
            # .grupos.append(artist_element)
            
        self.contact.update(hobbies)
            
    def __str__(self):
        return f"{self.contact}"
        