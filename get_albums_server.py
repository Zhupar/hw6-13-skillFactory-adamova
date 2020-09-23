from bottle import route
from bottle import run
from bottle import HTTPError
import album


@route ("/albums/<artist>")
def albums(artist):
	albums_list=album.find_artist(artist)
	if not albums_list:
		message = "Альбомов {} не найдено".format(artist)
		result = HTTPError(404, message)
	else:
		album_names = [album.album for album in albums_list]
		alb_count=len(album_names)
		result = "Найдено {alb_count} альбомов {artist}:\n".format(alb_count=alb_count, artist=artist)
		result += "\n".join(album_names)
		return result

if __name__ == "__main__":
	run(host="localhost", port=8080, debug=True)

