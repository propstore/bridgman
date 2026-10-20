# Goal
Correct the three demonstrated Propstore dimension-admission blockers in the
pinned Python 0.2 owner, without importing the unrelated master Rust rewrite.

# State
Isolated from 5eb6118bb2e346122aae6f7e3e9cd8581ec6c781. Unchanged maintenance
target: maintenance/python-0.2. Existing PR1 is a Dependabot Pygments update.
Propstore #332 merged at 3d15f12926a8f523ef425a6b11c6e75e8bddefd8.

# Decisions and why
Smallest correction: validate exponent dimensions before dimensionless-base
shortcuts; preserve a private proven-zero dimension term through the existing
walker and instantiate it against additive/comparison evidence; annotate the
public verify_expr input. Estimated 80 implementation lines plus regressions.
No unknown symbol may become a polymorphic zero. Traverse every authored child
before zero propagation, so zero cannot hide missing evidence or invalid sums.
The public dimensions-dict API retains its dimensionless zero instantiation;
relation checking and explanation use the private term consistently.
Kennedy 1997 original rendered p2 defines same-unit addition/comparison, p3
explicitly says zero is polymorphic and can take any units of measure. Visually
read page images from the local paper collection, with no text extraction.

# Surprises
The pinned Python baseline has no owner CI; add minimal locked Python tests and
typing CI as required by the delegated delivery. No unrelated owner worktrees
or user files are modified.

# Next step
Write and run failing owner regressions, implement the correction, publish a
focused maintenance draft with owner CI, obtain independent review, then repin
and verify the consumer. No merges, ready actions, existing body edits, or posts.

# Regression checkpoint
The new owner file produced 13 failing/6 passing cases on the pinned baseline.
Added exact rational arithmetic cases after the parent's further report; running
the same file against Propstore's installed pinned owner produced 16 failures
and 6 passes, including 2/2 and the preserved square-root exponent tree.
Corrected owner now passes all 22 tests (1.66s). Existing symbolic exponent
tests now explicitly bind their dimensionless exponent, instead of relying on
the old unbound-exponent acceptance. No supported bound symbolic powers removed.
Zero is private proven evidence, not missing evidence. Explain and verify share
relation instantiation. Literal zero, zero products, Abs and exact powers retain
polymorphism only after every authored operand has been checked.
Workflow action references verified with GitHub's commits API. actionlint 1.7.12
and zizmor 1.31.1 both passed; owner CI uses locked tests and package typing.
