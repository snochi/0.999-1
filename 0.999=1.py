from manimlib import *
from random import randint


class Intro(Scene):

    def construct(self):
        integers = Tex(r"\ldots",",","-2",",", "-1", ",", "0", ",", "1", ",", "2", ",", r"\ldots")

        triangle = Triangle().scale(0.1).next_to(integers[2],DOWN)

        t1 = Triangle().scale(0.1).next_to(integers[4],DOWN)
        t2 = Triangle().scale(0.1).next_to(integers[6],DOWN)
        t3 = Triangle().scale(0.1).next_to(integers[8],DOWN)
        t4 = Triangle().scale(0.1).next_to(integers[10],DOWN)

        letter = TexText("'negative two'").scale(0.7).next_to(triangle,DOWN)

        none = TexText("'negative one'").scale(0.7).next_to(t1,DOWN)
        zero = TexText("'zero'").scale(0.7).next_to(t2,DOWN)
        one = TexText("'one'").scale(0.7).next_to(t3,DOWN)
        two = TexText("'two'").scale(0.7).next_to(t4,DOWN)

        pi = Tex(r"\frac{355}{113} = ",r"3.",r"141592\ldots")
        e = Tex(r"e = ", r"2.7182818\ldots").shift(-UP/2)

        group = VGroup(pi,e)
        brace = Brace(group,direction=RIGHT)
        label = TexText("unique!").scale(0.7).next_to(brace,RIGHT)

        oneVSzpn = Tex(r"1",r"=",r"0.999\ldots")

        triangle2 = Triangle().rotate(PI).scale(0.1).next_to(oneVSzpn[1],UP)
        questionmark = TexText("?").scale(0.7).next_to(triangle2,UP)

        self.wait(1)

        self.play(Write(integers[8:]))
        self.play(Write(integers[:8]))

        self.play(ShowCreation(triangle), Write(letter))
        self.play(triangle.animate.next_to(integers[4],DOWN),Transform(letter,none),run_time=1)
        self.play(triangle.animate.next_to(integers[6],DOWN),Transform(letter,zero),run_time=1)
        self.play(triangle.animate.next_to(integers[8],DOWN),Transform(letter,one),run_time=1)
        self.play(triangle.animate.next_to(integers[10],DOWN),Transform(letter,two),run_time=1)

        self.play(FadeOut(triangle), FadeOut(letter), FadeOut(integers), Write(pi[1:]))

        self.play(pi[2].animate.shift(UP/4),run_time=1)
        self.play(pi[2].animate.shift(-UP/4),run_time=1)

        self.play(Write(pi[0]))
        self.play(pi.animate.shift(UP/2),run_time=0.5)
        self.play(Write(e))

        self.play(ShowCreation(brace))

        self.wait(1)

        self.play(Write(label))

        self.wait(1)

        self.play(FadeOut(group),FadeOut(brace),FadeOut(label))

        self.wait(1.5)

        self.play(Write(oneVSzpn[0]),run_time=0.5)

        self.wait(1.5)

        self.play(Write(oneVSzpn[1:]))

        self.wait(6.5)

        self.play(ShowCreation(triangle2),Write(questionmark))

        self.play(FadeOut(oneVSzpn),FadeOut(triangle2),FadeOut(questionmark),run_time=3)


