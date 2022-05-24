from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (?, ?, ?) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album
   
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)


def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)
    
    if album is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], artist, result['genre'], result['id'])
    return album

### EXTENSIONS


def delete(id):
    sql = "DELETE FROM albums WHERE id = ?"
    values = [id]
    run_sql(sql, values)

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    
    for row in results:
        album = Album(row['title'], row['artist_id'], row['genre'], row['id'])
        albums.append(album)
    return albums

def update(album):
    sql = "UPDATE albums SET (title, genre, artist_id) = (?,?,?) WHERE id = ?"
    values = [album.title, album.genre, album.artist.id, album.id]
    run_sql(sql, values)
