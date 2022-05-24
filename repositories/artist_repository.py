from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def save(artist):
   sql = "INSERT INTO artists (id, name) VALUES (?, ?) RETURNING *"
   values = [artist.id, artist.name]
   results = run_sql(sql, values)
   id = results[0]['id']
   artist.id = id
   return artist
   

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        artist = Artist(result['name'], result['id'])
    return artist
    
    

def albums(artist):
    albums = []
    sql = "SELECT * FROM albums WHERE artist_id = ?"
    values = [artist.id]
    results = run_sql(sql, values)
    
    for row in results:
        album = Album(row['id'], row['title'], row['genre'], artist)
        albums.append(album)
    return albums

### EXTENSIONS

def select_all():
    artists= []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    
    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists

def delete(id):
    id = None
    sql = "DELETE FROM artists WHERE id = ?"
    value = [id]
    run_sql(sql,value)
    

def update(artist):
    sql = "UPDATE FROM artists SET (name, id) = (?,?)"
    values = [artist.name, artist.id]
    run_sql(sql, values)
    
    
