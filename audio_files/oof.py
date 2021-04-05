from gtts import gTTS

# gTTS was clipping out the fist word, so a "Hi' is inserted
# This script is only to generate clear audio files before runs
# Please check their legibility before run

greet = gTTS("Hi, Welcome to our restaurant. We are pleased to have you here today. What would you like to order ?", lang="hi", tld="co.in")
greet.save("greet.mp3")

ordered = gTTS("Hi, anything else ?", lang="hi", tld="co.in")
ordered.save("anything_else.mp3")

ask_add = gTTS("Hi, And what may be your delivery address ?", lang="hi", tld="co.in")
ask_add.save("ask_add.mp3")

ordered = gTTS("Hi, Noted", lang="hi", tld="co.in")
ordered.save("ordered.mp3")