class Body(Scene):

    def construct(self):
        nl = NumberLine()
        nl2 = NumberLine(x_range=[0,1,1],unit_size=10,include_numbers=True,numbers_to_exclude=[])
        nl3 = NumberLine(x_range=[0,1,1],unit_size=10)

        triangle = Triangle().scale(0.1).next_to(nl2,UP/4).rotate(PI)
        onehalf = Tex(r"\frac{1}{2}").scale(0.7).next_to(triangle,UP)

        p = Tex("p").move_to(nl2.numbers.submobjects[0])
        q = Tex("q").move_to(nl2.numbers.submobjects[1])
        centerofpq = (p.get_center()+q.get_center())/2

        middlepoint = Tex(r"\frac{p+q}{2}").scale(0.7).next_to(triangle,UP)

        no_mp = TexText(r"no middle point!").scale(0.7).next_to(triangle,UP)
        peqq = Tex(r"p=q").scale(0.7)

        characterization = TexText(r"$p\neq q$"
                , r"\\$\Leftrightarrow$"
                , r"\\There is no number between $p,q$, exclusive.")

        zpneqone = Tex(r"0.999\ldots","=","1")
        neq = Tex(r"\neq").move_to(zpneqone[1])
        strict = Tex(r"<").move_to(zpneqone[1])

        inequalities = Tex(r"0",".999\ldots",r"<",r"?",r".???\ldots",r"<",r"1")

        brace = Brace(inequalities[3:5])
        label = Tex(r"=x").scale(0.7).next_to(brace,DOWN)

        zero = Tex(r"0").move_to(inequalities[3])
        one = Tex(r"1").move_to(inequalities[3])

        ineq1 = Tex(r"1",r".",r"?",r"?",r"?",r"\ldots",r"\geq",r"1").next_to(inequalities[5],UP)

        brace2 = Brace(ineq1[:5],direction=UP)
        label2 = Tex(r"=x").scale(0.7).next_to(brace2,UP)

        group1 = VGroup(ineq1, brace2, label2)

        ineq2 = Tex(r"0",r".",r"?",r"?",r"?",r"\ldots",r"\leq",r"0.999\ldots").next_to(inequalities[2],UP)

        brace3 = Brace(ineq2[:5],direction=UP)
        label3 = Tex(r"=x").scale(0.7).next_to(brace3,UP)

        group2 = VGroup(ineq2, brace3, label3)

        self.wait(1)

        self.play(ShowCreation(nl))

        self.wait(5)

        self.play(ReplacementTransform(nl,nl2))

        self.wait(8)

        self.play(ShowCreation(triangle),Write(onehalf))

        self.wait(3)

        self.play(ReplacementTransform(nl2,nl3),Write(p),Write(q),FadeOut(triangle),FadeOut(onehalf))

        self.wait(1)

        self.play(ShowCreation(triangle),Write(middlepoint))

        self.wait(7)

        self.play(p.animate.move_to(centerofpq),q.animate.move_to(centerofpq),ReplacementTransform(nl3,peqq),ReplacementTransform(middlepoint,no_mp))
        self.play(FadeOut(p),FadeOut(q),run_time=0.1)

        self.wait(3)
        
        self.play(FadeOut(no_mp),FadeOut(triangle),FadeOut(peqq))

        self.wait(1)

        self.play(Write(characterization[0]))
        self.play(Write(characterization[1]))

        self.wait(1)

        self.play(Write(characterization[2]))

        self.wait(2)

        self.play(ReplacementTransform(characterization,zpneqone))

        self.wait(6.5)

        self.play(ReplacementTransform(zpneqone[1],neq),run_time=0.5)

        triangle.next_to(neq,UP)
        
        ftsc = TexText(r"for contradiction").next_to(triangle,UP)

        contradiction = TexText(r"contradiction!").scale(0.7)

        leads2cont = TexText(r"This leads to a contradiction.").scale(0.7)

        zpnneqone = Tex(r"0.999\ldots",r"<",r"1")
        nneq = Tex(r"\neq").move_to(zpnneqone[1])
        eq = Tex(r"=").move_to(zpnneqone[1])

        self.wait(1)

        self.play(ShowCreation(triangle),Write(ftsc))

        self.wait(2)

        self.play(FadeOut(triangle),FadeOut(ftsc))

        self.wait(1)

        self.play(ReplacementTransform(neq,strict))

        self.wait(3)

        self.play(FadeOut(strict),ReplacementTransform(zpneqone,inequalities))

        self.wait(0.5)

        self.play(ShowCreation(brace),Write(label))

        self.wait(8.5)

        self.play(inequalities[3].animate.shift(UP/2))

        self.wait(1)

        self.play(inequalities[-1].animate.shift(UP/2))
        self.play(inequalities[0].animate.shift(UP/2))
        self.play(inequalities[3].animate.shift(-UP/2),inequalities[-1].animate.shift(-UP/2),inequalities[0].animate.shift(-UP/2))

        self.wait(3)

        self.play(Transform(inequalities[3],one),run_time=0.5)
        self.play(Transform(inequalities[3],zero),run_time=0.5)

        self.wait(2.5)

        self.play(Transform(inequalities[3],one),run_time=0.5)

        self.wait(1.5)

        self.play(Write(ineq1),ShowCreation(brace2),Write(label2))
        for i in range(100):
            d1 = Tex(str(randint(0,9))).move_to(ineq1[2])
            d2 = Tex(str(randint(0,9))).move_to(ineq1[3])
            d3 = Tex(str(randint(0,9))).move_to(ineq1[4])
            self.play(Transform(ineq1[2],d1),Transform(ineq1[3],d2),Transform(ineq1[4],d3),run_time=0.1)

        triangle.next_to(inequalities[5],UP)
        contradiction.next_to(triangle,RIGHT)
        self.play(ShowCreation(triangle),group1.animate.next_to(triangle,UP),Write(contradiction))

        self.wait(4)

        self.play(FadeOut(group1),FadeOut(triangle),FadeOut(contradiction))

        self.wait(1)

        self.play(Transform(inequalities[3],zero),run_time=0.5)

        self.wait(1)

        self.play(Write(ineq2),ShowCreation(brace3),Write(label3))
        for i in range(150):
            d1 = Tex(str(randint(0,9))).move_to(ineq2[2])
            d2 = Tex(str(randint(0,9))).move_to(ineq2[3])
            d3 = Tex(str(randint(0,9))).move_to(ineq2[4])
            self.play(Transform(ineq2[2],d1),Transform(ineq2[3],d2),Transform(ineq2[4],d3),run_time=0.1)

        triangle.next_to(inequalities[2],UP)
        contradiction.next_to(triangle,LEFT)
        self.play(ShowCreation(triangle),group2.animate.next_to(triangle,UP),Write(contradiction))

        self.wait(4)

        self.play(FadeOut(group2),FadeOut(contradiction),FadeOut(brace),FadeOut(label),triangle.animate.next_to(inequalities,UP))

        leads2cont.next_to(triangle,UP)

        self.play(Write(leads2cont))
        self.play(ReplacementTransform(inequalities,zpnneqone))

        self.wait(1)

        self.play(Transform(zpnneqone[1],nneq))
    
        self.wait(2)

        self.play(Transform(zpnneqone[1],eq),FadeOut(leads2cont),FadeOut(triangle))

        self.wait(1)

        self.play(FadeOut(eq),run_time=3)
