




# استيراد مكتبة turtle التي توفر إمكانيات الرسومات والرسم في Python
# Import the turtle module, which provides graphics and drawing capabilities in Python
import turtle

# إنشاء كائن نافذة (شاشة) باستخدام turtle.Screen() لإعداد بيئة اللعبة
# Create a window (screen) object using turtle.Screen() to set up the game environment
wind = turtle.Screen()


# تعيين عنوان النافذة إلى "Ping Pong By Codezilla"
# Set the title of the window to "Ping Pong By Codezilla"
wind.title("Ping Pong By Codezilla")


# تعيين لون خلفية النافذة إلى الأسود
# Set the background color of the window to black
wind.bgcolor("black")


# إعداد أبعاد النافذة: العرض = 800 بكسل، الارتفاع = 600 بكسل
# Set up the dimensions of the window: width=800 pixels, height=600 pixels
wind.setup(width=800, height=600)


# تعطيل التحديثات التلقائية للشاشة (tracer(0) يعني أن التحديثات يجب أن تكون يدوية لأداء أفضل في الألعاب)
# Disable automatic screen updates (tracer(0) means updates must be manual for better performance in games)
wind.tracer(0)

# madrab1	
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.penup()
madrab1.goto(-350, 0)

# madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(350, 0)

# ball
madra2 = turtle.Turtle()
madra2.speed(0)
madra2.shape("square")
madra2.color("white")
madra2.penup()
madra2.goto(0, 0)


# بدء حلقة لا نهائية للحفاظ على تشغيل اللعبة وتحديث الشاشة
# Start an infinite loop to keep the game running and updating the screen
while True:
    # Manually update the screen to reflect any changes (since tracer is off)
    wind.update()
    
    

