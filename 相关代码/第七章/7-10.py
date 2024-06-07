name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "
# 调查结果将存储在形如{name: place}的字典中。
responses = {}
while True: # 询问用户想去哪里度假。
 name = input(name_prompt)
 place = input(place_prompt)
 # 存储调查结果。
 responses[name] = place
# 询问是否还有其他人要参与调查。
 repeat = input(continue_prompt)
 if repeat != 'yes':
     break  # 显示调查结果。
 print("\n--- Results ---")
 for name, place in responses.items():
     print(f"{name.title()} would like to visit {place.title()}.")