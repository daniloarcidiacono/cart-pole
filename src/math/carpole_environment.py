import math

# State of a cart pole environment
class CartPoleEnvironment:
    def __init__(self, g = 9.81, F = 0, mp = 0.1, mc = 1, l = 0.5, muc = 0.0005, mup = 0.000002):
        # Physics engine
        self._equations = None
        self._integrator = None

        # Physical properties
        self._g = g
        self._F = F
        self._mc = mc
        self._mp = mp
        self._l = l
        self._muc = muc
        self._mup = mup

        # Constraints
        self._leftBound = -2.4
        self._rightBound = 2.4
        self._angleTolerance = math.radians(12)

        # Starting conditions
        self._startPosition = 0
        self._startVelocity = 0
        self._startAngle = math.radians(1)
        self._startAngleVelocity = 0

        # Actual status
        self._time = 0
        self._position = self._startPosition
        self._velocity = self._startVelocity
        self._angle = self._startAngle
        self._angleVelocity = self._startAngleVelocity

    # Resets the state to the starting conditions
    def reset(self):
        self._time = 0
        self._position = self._startPosition
        self._velocity = self._startVelocity
        self._angle = self._startAngle
        self._angleVelocity = self._startAngleVelocity

    # Returns TRUE if the constraints are violated
    def constraintsViolated(self):
        return self._position < self._leftBound or self._position > self._rightBound or self._angle < -self._angleTolerance or self._angle > self._angleTolerance

    # Steps the system
    def step(self, h):
        # Update the equations
        self._equations._g = self._g
        self._equations._mc = self._mc
        self._equations._mp = self._mp
        self._equations._l = self._l
        self._equations._muc = self._muc
        self._equations._mup = self._mup
        self._equations._F = self._F

        # Simulate
        [self._time,
         self._position,
         self._angle,
         self._velocity,
         self._angleVelocity] = self._integrator.integrate(
            self._equations,
            self._time,
            self._position,
            self._angle,
            self._velocity,
            self._angleVelocity,
            h
        )

        # # [0; 2pi)
        # self._angle %= 2 * math.pi
        #
        # # [-pi; pi]
        # if self._angle > math.pi:
        #     self._angle -= math.pi
        # elif self._angle < -math.pi:
        #     self._angle += math.pi

    def fromJson(self, json):
        self._g = json["parameters"]["gravity"]
        self._mc = json["parameters"]["cartMass"]
        self._mp = json["parameters"]["poleMass"]
        self._l = json["parameters"]["poleLength"]
        self._muc = json["parameters"]["cartFriction"]
        self._mup = json["parameters"]["poleFriction"]

        self._leftBound = json["constraints"]["leftBound"]
        self._rightBound = json["constraints"]["rightBound"]
        self._angleTolerance = math.radians(json["constraints"]["angleTolerance"])

        self._startPosition = json["startState"]["position"]
        self._startVelocity = json["startState"]["velocity"]
        self._startAngle = math.radians(json["startState"]["angle"])
        self._startAngleVelocity = math.radians(json["startState"]["angleVelocity"])

        self._time = json["state"]["position"]
        self._position = json["state"]["velocity"]
        self._velocity = json["state"]["velocity"]
        self._angle = math.radians(json["state"]["angle"])
        self._angleVelocity = math.radians(json["state"]["angleVelocity"])

    def toJson(self):
        return {
            'parameters': {
                'gravity': self._g,
                'cartMass': self._mc,
                'poleMass': self._mp,
                'poleLength': self._l,
                'cartFriction': self._muc,
                'poleFriction': self._mup
            },

            'constraints': {
                'leftBound': self._leftBound,
                'rightBound': self._rightBound,
                'angleTolerance': math.degrees(self._angleTolerance)
            },

            'startState': {
                'position': self._startPosition,
                'velocity': self._startVelocity,
                'angle': math.degrees(self._startAngle),
                'angleVelocity': math.degrees(self._startAngleVelocity)
            },

            'state': {
                'time': self._time,
                'position': self._position,
                'velocity': self._velocity,
                'angle': math.degrees(self._angle),
                'angleVelocity': math.degrees(self._angleVelocity)
            }
        }