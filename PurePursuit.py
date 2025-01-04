# PurePursuit.py

import math

# Global Variables
path = []  # List of [x, y] points defining the path
followerPath = []  # List of [x, y] points traversed by the follower
follower = None  # PathFollower object
followerSpeed = 2.5  # Speed of the follower
followerStopDistance = 2  # Distance at which the follower stops
lookaheadDistanceDelta = 2.5  # Increment for lookahead distance adjustments
pointSize = 8  # Size of the path and follower points
lookaheadDistance = 45  # Initial lookahead distance
pursuedCircleColor = [255, 0, 0]  # RGB color for the pursued point

def setup():
    """Initial setup for the simulation."""
    size(800, 400)
    reset()
    smooth()
    strokeWeight(2)

def reset():
    """Resets the simulation by clearing paths and the follower."""
    global path, follower, followerPath
    path = []
    follower = None
    followerPath = []

def draw():
    """Main draw loop to render the simulation."""
    background(255)  # White background

    # Draw the follower's path
    if followerPath:
        stroke(120)  # Gray color for follower path
        noFill()
        for i in range(0, len(followerPath) - 1, 4):
            p1 = followerPath[i]
            p2 = followerPath[i + 1]
            line(p1[0], p1[1], p2[0], p2[1])

    # Draw the main path
    stroke(0)  # Black color for path
    fill(0)
    for i, point in enumerate(path):
        ellipse(point[0], point[1], pointSize, pointSize)
        if i > 0:
            previousPoint = path[i - 1]
            line(point[0], point[1], previousPoint[0], previousPoint[1])

    # If left mouse is pressed, show the lookahead line from the cursor
    if mousePressed and mouseButton == LEFT:
        x = mouseX
        y = mouseY
        lookaheadPoint = getLookaheadPoint(x, y, lookaheadDistance)
        if lookaheadPoint is not None:
            drawLookaheadPoint(x, y, lookaheadPoint[0], lookaheadPoint[1])

    # Draw and potentially move the PathFollower
    global follower
    if follower is not None:
        position = follower.getFollowerPosition()
        lookaheadPoint = getLookaheadPoint(position[0], position[1], lookaheadDistance)

        # Draw the follower
        fill(0)  # Black color for follower
        noStroke()
        ellipse(position[0], position[1], pointSize, pointSize)

        if lookaheadPoint is not None:
            drawLookaheadPoint(position[0], position[1], lookaheadPoint[0], lookaheadPoint[1])

            # Calculate the distance to the lookahead point
            deltaX = lookaheadPoint[0] - position[0]
            deltaY = lookaheadPoint[1] - position[1]
            distance = 2 * math.sqrt(deltaX ** 2 + deltaY ** 2)

            # Draw the circle around the follower
            noFill()
            stroke(0, 150)  # Semi-transparent black
            ellipse(position[0], position[1], distance, distance)

            # Check if the follower has reached the destination
            if distance < followerStopDistance:
                follower = None
            else:
                # Move the follower upon pressing 'f'
                if keyPressed and key == 'f':
                    followerPath.append([follower.position[0], follower.position[1]])
                    follower.moveFollowerTowardsPoint(lookaheadPoint[0], lookaheadPoint[1])

def signum(n):
    """
    Returns the sign of the input number n.
    Returns 1 for n = 0 to satisfy line-circle intersection requirements.
    """
    if n == 0:
        return 1
    else:
        return math.copysign(1, n)

