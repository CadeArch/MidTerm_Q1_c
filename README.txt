I have 3 model robots running at different dts 1 s 0.1 s and 0.01 s
there are a few gutchecks along in the code to make sure the math is aligning as expected
graphs plotting where the robot is visiting per time step is commented out but may be seen if uncommented

basically this is a two part question
1. Find the theoretical perfect ending position of the robot using the radius of the turning angle
2. plot the respective locations that the robot visits and use the last location visited to see how close to the
   perfect location each robot reaches. (in plotting where the robot goes use the discretized equations of motion)


# output when run

radius:  6.92820323027551
path Circumfrence:  43.53118474162123
time for one revolution:  2.1765592370810616
total revolutions 4.594407461848267
distance for one revolution:  43.53118474162123
total Distance traveled:  200.0
total Distance traveled:  200.0
end distance into 5th revolution (arc length)  25.87526103351507
theta of end position 213.98668626537602
theoretical end position ( -5.744640875665662, -3.8728673111315417)

dt = 1
total points on graph:  11
last point position 1 dt (10.174772088209632, -19.007836733560396)
theoretical end position (-5.744640875665662, -3.8728673111315417)

dt = 0.1
total points on graph:  101
last point position 0.1 dt (-5.097512294274187, -5.675102459925033)
theoretical end position (-5.744640875665662, -3.8728673111315417)

dt - 0.01
total points on graph:  1001
last point position 0.01 dt (-5.687860780209038, -4.05551510717557)
theoretical end position (-5.744640875665662, -3.8728673111315417)

