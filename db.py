import sqlite3

try:
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()

    intent_query = 'SELECT * FROM intent'
    cursor.execute(intent_query)
    all_intents = cursor.fetchall()

    action_query = 'SELECT * FROM action'
    cursor.execute(action_query)
    all_actions = cursor.fetchall()

    query_button = 'SELECT * FROM image img inner join action a on a.ac_id = img.ac_id'
    cursor.execute(query_button)
    all_images = cursor.fetchall()

    query_button = 'SELECT * FROM video v inner join action a on a.ac_id = v.ac_id'
    cursor.execute(query_button)
    all_videos = cursor.fetchall()

    query_button = 'SELECT * FROM button b inner join action a on a.ac_id = b.ac_id'
    cursor.execute(query_button)
    all_button = cursor.fetchall()



    with open ('domain.yml', 'w') as f:
        header = 'version: "3.0"\n\nintents:\n'
        f.write(header)
        for intents in all_intents:
            data = ['  - ', intents[1] , '\n']
            f.writelines(data)

        body = '\nresponses:\n'
        f.write(body)
        for actions in all_actions:
            if(actions[2] != ''):
                action_data = ['  ', actions[1] , ':\n  - text: "',actions[2],'"\n']
                f.writelines(action_data)
            if(actions[3] == 'image'):
                for images in all_images:
                    if(actions[0] == images[2]):
                        add_img = ['    image: "', images[1] , '"\n']
                        f.writelines(add_img)
            elif(actions[3] == 'video'):
                for videos in all_videos:
                    if(actions[0] == videos[3]):
                        add_video = ['    attachment: { "type":"video","payload":{ "src": "',videos[2], '" } }\n']
                        f.writelines(add_video)
            elif(actions[3] == 'button'):
                btn = ['    buttons:\n']
                f.writelines(btn)
                for buttons in all_button:
                    if(buttons[4] == actions[0]):
                        add_button = ['    - title: "', buttons[1] , '"\n      payload: "/', buttons[2], '"\n']
                        f.writelines(add_button)

        footer = ['\nsession_config:\n  session_expiration_time: 60\n  carry_over_slots_to_new_session: true']
        f.writelines(footer)
    f.close()


    #Story.yml file

    query_story = 'SELECT * FROM story'
    cursor.execute(query_story)
    all_story = cursor.fetchall()

    query_story = 'SELECT * FROM intent'
    cursor.execute(query_story)
    result_intent = cursor.fetchall()
    
    query = 'SELECT * FROM intent_action ia INNER JOIN intent i ON ia.int_id = i.int_id INNER JOIN action a ON ia.ac_id = a.ac_id'
    cursor.execute(query)
    result_int_action = cursor.fetchall()
    # field_names = [val[0] for val in cursor.description]
    # print(field_names)
    # for rows in result_int_action:
    #     print(rows)
        







    with open ('./data/stories.yml', 'w') as s:
        header = 'version: "3.0" \n\nstories:\n\n'
        s.write(header)
        for stories in all_story:
            data = ['- story: ', stories[1], '\n  steps:\n']
            s.writelines(data)
            for intents in result_intent:
                if(intents[2] == stories[0] ):
                    data = ['  - intent: ', intents[1] , '\n']
                    s.writelines(data)
                    for int_action in result_int_action:
                        if(int_action[2] == intents[0]):
                            data = ['  - action: ', int_action[6], '\n']
                            s.writelines(data)
    s.close()


    cursor.close()
except sqlite3.Error as error:
    print('Error occured - ', error)

finally:
    if conn:
        conn.close()
        print("Database connection closed")