def getLookaheadPoint(x, y, r):
    """
    Generate the furthest lookahead point on the path that is distance r from the point (x, y).
    """
    lookahead = None

    for i in range(len(path) - 1):
        segmentStart = path[i]
        segmentEnd = path[i + 1]

        # Translate the segment to the origin
        p1 = [segmentStart[0] - x, segmentStart[1] - y]
        p2 = [segmentEnd[0] - x, segmentEnd[1] - y]

        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        d = math.sqrt(dx ** 2 + dy ** 2)
        if d == 0:
            continue
        D = p1[0] * p2[1] - p2[0] * p1[1]

        discriminant = r * r * d * d - D * D
        if discriminant < 0 or (p1[0] == p2[0] and p1[1] == p2[1]):
            continue

        sqrt_discriminant = math.sqrt(discriminant)
        x1 = (D * dy + signum(dy) * dx * sqrt_discriminant) / (d * d)
        x2 = (D * dy - signum(dy) * dx * sqrt_discriminant) / (d * d)
        y1 = (-D * dx + abs(dy) * sqrt_discriminant) / (d * d)
        y2 = (-D * dx - abs(dy) * sqrt_discriminant) / (d * d)

        # Check if the intersections are within the segment
        validIntersection1 = (min(p1[0], p2[0]) < x1 < max(p1[0], p2[0])) or (min(p1[1], p2[1]) < y1 < max(p1[1], p2[1]))
        validIntersection2 = (min(p1[0], p2[0]) < x2 < max(p1[0], p2[0])) or (min(p1[1], p2[1]) < y2 < max(p1[1], p2[1]))

        if validIntersection1 or validIntersection2:
            lookahead = None  # Reset lookahead if any valid intersection exists

        if validIntersection1:
            lookahead = [x1 + x, y1 + y]

        if validIntersection2:
            if (lookahead is None or
                abs(x1 - p2[0]) > abs(x2 - p2[0]) or
                abs(y1 - p2[1]) > abs(y2 - p2[1])):
                lookahead = [x2 + x, y2 + y]

    # Special case for the very last point on the path
    if path:
        lastPoint = path[-1]
        endX, endY = lastPoint[0], lastPoint[1]
        dist_to_end = math.sqrt((endX - x) ** 2 + (endY - y) ** 2)
        if dist_to_end <= r:
            return [endX, endY]

    return lookahead

def drawLookaheadPoint(x1, y1, x2, y2):
    """
    Draws a lookahead point and the line connecting it to the follower.
    """
    stroke(0)  # Black color for lines
    line(x1, y1, x2, y2)
    fill(pursuedCircleColor[0], pursuedCircleColor[1], pursuedCircleColor[2])  # Color for lookahead point
    noStroke()
    ellipse(x2, y2, pointSize, pointSize)

def keyPressed():
    """Handles key press events for controlling the simulation."""
    global lookaheadDistance, follower, followerPath
    if key == 'r':
        reset()
    elif key == 'n':
        if path:
            firstPoint = path[0]
            followerPath = []
            follower = PathFollower(firstPoint[0], firstPoint[1], followerSpeed)
    elif key == '+':
        lookaheadDistance += lookaheadDistanceDelta
    elif key == '-':
        lookaheadDistance = max(lookaheadDistanceDelta, lookaheadDistance - lookaheadDistanceDelta)  # Prevent negative lookahead

def mousePressedEvent():
    """Handles mouse press events for adding points to the path."""
    global path
    if mouseButton == RIGHT:
        path.append([mouseX, mouseY])

# Assign mousePressedEvent to the mousePressed function in Processing
mousePressed = mousePressedEvent

class PathFollower:
    """Class representing the follower that pursues the path."""
    def __init__(self, x, y, speed):
        self.position = [x, y]
        self.speed = speed

    def moveFollowerTowardsPoint(self, x, y):
        """Moves the follower towards a specified point by its speed."""
        offsetX = x - self.position[0]
        offsetY = y - self.position[1]
        distanceToPoint = math.sqrt(offsetX ** 2 + offsetY ** 2)
        if distanceToPoint == 0:
            return
        normalizedX = offsetX / distanceToPoint
        normalizedY = offsetY / distanceToPoint
        self.position[0] += normalizedX * self.speed
        self.position[1] += normalizedY * self.speed

    def getFollowerPosition(self):
        """Returns the current position of the follower."""
        return self.position
