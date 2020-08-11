# import os
# os.system('youtube-dl -f bestvideo[height=480] -o argentina_vs_neigeeria.mp4 https://www.youtube.com/watch?v=RmlkAOwJ1gI ')
# os.system('youtube-dl -f bestaudio -o audio.mp3  https://youtube.com/watch?v=6BYIKEH0RCQ ')


# os.system('youtube-dl -f bestvideo[height=720] youtube.com/watch?v=6BYIKEH0RCQ')
# # # os.system('youtube-dl -x --audio-format mp3 https://www.youtube.com/watch?v=-52Ho9V1Nj8')

# # # from mhmovie.code import *
# # # m = movie("How to Install YouTube-DL.webm")
# # # mu = music('Post Malone   Rockstar ft  21 Savage Ilkay Sencan Remix.mp3')
# # # final = m+mu
# # # filename = "output.mp4"
# # # final.save(filename)

# # # import moviepy.editor as mpe
# # # my_clip = mpe.VideoFileClip('Real Madrid La Liga CHAMPIONS 2020-QFvCXCdP3TU.mp4')
# # # audio_background = mpe.AudioFileClip('Post Malone   Rockstar ft  21 Savage Ilkay Sencan Remix.mp3') 
# # # final_audio = mpe.CompositeAudioClip([my_clip.audio, audio_background])
# # # final_clip = my_clip.set_audio(final_audio)

# import os

# os.rename("Cr7.pm4","cr7.mp4")
# import subprocess
# p = subprocess.call('ffmpeg -i Cristiano Ronaldo Vs Cagliari 2020 Away HD 1080i-VR9NhnYR9Rc.mp4 -i PostMalone_Rockstar_21_Savage_Ilkay_Sencan_Remix.mp3 -c copy output4.mp4')

# # # # ffmpeg -i video.avi -i audio.mp3 -vcodec codec -acodec codec output_video.avi -newaudio


from selenium import webdriver
import time
import os
import subprocess
browser_one = webdriver.Chrome()
browser_two = webdriver.Chrome()
#for video
browser_one.get("https://www.youtube.com")
time.sleep(5)
vidname = input()
time.sleep(5)
search = browser_one.find_elements_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
search[0].send_keys(vidname)
# time.sleep(7)
browser_one.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button').click()
windowName = browser_one.current_url
# print(windowName)
vid1 = browser_one.find_elements_by_id('img')[0].click()
# print(browser.current_url)
vidlink = browser_one.current_url

#for audio
browser_two.get("https://www.youtube.com")
time.sleep(5)
audname = input()
time.sleep(5)
search = browser_two.find_elements_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
search[0].send_keys(audname)
# time.sleep(7)
browser_two.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button').click()
windowName = browser_two.current_url
# print(windowName)
vid1 = browser_two.find_elements_by_id('img')[0].click()
# print(browser.current_url)
audlink = browser_two.current_url

print(vidlink,audlink)
time.sleep(5)
os.system('youtube-dl -f bestvideo[height=720] -o video.mp4 {}'.format(vidlink))
os.system('youtube-dl -f bestaudio -o audio.mp3 {}'.format(audlink))


p = subprocess.call('ffmpeg -i video.mp4 -i audio.mp3 -c copy output2.mp4')


