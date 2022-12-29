import random, ascii, os
import requests

#Vyber ceskych mest pres api s limitem
API_KEY = ascii.api_key
country_id = "cz"
limit = 30
url = f"https://api.api-ninjas.com/v1/city?country={country_id}&limit={limit}"
response = requests.get(url, headers={"X-Api-Key":API_KEY})
text = response.json()
city = random.choice(text)["name"].upper()

#Generace listu pro neodkryty nazev s osetrenim mezery 
guess_city =[("?" if i != " " else " ") for i in city]
start_pos = 0


while True:
    os.system("cls")
    guess_city_str = ""
    char_found = False
    print(ascii.hangman_positions[start_pos])
    print(guess_city)
    guess_char = input("Guess the letter: ").upper()
    
    #Kontrola zda je pismeno v nektere pozici, pokud ano, zmeni danou pozici v neodkrytem liste na pismeno  
    for i in range(len(city)):
        if guess_char == city[i]:
            guess_city[i] = guess_char
            char_found = True
            
    #Pokud v cyklu nenašel písmeno, tak změní pozici obrázku sibenice             
    if char_found == False:
        start_pos += 1
        
    #Prevod listu do stringu pro nasledne porovnani      
    for char in guess_city:
        guess_city_str += char
        
    #Vyhodnoceni zda je nalezeno vse nebo je prekrocen pocet pokusu (pokusy dle mnozstvi obrazku) 
    if guess_city_str.upper() == city:
        print(f"Well done, you win! Name of city {city}")
        break
    elif start_pos >= (len(ascii.hangman_positions)-1):
        os.system("cls")
        print(ascii.hangman_positions[start_pos])
        print(f"Too much attmepts, game over! Name of city {city}")
        break 
