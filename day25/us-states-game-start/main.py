import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("US States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guess_list = []
while len(guess_list) < 50:
    answer_state = screen.textinput(title =  f"{len(guess_list)}/50 ,Guess the states", prompt = "Guess another states name.").title()

    data = pd.read_csv("50_states.csv")
    #if (data['state'] == answer_state).any(): both works
    
    if answer_state == "Exit":
        #remaining = []
        # for item in data['state'].tolist():  # data.state.tolist()
        #     if item not in guess_list:
        #         remaining.append(item)
        remaining = [item  for item in data["state"].tolist() if item not in guess_list ]

        new_data = pd.DataFrame(remaining,columns=["states"])
        new_data.to_csv("new_data.csv")
        break
    if answer_state in data['state'].values:
        print(answer_state)
        x_cord = int(data[data['state'] == answer_state]["x"])
        y_cord = int(data[data['state'] == answer_state]["y"])
        locater = turtle.Turtle()
        locater.hideturtle()
        locater.penup()
        locater.goto(x_cord, y_cord)
        locater.write(answer_state)
        guess_list.append(answer_state)
    




# def get_mouse_click_coor(x,y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

#turtle.mainloop()  # this keeps the screen open even the process is done.