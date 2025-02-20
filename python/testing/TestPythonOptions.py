import sys
import f3d

engine = f3d.engine(f3d.window.NONE)

assert engine.getOptions().getAsBool("interactor.axis") is False
assert engine.getOptions().getAsDouble("model.material.roughness") == 0.3
assert engine.getOptions().getAsInt("render.raytracing.samples") == 5
assert engine.getOptions().getAsDoubleVector("model.color.rgb") == [1.0, 1.0, 1.0]
assert engine.getOptions().getAsString("scene.up-direction") == "+Y"

closest = engine.getOptions().getClosestOption("scene-direction")
assert closest[0] == "scene.up-direction"
assert closest[1] == 3

options = f3d.options()
options.set("interactor.axis", True)
options.set("model.material.roughness", 0.7)
options.set("render.raytracing.samples", 2)
options.set("model.color.rgb", [0.0, 1.0, 1.0])
options.set("scene.up-direction", "-Z")

engine.setOptions(options)

assert engine.getOptions().getAsBool("interactor.axis") is True
assert engine.getOptions().getAsDouble("model.material.roughness") == 0.7
assert engine.getOptions().getAsInt("render.raytracing.samples") == 2
assert engine.getOptions().getAsDoubleVector("model.color.rgb") == [0.0, 1.0, 1.0]
assert engine.getOptions().getAsString("scene.up-direction") == "-Z"

assert len(options.getNames()) > 0

options2 = engine.getOptions()
options2.set("interactor.axis", False)
assert not options2.isSame(options, "interactor.axis")
options2.copy(options, "interactor.axis")
assert options2.isSame(options, "interactor.axis")
