# indrajala-demos

Runnable demos for [indrajala-ml](https://github.com/davidbarkhuizen/indrajala-ml): linear
(MADALINE) and backprop classifiers trained and plotted, UCI digits and MNIST recognition, the
numpy and Rust backends side by side, and drawing your own digits for the networks to read.

The demos, the matplotlib plotting (`indrajala_demos/graphics/`) and the tkinter digit capture
(`indrajala_demos/capture/`) lived in indrajala-ml until 2026-10 and moved here with their
history, so the library needs neither matplotlib nor tkinter
([indrajala-ml's demos-split workplan](https://github.com/davidbarkhuizen/indrajala-ml/blob/main/docs/demos-split-workplan.md)).
Commit messages from before the move cite indrajala-ml's pull requests as
`davidbarkhuizen/indrajala-ml#N`.

## Setup

indrajala-ml is a git submodule at `indrajala-ml/` (with its Rust crate at
`indrajala-ml/rust/`), so the demos run against an exact library commit; `data/` links to its
datasets. There are no PyPI releases before 1.0.

Requires Python >= 3.14, a Debian/Ubuntu host (`setup` apt-installs `python3-tk`) and
[rustup](https://rustup.rs).

```
git clone --recurse-submodules git@github.com:davidbarkhuizen/indrajala-demos.git
./cli setup          # submodules, .venv, indrajala-ml and its crate, matplotlib, the datasets
./cli demo           # interactive demo menu
./cli demo <n>       # run demo n directly
./cli test           # pytest tests/
./cli lint           # ruff check, ruff format --check, pyright
./cli build-rust     # rebuild the crate after the submodule moves
./cli fetch-data     # re-verify / re-fetch datasets
```

The tool pins (maturin, ruff, pyright) are read from `indrajala-ml/cli`, so both repositories
build and lint alike.

## Updating the library

A "Bump indrajala-ml/" PR moves the submodule (`git -C indrajala-ml checkout <commit>`, then
`git submodule update --recursive`, `./cli build-rust`, `./cli test`). CI runs the demos' tests
against the submodule's commit, so a library change that breaks a demo shows on that PR.

The menu also offers indrajala-ml's measurement tools (the per-op timing, the conv Rust/numpy
comparison, batch-size scaling), which live in the library because its timing protocol uses
them.

## Licence

MIT, as indrajala-ml.
