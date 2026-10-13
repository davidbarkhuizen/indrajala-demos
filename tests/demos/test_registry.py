import ast
import importlib.util
from pathlib import Path

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


def test_every_entry_exists_and_defines_main():

    # read, not imported: some demos select the TkAgg backend on import, which a headless
    # machine (CI) can't load
    for info in DEMOS:
        spec = importlib.util.find_spec(info.module)
        assert spec is not None and spec.origin is not None, info.module
        tree = ast.parse(Path(spec.origin).read_text())
        assert any(isinstance(node, ast.FunctionDef) and node.name == "main" for node in tree.body), info.module
