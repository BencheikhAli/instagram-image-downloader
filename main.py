import instaloader

image = instaloader.Instaloader()
name = input('Whats the instagram username: ')

image.download_profile(name, profile_pic_only=True)
