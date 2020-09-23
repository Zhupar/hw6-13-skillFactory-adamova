import os
import json

from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request
import album
import year_validation

@route("/albums", method="POST")
def add_album():
    year=request.forms.get("year") 
    
    try:
        year_validation.year_validation(year) #проверяет валидность значения для года

    except Exception:
        return HTTPError(400, 'Некорректное значение для года!')

    else:
        new_album = album.Album(
        year= year,
        artist= request.forms.get("artist"),
        genre = request.forms.get("genre"),
        album= request.forms.get("album")
        )
         
    if not (album.find_album(new_album)):
        album.save(new_album)
    else:
        raise HTTPError(409, f'Альбом {new_album.album} существует') 

    
if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)