import adsk.core, adsk.fusion, math, traceback
from .HexSpiralFunction import generate_hex_spiral  # Relative import

def run(context):
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        if not design:
            ui.messageBox('No active design found. Please create a new design.')
            return

        rootComp = design.rootComponent
        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)
        lines = sketch.sketchCurves.sketchLines

        # Draw hexagon (300 mm side length)
        side_length = 30  # Convert to cm (300 mm = 30 cm)
        center = adsk.core.Point3D.create(0, 0, 0)
        points = []
        for i in range(6):
            angle = math.radians(60 * i)
            x = center.x + side_length * math.cos(angle)
            y = center.y + side_length * math.sin(angle)
            points.append(adsk.core.Point3D.create(x, y, 0))
        for i in range(6):
            start_point = points[i]
            end_point = points[(i + 1) % 6]
            lines.addByTwoPoints(start_point, end_point)

        # Draw spiral
        spiralArray = generate_hex_spiral(0.5,0.5,side_length)  # Assumes mm output from function
        spiralArray = [adsk.core.Point3D.create(x, y, 0) for x, y in spiralArray]  # Convert mm to cm
        for i in range(len(spiralArray) - 1):
            start_point = spiralArray[i]
            end_point = spiralArray[i + 1]
            lines.addByTwoPoints(start_point, end_point)


        # Extrude hexagon
        hex_profile = sketch.profiles.item(0)
        if not hex_profile:
            ui.messageBox('No profile found for extrusion.')
            return
        extrudes = rootComp.features.extrudeFeatures
        extrude_input = extrudes.createInput(hex_profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        distance = adsk.core.ValueInput.createByReal(0.635)  # 0.25 inches = 0.635 cm
        extrude_input.setDistanceExtent(False, distance)
        extrudes.add(extrude_input)

        # ui.messageBox('Hexagon and spiral drawn, hexagon extruded.')

    except:
        ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))