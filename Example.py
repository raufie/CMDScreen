from CMDScreen import CMDScreen
import time
# the CMDScreen object is what you will use to control anything on your command prompt
screen = CMDScreen()
name_object = screen.register(
    "User Basic Information", "Name: Raufie 2.0\nAge: 31\nSpecies: UberNerd\n")
history_object = screen.register(
    "User History", "*Staying Single\n*Solving AGI\n*Playing Half Life after 30 years for the 10000th time\n")

screen.render()
# call the render method to render all the states
time_object = screen.register("Updating Information in...", "6")
for i in range(6):
    time.sleep(1)
    # You can use the set value method to change the string value of that object
    # SET VALUE AUTOMATICALLY UPDATES THE SCREEN
    time_object.set_value(str(6-i))


# These objects can also be deleted by calling the unregister function on them
# you can also call this function from screen...
time_object.unregister()
# this object is now deleted
# YOU STILL HAVE TO RENDER it though to see any changes
# This was done because many times you wanna unregister an object before you make changes...
screen.render()
