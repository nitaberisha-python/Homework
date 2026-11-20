print("===== PLAYLIST MANAGER =====")

playlist = ["Flowers", "Blinding Lights", "Shape of You", "Levitating", "Flowers"]

print(f"Playlist: {playlist}")
print(f"Songs: {len(playlist)}")
print(f"First Song: {playlist[0]}")
print(f"Last Song: {playlist[-1]}")

playlist.append("Houdini")
playlist.insert(1, "Calm Down")

new_songs = ["As It Was", "Anti-Hero"]
playlist.extend(new_songs)

print(f"After Adding: {playlist}")

flowers_count = playlist.count("Flowers")
print(f"Flowers Count: {flowers_count}")

playlist.remove("Flowers")
print(f"After Remove: {playlist}")

levitating_position = playlist.index("Levitating")
print(f"Levitating Position: {levitating_position}")

if "Despacito" in playlist:
    print("Despacito Found: Yes")
else:
    print("Despacito Found: No")

skipped_song = playlist.pop()
print(f"Skipped: {skipped_song}")

played_song = playlist.pop(0)
print(f"Now Played: {played_song}")

playlist.sort()

print(f"Sorted: {playlist}")
print(f"Songs Left: {len(playlist)}")

print("============================")