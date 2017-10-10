# *  Credits:
# *
# *  v.1.0.0
# *  original RPi Sensor classes by pkscout

try:
    import random, time
    from sense_hat import SenseHat
except ImportError:
    pass



class SenseHatSensors:
    def __init__( self, testmode=False ):
        self.TESTMODE = testmode
        try:
            self.SENSE = SenseHat()
        except (OSError, NameError) as error:
            self.SENSE = None

    
    def Humidity( self ):
        if self.SENSE:
            for i in range( 0, 5 ):
                reading = self.SENSE.get_humidity()
                if reading:
                    return reading
        elif self.TESTMODE:        
            return random.randint( 43, 68 )
        return None

        
    def Temperature( self ):
        if self.SENSE:
            for i in range( 0, 5 ):
                reading = self.SENSE.get_temperature()
                if reading:
                    return reading
        elif self.TESTMODE:        
            return random.randint( 21, 28 )
        return None

        
    def Pressure( self ):
        if self.SENSE:
            for i in range( 0, 5 ):
                reading = self.SENSE.get_pressure()
                if reading:
                    return reading
        elif self.TESTMODE:        
            return random.randint( 990, 1020 )
        return None



class SenseHatLED:
    def __init__( self, low_light=True, rotate=False ):
        try:
            self.SENSE = SenseHat()
        except (OSError, NameError) as error:
            self.SENSE = None
        if self.SENSE:
            self.SENSE.low_light = low_light
            if rotate:
                self.SENSE.set_rotation( 180 )
        self.PALETTE = {'green':(0, 255, 0), 'yellow':(255, 255, 0), 'blue':(0, 0, 255),
                        'red':(255, 0, 0), 'white':(255,255,255), 'nothing':(0,0,0),
                        'pink':(255,105, 180)}
    
    
    def Blink( self, x, y, color=(255, 255, 255), pause=0.2, pivot=False ):
        if pivot:
            bx = y
            by = x
        else:
            bx = x
            by = y
        self.PixelOn( bx, by, color )
        time.sleep( pause )
        self.PixelOff( bx, by )


    def ClearPanel( self, color=None ):
        if self.SENSE:
            if color:
                self.SENSE.clear( color )
            else:
                self.SENSE.clear()


    def Color( self, color ):
        if isinstance( color, basestring ):
            return self.PALETTE[color.lower()]
        elif isinstance( color, tuple ):
            if len( color ) == 3:
               return color
        return (255, 255, 255)


    def PixelOff( self, x, y ):
        if self.SENSE:
            self.SENSE.set_pixel( x, y, 0, 0, 0 )
        
        
    def PixelOn( self, x, y, color=(255, 255, 255) ):
        if self.SENSE:
            self.SENSE.set_pixel( x, y, color )
        
        
    def Sweep( self, vertical=False, anchor=0, start=0, stop=7, color=(255, 255, 255), pause=0.1 ):
        if start < 0:
            start = 0
        if stop > 7:
            stop = 7
        current = start
        while current <= stop:
            self.Blink( current, anchor, color, pause, vertical )
            current = current + 1
        current = current - 2
        while current >= start:
            self.Blink( current, anchor, color, pause, vertical )
            current = current - 1
    
        
            
    
    
    