import importlib

from indrajala_demos.demos.registry import DEMOS

# indrajala-ml's measurement tools, which the menu offers beside the demos
MEASUREMENT_TOOLS = [
    "indrajala_ml.measurement.conv_comparison",
    "indrajala_ml.measurement.layer_op_timing",
    "indrajala_ml.studies.batch_size_scaling_run",
]


def test_the_measurement_tools_are_registered():

    modules = {info.module for info in DEMOS}
    for module in MEASUREMENT_TOOLS:
        assert module in modules, module


def test_every_entry_imports_and_has_a_main():

    for info in DEMOS:
        assert callable(importlib.import_module(info.module).main), info.module
