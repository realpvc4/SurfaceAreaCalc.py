import math

#modules left: ,,,,,

def main():
    choice = input("Choices:\n[sphere, cube, cone, sqaure-based pyramid (sbp) , triangular prism (tp), cylinder]\nEnter the figure of which you would like to find the surface area of: ")
    
    if choice == "sphere":
        #SA Sphere = 4πr²
        def surface_area_sphere(sphereRadius):
            return (4 * piValueSphere * pow(sphereRadius,2))
            
        piValueSphere = float(input("Let pi 'π' equal: "))
        sphereRadius = float(input("Let radius 'r' equal: "))
        sphereSA = surface_area_sphere(sphereRadius)
        print("The surface area of the sphere is:", sphereSA,"units²")
        return main()

    elif choice == "cube":
        #SA of Cube = 6(EdgeLength²)
        def surface_area_cube(SideLengthCube):
            return (6*(pow(SideLengthCube,2)))
        
        SideLengthCube = float(input("Let side length 'a' equal: "))
        cubeSA = surface_area_cube(SideLengthCube)
        print("The surface area of the cube is:", cubeSA,"units²")
        return main()

    elif choice == "cone":
        #SA Sphere = πr(r+ sqrt(h²+r²))
        def surface_area_cone(coneRadius, coneHeight):
            return (piValueCone * coneRadius)*(coneRadius+(math.sqrt(pow(coneRadius,2)+pow(coneHeight,2))))

        piValueCone = float(input("Let pi 'π' equal: "))
        coneRadius = float(input("Let radius 'r' equal: "))
        coneHeight = float(input("Let height 'h' equal: "))
        coneSA = surface_area_cone(coneRadius, coneHeight)
        print("The surface area of the cone is:", coneSA,"units²")
        return main()
    
    elif choice == "sbp":
        #SAsbp = a²+2a(sqrt((a²/4)+(h²)))
        def surface_area_cone(SideLengthsbp,sbpHeight):
            print(pow(SideLengthsbp,2)+2*SideLengthsbp*math.sqrt(math.floor(pow(SideLengthsbp,2)/4)+sbpHeight*sbpHeight))

        SideLengthsbp = float(input("Let side length 'a' equal: "))
        sbpHeight = float(input("Let height 'h' equal: "))
        sbpSA = surface_area_cone(SideLengthsbp,sbpHeight)
        print("The surface area of the cone is", sbpSA,"units²")
        return main()

    elif choice == "tp":
        #SAtp = ah+(al)+(bl)+(cl)
        def surface_area_tp(tpla, tplb, tplc, tph):
            return((tpla*l)+(tpla*tph)+(tplb*tph)+(tplc*tph))
        
        tpla = float(input("Let the triangular base length 'a' equal: "))
        tplb = float(input("Let the triangular side length b 'b' equal: "))
        tplc = float(input("Let the triangular side length c 'c' equal: "))
        tph = float(input("Let the prism height 'h' equal: "))
        l = math.sqrt((tplc*tplc)- math.pow((.5*tpla),2))
        SAtp = surface_area_tp(tpla, tplb, tplc, tph)
        print("The surface area of the triangular prism is", SAtp,"units²")
        return main()

    elif choice == "cylinder":
        #SA Cylinder = 2πrh + 2πr²
        def surface_area_cylinder(cylinderRadius, cylinderHeight):
            return (2 * piValueCylinder * cylinderRadius * cylinderHeight)+(2 * piValueCylinder * pow(cylinderRadius,2))

        piValueCylinder = float(input("Let pi 'π' equal: "))
        cylinderRadius = float(input("Let radius 'r' equal: "))
        cylinderHeight = float(input("Let height 'h' equal: "))
        cylinderSA = surface_area_cylinder(cylinderRadius, cylinderHeight)
        print("The surface area of the cylinder is:", cylinderSA,"units²")
        return main()
main()