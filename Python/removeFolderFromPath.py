import os
import shutil

def move_songs_to_music_folder(root_folder):
    music_folder = os.path.join(root_folder, 'May23')
    
    # Verificar si existe la carpeta 'music'
    if not os.path.exists(music_folder):
        print(f"La carpeta '{music_folder}' no existe.")
        return
    
    # Obtener una lista de subcarpetas en la carpeta 'music'
    subfolders = [f for f in os.listdir(music_folder) if os.path.isdir(os.path.join(music_folder, f))]
    
    # Recorrer las subcarpetas y mover las canciones a la carpeta 'music'
    for subfolder in subfolders:
        subfolder_path = os.path.join(music_folder, subfolder)
        songs = [f for f in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, f))]
        
        for song in songs:
            song_path = os.path.join(subfolder_path, song)
            shutil.move(song_path, os.path.join(music_folder, song))
        
        # Eliminar la subcarpeta una vez que se han movido las canciones
        shutil.rmtree(subfolder_path)

if __name__ == "__main__":
    root_folder = "C:\\Users\\jimoreno\\Downloads\\Music"  # Reemplaza esta ruta con la ruta de tu carpeta raíz
    
    move_songs_to_music_folder(root_folder)