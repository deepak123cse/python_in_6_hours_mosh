emojis_dict = {
    ":)" : "😁",
    ":(" : "😒",
    ":b" : "👍"
}
message_text = input("Input > ")
words_list = message_text.split(' ')
converted_text = ""
for word in words_list:
    if emojis_dict.get(word) is not None:
        converted_text += emojis_dict.get(word) + ' ' # you can use default option in get instead of if /else condition
    else:
        converted_text += word + ' '
print(converted_text)