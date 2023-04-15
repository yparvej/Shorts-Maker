import ffmpeg
from Fonts import Fonts

# Define the paths and values to everything
number_of_videos = 3
video_folder = "E:/Bots/VideoMaker/videos"
# video_folder = "E:/Bots/VideoMaker/videos/caribbean/darken0.4"
audio_folder = "E:/Bots/VideoMaker/audio"
json_file = "E:/Bots/VideoMaker/sources/spiritual_growth_data.json"
fonts_dir = "E:/Bots/VideoMaker/sources/fonts"
output_folder = "E:/Bots/VideoMaker/customers"
text_source_font = r"C\:/Users/Samurai/AppData/Local/Microsoft/Windows/Fonts/Aloevera-OVoWO.ttf"
image_file = "E:/Bots/VideoMaker/sources/logo.png"
customer_name = "nourishlifeapp"
verse_text_image_path = f"E:/Bots/VideoMaker/verse_images/{customer_name}"
fonts_paths = ['E:/Bots/VideoMaker/sources/fonts/AdventureScript.ttf', 'E:/Bots/VideoMaker/sources/fonts/CoffeeJellyUmai.ttf', 'E:/Bots/VideoMaker/sources/fonts/CourierprimecodeRegular.ttf', 'E:/Bots/VideoMaker/sources/fonts/EbGaramond08Regular-2mWe.ttf', 'E:/Bots/VideoMaker/sources/fonts/FlowersSunday.otf', 'E:/Bots/VideoMaker/sources/fonts/GreenTeaJelly.ttf', 'E:/Bots/VideoMaker/sources/fonts/HeyMarch.ttf', 'E:/Bots/VideoMaker/sources/fonts/Hugamour.ttf', 'E:/Bots/VideoMaker/sources/fonts/LetsCoffee.otf', 'E:/Bots/VideoMaker/sources/fonts/Lightning Script.ttf', 'E:/Bots/VideoMaker/sources/fonts/LikeSlim.ttf', 'E:/Bots/VideoMaker/sources/fonts/LoftygoalsRegular.otf', 'E:/Bots/VideoMaker/sources/fonts/PineappleDays.ttf', 'E:/Bots/VideoMaker/sources/fonts/SunnySpellsBasicRegular.ttf', 'E:/Bots/VideoMaker/sources/fonts/TakeCoffee.ttf', 'E:/Bots/VideoMaker/sources/fonts/WantCoffee.ttf']
fonts_sizes = [100, 95, 70, 70, 65, 85, 75, 73, 50, 85, 75, 75, 52, 87, 50, 65]
fonts_maxcharsline = [38, 34, 25, 35, 30, 45, 35, 35, 34, 35, 35, 35, 35, 35, 35, 35]
# project_dir = os.getcwd()
# font_dir = "C:/Windows/Fonts"


if __name__ == "__main__":
    fonts = Fonts(fonts_paths, fonts_sizes, fonts_maxcharsline)
    ffmpeg.create_videos(video_folder=video_folder, audio_folder=audio_folder, fonts=fonts, json_file=json_file,
                         fonts_dir=fonts_dir, output_folder=output_folder, text_source_font=text_source_font,
                         image_file=image_file, customer_name=customer_name, number_of_videos=number_of_videos)