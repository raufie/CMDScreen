# CMDState
I know what you're thinking.. why the heck do we even need it???
It's just a fun little project that I know i'll be needing, 
## Why?
I have need for this kinda stuff, idk if its there online...
this is one of those projects where its too easy to make it yourself that you'd rather build it than search it

## A lifelong abstraction
Idk why we even do it, for every cmd project i find it time wasting to write a lot of this stuff from scratch, and im pretty sure there is something out there, but a very high level abstraction with customizability is the goal here... ... how to use it? well its super easy that's why its a high level abstraction for cmd prints (even tho print itself is a pretty darn high level abstraction lol)


# CMDScreen Objects
Create a single one of these objects and update everything on your screen with this
```
screen = CMDScreen()
```
# ScreenStates
CMDScreen holds different kinds of states for you, that was the whole point, 
imagine you want to change some parts of the view but not others.. ik its simple to implement but here u get it anyway
```
name_object = screen.register_state("name","Bruh")
//register_state takes name and value... both strings... both are displayed... 
```
# Render
This is vip, call this to render all the states
```
screen.render()
//optionally pass clear_screen=False to not clear screen (but why? unless ur building a chat app or something else where history is needed)
```

## ScreenState.set_name, set_value
You can change the values of these states by calling these methods on state objects, the cmd is automatically re rendered
```
name_object.set_value("brutha")
```

## ScreenState.unregister
Unregister a state object by calling it
```
name_object.unregister()
```
You have to call render after this to see the changes

All the values are rendered line by line ... CMDScreen holds a list of state objects and loops over them printing them one by one with their name and value

#### Now what? oh its so basic? Nothing... 
No one cares about command prompt... we can make it as good looking as we want but we are writing it for other programmers not users... so yeah.. its not react....