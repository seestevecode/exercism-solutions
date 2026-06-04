module LuciansLusciousLasagna exposing (elapsedTimeInMinutes, expectedMinutesInOven, preparationTimeInMinutes)


expectedMinutesInOven = 
    40


preparationTimeInMinutes numberOfLayers = 
    numberOfLayers * 2


elapsedTimeInMinutes numberOfLayers totalMinutesInOven =
    preparationTimeInMinutes numberOfLayers + totalMinutesInOven
