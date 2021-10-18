I have 3 model robots running at different dts 1 s 0.1 s and 0.01 s
there are a few gutchecks along in the code to make sure the math is aligning as expected
graphs plotting where the robot is visiting per time step is commented out but may be seen if uncommented

basically this is a two part question
1. Find the theoretical perfect ending position of the robot using the radius of the turning angle
2. plot the respective locations that the robot visits and use the last location visited to see how close to the
   perfect location each robot reaches. (in plotting where the robot goes use the discretized equations of motion)