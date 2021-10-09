from manim import *

class av(ThreeDScene):
    def construct(self):
        #متغیر های حرکت دهنده مثلث متحرک
        #متغیر ارتفاع از کف
        h=ValueTracker(0)
        #متغیر حرکت روی محور x ها
        x=ValueTracker(0)
        #طراحی ۴ ضلع ثابت
        z1=Line(start=[-2,1.5,0],end=[3,1.5,0])
        z2=Line(start=[3,1.5,0],end=[2,-1.5,0])
        z3=Line(start=[2,-1.5,0],end=[-2,-1.5,0])
        z4=DashedLine(start=[-2,-1.5,0],end=[-2,1.5,0])
        #طراحی نوشته h
        t_h= always_redraw(lambda : 
        Text("h").next_to(z4,RIGHT).shift([x.get_value(),0,h.get_value()])
        )
        #طراحی مثلث متحرک
        mosalas = always_redraw(lambda :
        Polygon([-2+x.get_value(),-1.5,h.get_value()],
                [-2+x.get_value(),1.5,h.get_value()],
                [-3+x.get_value(),-1.5,h.get_value()],
                color="#FFFFFF")
        )

        #کشیدن تصویر
        self.play(Write(z1),
                  Write(z2),
                  Write(z3),
                  Write(z4),
                  Write(t_h),
                  Write(mosalas),
                  run_time=1.5)
        #مکث
        self.wait()
        #حرکت دادن مثلث به اون سمت دیگه فقط روی محور ایکس‌ها
        self.play(x.animate.set_value(5),run_time=2)

        #چرخش پر سرعت با دوران بالای دوربین
        #زاویه سه رخ دادن به کار
        #برگردوندن مثل به نقطه اول
        self.move_camera(phi=(30+360) * DEGREES, theta=-(120+720) * DEGREES ,
                         added_anims=[x.animate.set_value(0),
                           ],
                           run_time=1.5)
        #مکث
        self.wait(1.5)

        #برش مثلث از کف
        self.play(h.animate.set_value(2))
        #مکث
        self.wait()
        #حرکت دادن مثلث به اون سمت دیگه
        self.play(x.animate.set_value(5))
        #مکث
        self.wait()
        #پایین بردن مثلث
        self.play(h.animate.set_value(0))
        #مکث
        self.wait()
