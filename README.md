# Bowling kata


![Let's play bowling](https://s-media-cache-ak0.pinimg.com/236x/00/f0/57/00f057f62b49076c34d9646a9c09f08a.jpg)

In this kata, you'll developp a java library that will allow to count the points of a bowling game. You'll have to implement the tests and then code the library so that it fullfills the tests.

### Bowling rules

The bowling is a game in which a player has to hit some pins places a then end of a lane with the help of a bowl. A game is composed of ten "frames". In each frame, the player has two rolls to knock down 10 pins. The score of a frame is the total number of pins knock down plus bonus for spares and strikes.

The spare : when the player knocks down all 10 pins in two tries. In that case, there is a bonus which value is the number of pins that are knocked down in then next roll.

The strike : when the player knocks down all 10 pins in one try. In that case, there is a bonus which value is the number of pins that are knocked down in then next two rolls.

In the last frame, if a strike or a spare is shot, then the player is allowed to roll one or two additional balls to complete the frame. So there can't be more than three rolls in the last frame.

Consequently, in the case of a perfect game where the player would roll 12 strikes, then the score should be 300.

In the following schema, you'll see the count for a sample bowling game.

<img alt="Sample bowling game " src="https://raw.githubusercontent.com/dmetzler/exam-jee-2015/master/images/samplegame.png" width="800px"/>


This coding kata will be done in 6 parts:
 * The First Test
 * The Second Test
 * The Third Test
 * The Fourth Test
 * The Fifth Test
 * The Sixth Test
