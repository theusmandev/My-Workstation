import instaloader

L = instaloader.Instaloader()

# Browser cookies se login lega
L.load_session_from_browser("devurdunovelbank")

# Session save
L.save_session_to_file()

print("✅ Session created successfully (NO password used)")
