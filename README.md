# thirdrock
# python 3.7

                   ########################################
####################              THIRD ROCK              #####################
                   ########################################

    # A 3D space exploration/asteroid avoidance game! Fly through an infinitely 
    # generating random asteroid field, and collect star particles as you pass by
    # them. Fun for all ages!
  
  ## Required Libraries
    # PyOpenGL
   # PyGame
  
  ## How to run:
      # (through vscode) install libraries
      # run command "python ui.py"
      # look at the pygame window that opens!
      
  ## User interaction
    # Users can interact with the game menu through keypresses (instructions
    #     in the menu)
    
    # Fly the ship using the 'w' 'a' 's' 'd' keys, where 
        > 'w' is up
        > 'a' is left
        > 's' is down
        > 'd' is right
        
    # take care to avoid asteroid collisions!
    
  ## File Organization
    # ui.py
      > where the OpenGL buffer is created, and most function to do with the game window
      > contains the 'main' function that runs the game
      > 
    # utilities.py
      > contains functions that are useful to other files, but don't fit into a category
      >   many of these are related to math calculations
    # shapes.py
      > contains all shape generating a drawing functions
      >   I got to learn a lot about this, there are many functions that aren't used 
      >   in the final game but were still beneficial to create!
    # AsteroidField.py
      > contains the AsteroidField class that maintains all information about the asteroid
      >   field generated during game play
      >   
    # Asteroid.py
      > contains the Asteroid class, which contains all information to maintain a single 
      >   asteroid
    # StarParticle.py
      > contains the StarParticle class, which contains all information to maintain a single
      >   star particle
    
  ## Notes
    # please see the actual code for detailed comments about how the program works.
    
    # Thank you to staff of CLPS 0950 for all the help with this and throughout the semester :)
    

  
  
