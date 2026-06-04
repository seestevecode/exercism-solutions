module MariosMarvellousLasagna exposing (remainingTimeInMinutes)

remainingTimeInMinutes : Int -> Int -> Int
remainingTimeInMinutes numberOfLayers minutesInOven =
    let
        expectedMinutesInOven = 40
        preparationTimeInMinutes = numberOfLayers * 2
    in
    preparationTimeInMinutes + expectedMinutesInOven - minutesInOven
