def get_text_from_json(class_key,text_key):
    import json
    import characthers

    with open('text_manager.json','r',encoding='utf-8') as file:
        text_data = json.load(file)
    char_name = characthers.main_characther.get_char_name()
    my_text = text_data[class_key][text_key].format(name=char_name)
    print(my_text)
    